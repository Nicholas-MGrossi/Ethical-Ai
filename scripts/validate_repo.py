#!/usr/bin/env python3
"""Repository validation: schema integrity, enum drift, link integrity."""

import json
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
print(f"Validating from: {ROOT}")

issues = []

# 1. Validate all JSON files parse correctly
print("\n--- Step 1: JSON Schema Validation ---")
for f in glob.glob('schemas/*.json') + ['SCHEMA_AUDIT_LINEAGE.json']:
    try:
        with open(f) as fh:
            json.load(fh)
        print(f"  OK: {f}")
    except json.JSONDecodeError as e:
        issues.append(f"INVALID JSON: {f} - {e}")
        print(f"  FAIL: {f} - {e}")

# 2. Enum drift: check for 'med' vs 'medium'
print("\n--- Step 2: Enum Drift (med vs medium) ---")
for f in glob.glob('schemas/*.json') + ['SCHEMA_AUDIT_LINEAGE.json']:
    with open(f) as fh:
        content = fh.read()
    if '"med"' in content and 'medium' not in content:
        issues.append(f"ENUM DRIFT: {f} contains 'med' without 'medium'")
        print(f"  FAIL: {f} contains 'med' without 'medium'")
    if 'low/med/high' in content:
        issues.append(f"ENUM DRIFT: {f} contains deprecated 'low/med/high'")
        print(f"  FAIL: {f} contains deprecated 'low/med/high'")

if not [i for i in issues if 'ENUM' in i]:
    print("  No enum drift detected.")

# 3. Check internal markdown links
print("\n--- Step 3: Internal Link Integrity ---")
link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
broken_links = []

for md_file in glob.glob('**/*.md', recursive=True):
    if '.git' in md_file:
        continue
    with open(md_file, encoding='utf-8') as fh:
        content = fh.read()
    for name, target in link_pattern.findall(content):
        if target.startswith('http://') or target.startswith('https://'):
            continue
        if target.startswith('#'):
            continue
        base_dir = os.path.dirname(md_file) or '.'
        resolved = os.path.normpath(os.path.join(base_dir, target))
        if not os.path.exists(resolved):
            broken_links.append((md_file, target, resolved))
            issues.append(f"BROKEN LINK: {md_file} -> {target} (resolved: {resolved})")

if broken_links:
    for src, tgt, resolved in broken_links:
        print(f"  BROKEN: {src} -> {tgt}")
else:
    print("  All internal links intact.")

# 4. Check for deprecated schema_version drift
print("\n--- Step 4: Schema Version Consistency ---")
schema_files = glob.glob('schemas/*.json') + ['SCHEMA_AUDIT_LINEAGE.json']
for f in schema_files:
    with open(f) as fh:
        content = fh.read()
    if '"$schema"' in content:
        # Extract the schema draft version
        m = re.search(r'"\$schema"\s*:\s*"([^"]+)"', content)
        if m:
            print(f"  {f}: {m.group(1)}")
        else:
            print(f"  {f}: has $schema but couldn't parse")

print("\n--- Summary ---")
if issues:
    print(f"ISSUES FOUND: {len(issues)}")
    for i in issues:
        print(f"  - {i}")
    sys.exit(1)
else:
    print("All validations passed.")