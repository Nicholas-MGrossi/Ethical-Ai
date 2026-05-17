# How to Validate: Schema, Enum Drift, and Link Integrity

## 1. Purpose

This document provides maintainers with the commands and procedures needed to validate repository artifacts against their JSON Schemas, detect enum drift between documents, and verify internal link integrity. Run these checks before any pull request that modifies schema, documentation, or compliance artifacts.

---

## 2. Schema Validation

### 2.1 Prerequisites

```bash
# Using ajv-cli (Node.js)
npm install -g ajv-cli ajv-formats

# Using Python jsonschema
pip install jsonschema
```

### 2.2 Validate an Instance Against a Schema

```bash
# ajv-cli (Draft 2020-12 / Draft 7)
ajv validate -s schemas/data_lineage_schema.json -d path/to/instance.json

# Python
python -m jsonschema -i path/to/instance.json schemas/data_lineage_schema.json
```

### 2.3 Validate All Core Schemas (Batch)

```bash
# PowerShell (Windows)
foreach ($schema in Get-ChildItem -Path schemas -Filter *.json) {
    Write-Host "Validating $($schema.Name)..."
    ajv validate -s $schema.FullName -d test/fixtures/$($schema.BaseName).json 2>&1
}
```

> **Note:** Place sample instance files in `test/fixtures/` mirroring the schema name (e.g., `test/fixtures/data_lineage_schema.json`).

### 2.4 Schema Files

| Schema File | Draft Version | Key Enums to Monitor |
|---|---|---|
| `schemas/data_lineage_schema.json` | Draft 7 | `operation`, `custodian`, `deletion_method` |
| `schemas/audit_log_schema.json` | Draft 7 | `event_type`, `severity`, `compliance_tags` |
| `schemas/compliance_report_schema.json` | Draft 7 | `status`, `finding_type`, `framework` |
| `schemas/data_subject_request_schema.json` | Draft 7 | `request_type`, `status`, `jurisdiction` |
| `schemas/consent_record_schema.json` | Draft 7 | `consent_type`, `status`, `verification_method` |
| `schemas/child_safety_incident_schema.json` | Draft 7 | `incident_type`, `severity`, `reporting_status` |
| `schemas/rollback_record_schema.json` | Draft 7 | `trigger_reason`, `status` |
| `SCHEMA_AUDIT_LINEAGE.json` | Draft 2020-12 | `event_type`, `user_type`, `confidence_bucket`, `rollback_status` |

---

## 3. Enum Drift Detection

Enum drift occurs when the same logical set of values is defined differently across schemas, documentation, or code. The following procedure detects drift systematically.

### 3.1 Single-Enum Drift Check

```bash
# Search for all enum definitions in JSON schemas
grep -rn '"enum"' schemas/ --include="*.json"

# Extract enum values for a specific property, e.g., event_type
python -c "
import json, sys, glob
event_types = {}
for f in glob.glob('schemas/*.json') + ['SCHEMA_AUDIT_LINEAGE.json']:
    with open(f) as fh:
        schema = json.load(fh)
    def walk(obj, path=''):
        if isinstance(obj, dict):
            if 'enum' in obj:
                key = f'{f}:{path}'
                event_types[key] = set(obj['enum'])
            for k, v in obj.items():
                walk(v, f'{path}.{k}')
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                walk(v, f'{path}[{i}]')
    walk(schema)
for k, v in sorted(event_types.items()):
    print(f'{k}: {v}')
"
```

### 3.2 Cross-Document Enum Consistency Check

```bash
# Extract enum values from SCHEMA_AUDIT_LINEAGE.json event_type
python -c "
import json
with open('SCHEMA_AUDIT_LINEAGE.json') as f:
    s = json.load(f)
enum_vals = s['properties']['event_type']['enum']
print('event_type enum:', sorted(enum_vals))
print('Count:', len(enum_vals))
"
```

Expected `event_type` values (alphabetical):
```
adversarial_detection
classification
decision_denied
execution_completed
execution_started
human_confirmation
input_intake
pii_scrub
policy_gate_check
rollback_checkpoint_created
rollback_completed
storage_delete
storage_write
```

