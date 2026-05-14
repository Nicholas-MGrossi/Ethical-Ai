# JSON Schema Library for Compliance & Audit

This directory contains machine-readable JSON Schema definitions for all compliance, audit, and governance artifacts required by the Universal Standards for LLM-Based Assistants v1.0 and associated Technical and Ethical Architecture.

## Schema Inventory

### Core Operational Schemas

| Schema | Purpose | Primary Use |
|--------|---------|-------------|
| `data_lineage_schema.json` | Tracks every transformation applied to data from origin to final disposition | Audit trails, GDPR Article 30 Records of Processing Activities |
| `audit_log_schema.json` | Immutable event logging with cryptographic chaining | Security monitoring, incident response, regulatory inspection |
| `compliance_report_schema.json` | Periodic compliance assessment report against all frameworks | Management review, external audit, certification |
| `data_subject_request_schema.json` | Tracks individual privacy rights requests (access, deletion, etc.) | DSAR fulfillment, GDPR/CCPA compliance |
| `rollback_record_schema.json` | Documents every system rollback operation | Change management, disaster recovery, accountability |
| `consent_record_schema.json` | Records GDPR/CCPA/COPPA consent with verifiable evidence | Age-gating, parental consent, lawful basis tracking |
| `child_safety_incident_schema.json` | Documents all safeguarding incidents involving minors | COPPA compliance, NCMEC reporting, child protection |

## Usage Guidelines

### Validation

All schema artifacts are validated against JSON Schema Draft 7. Use standard validators:

```bash
# Using ajv-cli
ajv validate -s data_lineage_schema.json -d lineage_record.json

# Using Python jsonschema
python -m jsonschema -i audit_entry.json audit_log_schema.json
```

### Schema Evolution

Schema versions follow semantic versioning (`major.minor.patch`). When modifying schemas:

1. **Backward-compatible changes** (additive only): Increment minor version.
2. **Breaking changes**: Increment major version; provide migration tool.
3. **Bug fixes only**: Increment patch version.

All schema changes require:
- Update of `$schema` URI to new version.
- Migration guide in `SCHEMA_MIGRATION.md` (if breaking change).
- Community review period of minimum 30 days for major versions.

### Integration Points

#### Data Lineage

Every system component generating, transforming, or storing data must emit a lineage record:

```python
from uuid import uuid4
from datetime import datetime
import hashlib
import json

def create_lineage_record(stage_name: str, input_element: dict, output_element: dict):
    record = {
        "system_version": "1.0.0",
        "lineage_id": str(uuid4()),
        "data_flow": [{
            "stage": 1,
            "name": stage_name,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "element_id": str(uuid4()),
            "source": input_element.get("element_id"),
            "operation": stage_name,
            "custodian": "privacy_scrubber",
            "output_reference": output_element.get("element_id")
        }],
        "final_state": {
            "storage_location": output_element["storage"],
            "retention_expiry": output_element["retention_expiry"],
            "deletion_method": "cryptographic_shredding",
            "archival_status": "active"
        }
    }
    record["cryptographic_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(record, sort_keys=True).encode()
    ).hexdigest()
    return record
```

#### Audit Logging

All system actions must generate an audit event conforming to `audit_log_schema.json`:

```python
def log_audit_event(event_type: str, actor: dict, action: dict, system_state: dict):
    event = {
        "audit_event": {
            "event_id": str(uuid4()),
            "event_type": event_type,
            "severity": "info",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "epoch_millis": int(datetime.utcnow().timestamp() * 1000),
            "source_ip": "redacted_for_privacy",
            "user_agent": "redacted_for_privacy",
            "session_id": get_current_session_id(),
            "actor": actor,
            "action": action,
            "system_state": system_state,
            "compliance_tags": ["Universal_Standards", "GDPR"]
        }
    }
    # Compute chain hash
    previous = get_last_event_hash()
    event["chain"] = {
        "previous_event_hash": previous,
        "current_hash": "sha256:" + hashlib.sha256(json.dumps(event["audit_event"], sort_keys=True).encode()).hexdigest(),
        "merkle_root": None
    }
    store_immutable(event)
```

#### Compliance Reporting

Generate quarterly compliance assessment:

```bash
python scripts/generate_compliance_report.py \
  --period-start 2026-01-01 \
  --period-end 2026-03-31 \
  --output reports/Q1-2026-compliance.json \
  --format json
```

The resulting report validates against `compliance_report_schema.json`.

### Export Formats

All compliance data must be exportable in these formats:

1. **JSON**: Native schema format; used for API and interchange.
2. **JSONL**: Newline-delimited JSON for bulk log streaming.
3. **CSV**: Tabular summary for spreadsheet analysis (derived from JSON).
4. **PDF**: Human-readable report for publishing (generated from JSON template).

### Access Control

Schema files themselves are **public documentation**; no sensitive data resides in schema definitions. However, actual audit logs, lineage records, and reports contain sensitive information and must be protected:

- **Read Access:** `audit_readers` group (compliance, legal, security).
- **Write Access:** `audit_writers` group (system components only; no human direct writes).
- **Immutable:** Once written, records cannot be modified; corrections append new entries.

### Schema Development Workflow

1. **Design:** Draft schema changes with stakeholder review (legal, security, engineering).
2. **Implementation:** Create new schema file with version increment.
3. **Validation:** Test against representative sample data sets.
4. **Documentation:** Update this README and provide migration notes.
5. **Deployment:** Schema files deployed as immutable configuration; applications may read them at startup for validation.
6. **Announcement:** Notify all integrators of schema change via standard channels.

---

## References

- **Universal Standards for LLM-Based Assistants v1.0**: `UNIVERSAL_LLM_STANDARDS.md`
- **Technical and Ethical Architecture**: `TECHNICAL_ETHICAL_ARCHITECTURE.md`
- **Compliance Checklist**: `COMPLIANCE_CHECKLIST.md`
- **JSON Schema Specification**: <https://json-schema.org/>

---

**Maintainer:** Compliance & Governance Working Group  
**License:** CC0 1.0 Universal (Public Domain)  
**Last Updated:** 2026-05-14  
**Status:** Ratified — Stable
