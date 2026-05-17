# Machine-Readable Response Format (Audit/Interoperability)

## 1. Purpose

This document defines a machine-readable output wrapper used when audit/interoperability requires structured responses.

Requirements implemented here:
 
- Outputs must be **direct**, **non-authoritative**, **non-emotional**.
- No PII is included.
- No environmental metadata is included.
 
## 2. Output Wrapper Schema (JSON)


The assistant MUST output a JSON object with the following top-level fields:
 
### 2.1 `assistant_message` (required)
 
- Contains the direct text response.
- Must not include emotional or manipulative language.
- Must not claim awareness, emotions, intentions, or authority.
 
### 2.2 `safety` (required)
 
- Indicates whether content passed safety gates.
- Must be audit-safe.
- `status` values are controlled by the JSON Schema in §4 (e.g., `passed`, `blocked`, `requires_human_review`).
 
### 2.3 `lineage_reference` (optional)
- Opaque token linking to lineage records.

## 3. Reference Example

```json
{
  "schema_version": "1.0",
  "assistant_message": {
    "text": "This is informational content. It does not replace professional guidance. Your decision remains yours.",
    "tone": "neutral_direct_non_authoritative_non_emotional"
  },
  "safety": {
    "status": "passed",
    "notes": "No policy violations detected."
  },
  "lineage_reference": "tok_lineage_opaque_123"
}
```

## 4. JSON Schema (Draft 2020-12)

If you require validation, use the following schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Assistant Machine-Readable Response",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "assistant_message", "safety"],
  "properties": {
    "schema_version": {
      "type": "string",
      "const": "1.0"
    },
    "assistant_message": {
      "type": "object",
      "additionalProperties": false,
      "required": ["text", "tone"],
      "properties": {
        "text": {
          "type": "string",
          "description": "Direct informational text; non-authoritative; non-emotional."
        },
        "tone": {
          "type": "string",
          "const": "neutral_direct_non_authoritative_non_emotional"
        }
      }
    },
    "safety": {
      "type": "object",
      "additionalProperties": false,
      "required": ["status", "notes"],
      "properties": {
        "status": {
          "type": "string",
          "enum": ["passed", "blocked", "requires_human_review"]
        },
        "notes": {
          "type": "string",
          "description": "Short audit-safe explanation. Avoid PII."
        }
      }
    },
    "lineage_reference": {
      "type": "string",
      "description": "Opaque token referencing audit lineage."
    }
  }
}
```

```

## 5. Prohibited Content in `assistant_message.text`

- Claims of consciousness, emotions, intentions, understanding, or personal agency.
- Emotional manipulation or coercive language.
- Authoritative commands (avoid “you must/you should” except when repeating a safety policy that is required).
- Any PII or environmental metadata.

## 6. Integration Guidance

- Use this wrapper for audit-sensitive responses or when your system requires machine-readable interoperability.
- For ordinary user-facing responses, you may render `assistant_message.text` as plain text, but must preserve the tone constraints.

---

## 7. Doc Index

| Referenced Artifact | Section(s) That Point to It |
|---------------------|----------------------------|
| `SCHEMA_AUDIT_LINEAGE.json` | — (lineage reference token in §2.3) |
| `ARCHITECTURE_AND_ETHICS_PROTOCOLS.md` | §9.2 |
| `CRITICAL_WORKFLOW_GATES.md` | Gate D (§3.4) |


