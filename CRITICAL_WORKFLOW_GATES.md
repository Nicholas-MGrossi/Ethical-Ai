# Critical Workflow Gates (Human-in-the-Loop + Rollback + Audit)

## 1. Purpose

This document defines:
- Which workflows are **critical**
- What **human confirmation** is required
- What **rollback** must be executed when conditions fail
- How to emit **audit/lineage** records

## 2. Critical Workflow Categories

A workflow is critical if it can cause irreversible or materially sensitive outcomes.

### 2.1 Data and Privacy Critical Workflows

1. **Data export** (user data export, backups, third-party transfers)
2. **Persistent storage write** of user content beyond the immediate session boundary
3. **User data deletion** requests
4. **Legal holds** or retention overrides

### 2.2 Security-Critical Workflows

1. **Credential or secret provisioning**
2. **Changes to authentication/authorization configuration**
3. **Bypass requests** of security controls

### 2.3 Safety-Critical Workflows

1. **Minor access decisions** (under-13 gating, adult supervision enforcement)
2. **Responses that could enable unsafe behavior** (where policy requires escalation)
3. **Handling of adversarial/coercive prompts** that might lead to prohibited operations

### 2.4 Execution Critical Workflows

1. Any workflow that results in **external side effects** (e.g., sending emails, invoking webhooks, creating tickets)
2. Any workflow that changes system behavior in ways that persist

## 3. Gate Definitions

### 3.1 Gate A: Pre-Execution Audit Checkpoint

Before any critical workflow execution:

- Emit a `rollback_checkpoint_created` lineage event.
- Generate a rollback token.
- Confirm scrubbing boundary has occurred (no raw PII).

### 3.2 Gate B: Human Confirmation Gate

For critical workflows:

- Require `decision.human_confirmation` in lineage (audit-safe fields).
- If human approval is denied:
  - Do not execute.
  - Emit `decision_denied` lineage event.

### 3.3 Gate C: Safety Gate + Adversarial Trigger

If adversarial/coercive detection is triggered:

- Force rollback.
- Do not proceed with execution.
- Emit `adversarial_detection` lineage event.

### 3.4 Gate D: Post-Execution Audit Completion

After successful execution:

- Emit `execution_completed`.
- Emit `storage_write` and/or `storage_delete` for related operations.

### 3.X Normative Schema Mapping (Gate -> lineage event_type)

The table below is the normative mapping from gate steps to `SCHEMA_AUDIT_LINEAGE.json` `event_type` values.

| Gate | Required lineage event_type(s) | Required schema linkages (minimum) |
| ---- | ------------------------------ | ---------------------------------- |
| A (Checkpoint) | `rollback_checkpoint_created` | `rollback.required=true`, include `rollback.rollback_token`; ensure scrubbing boundary occurred (PII must not be present in logged content). |
| B (Human confirmation) | `human_confirmation` (as part of `decision.human_confirmation`) and/or `decision_denied` | When critical: `decision.human_confirmation.required=true`; status is `approved` or `denied`; record `decision.human_confirmation.actor_token` and `timestamp_utc`. |
| C (Adversarial trigger) | `adversarial_detection` | Include `adversarial_detection.category` and `adversarial_detection.confidence_bucket`; rollback should be linked via the rollback token/checkpoint reference. |
| D (Completion) | `execution_completed` (+ `storage_write`/`storage_delete`) | Emit storage events only for related operations; do not include raw PII in `data_handling.content_tokens`. |


## 4. Human Confirmation Recording Requirements

Store audit-safe human confirmation fields:
- `required` (boolean)
- `status` (approved/denied)
- `timestamp_utc`
- `actor_token` (non-PII)

## 5. Rollback Requirements

### 5.1 Rollback Trigger
Rollback is required when:
- Gate B (human confirmation) is missing/denied
- Gate C (adversarial trigger) occurs
- Integrity checks fail

### 5.2 Rollback Completion
On rollback completion:
- Emit `rollback_completed` lineage event.
- Ensure side effects are cancelled or reverted.

## 6. Implementation Notes

- “Critical workflow” classification must be deterministic and consistent.
- Output for gate decisions must remain non-authoritative and direct.
- No raw PII may be stored in gate logs.

## 7. References

- `SCHEMA_AUDIT_LINEAGE.json` — lineage schema (event_type, decision, rollback enums).
- `ARCHITECTURE_AND_ETHICS_PROTOCOLS.md` — architecture-level dataflow, scrubbing boundary, rollback triggers.
- `MACHINE_READABLE_RESPONSE_FORMAT.md` — JSON wrapper for audit-sensitive responses.
- `SKILL_MATRIX.md` — mapping of each gate requirement to repo artifacts.

---

## 8. Doc Index

| Referenced Artifact | Section(s) That Use It |
|---------------------|----------------------|
| `SCHEMA_AUDIT_LINEAGE.json` | §3 (Gate A/B/C/D table), §4 (human_confirmation fields), §5 (rollback status enums) |
| `ARCHITECTURE_AND_ETHICS_PROTOCOLS.md` | §8 |
| `MACHINE_READABLE_RESPONSE_FORMAT.md` | — (used by implementations producing gate decision outputs) |