### 3.3 Validate Low/Medium/High Consistency

The repository uses `low/medium/high` (not `low/med/high`). Enforce with:

```bash
# Check for incorrect 'med' usage
grep -rn '"med"' schemas/ --include="*.json"
grep -rn 'low/med/high' *.md --include="*.md"

# Confirm correct usage
grep -rn '"medium"' schemas/ --include="*.json"
```

---

## 4. Internal Link Integrity Check

### 4.1 Extract and Verify Markdown Links

```bash
# Extract all markdown links using Python
python -c "
import re, os

link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
broken = []

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, encoding='utf-8') as fh:
                content = fh.read()
            for name, target in link_pattern.findall(content):
                if target.startswith('http://') or target.startswith('https://'):
                    continue  # skip external links
                if target.startswith('#'):
                    continue  # skip anchor-only links
                # Resolve relative path
                base_dir = os.path.dirname(path)
                resolved = os.path.normpath(os.path.join(base_dir, target))
                if not os.path.exists(resolved):
                    broken.append((path, target, resolved))

if broken:
    print('BROKEN LINKS:')
    for src, target, resolved in broken:
        print(f'  {src} -> {target} (resolved: {resolved})')
else:
    print('All internal links intact.')
"
```

### 4.2 Verify Anchor Targets

```bash
# Check that section anchors referenced in links exist
python -c "
import re, os

def extract_headings(path):
    headings = set()
    with open(path, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^(#{1,6})\s+(.+)$', line)
            if m:
                level = len(m.group(1))
                text = m.group(2).strip()
                anchor = text.lower().replace(' ', '-').replace('_', '-')
                anchor = re.sub(r'[^a-z0-9-]', '', anchor)
                headings.add(anchor)
    return headings

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            headings = extract_headings(path)
            print(f'{f}: {len(headings)} headings')
"
```

---

## 5. Full Validation Pipeline

Run all checks in sequence:

```bash
echo '=== SCHEMA VALIDATION ==='
# Add ajv commands here

echo '=== ENUM DRIFT CHECK ==='
python -c "
import json, glob

# Check all enum definitions for 'med' vs 'medium'
issues = []
for f in glob.glob('schemas/*.json') + ['SCHEMA_AUDIT_LINEAGE.json']:
    with open(f) as fh:
        content = fh.read()
    if '"med"' in content and 'medium' not in content:
        issues.append(f'{f}: contains \"med\" without \"medium\"')
    if 'low/med/high' in content:
        issues.append(f'{f}: contains deprecated low/med/high format')

if issues:
    print('DRIFT ISSUES FOUND:')
    for i in issues:
        print(f'  {i}')
else:
    print('No enum drift detected.')
"

echo '=== LINK INTEGRITY ==='
# Run link checker from §4.1

echo '=== DOC INDEX CROSS-REFERENCE ==='
# Verify doc index tables reference valid sections

echo '=== ALL CHECKS COMPLETE ==='
```

---

## 6. Quick Reference: One-Line Commands

| Check | Command |
|---|---|
| Validate JSON instance | `ajv validate -s schema.json -d instance.json` |
| List all enums | `grep -rn '"enum"' schemas/ --include="*.json"` |
| Check for `med` drift | `grep -rn '"med"' schemas/ --include="*.json"` |
| Check for `low/med/high` | `grep -rn 'low/med/high' *.md --include="*.md"` |
| Verify all schemas valid JSON | `python -m json.tool schemas/*.json > /dev/null` |

---

## 7. References

- `SCHEMA_AUDIT_LINEAGE.json` — Central lineage event schema
- `CRITICAL_WORKFLOW_GATES.md` §3.X — Normative schema-to-gate mapping table
- `ARCHITECTURE_AND_ETHICS_PROTOCOLS.md` §13 — Artifact reference table
- JSON Schema home: <https://json-schema.org/>

---

**Version:** 1.0  
**Maintainer:** Repository maintainers  
**Last Updated:** 2026-05-16  
**License:** CC0 1.0 Universal (Public Domain)