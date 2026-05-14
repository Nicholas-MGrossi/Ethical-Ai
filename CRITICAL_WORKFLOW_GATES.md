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
- Require a `human_confirmation` field in lineage.
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

- `SCHEMA_AUDIT_LINEAGE.json` for lineage schema.
- `ARCHITECTURE_AND_ETHICS_PROTOCOLS.md` for architecture-level dataflow.

