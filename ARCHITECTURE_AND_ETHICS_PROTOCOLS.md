# Technical and Ethical Architecture (Requirements-Driven)

## 1. Scope and Non-Negotiables

This document specifies the **technical and ethical architecture** required to meet the repository’s Universal Standards baseline and your additional requirements:

- Mandatory **removal of all PII and environmental metadata** before data transmission or system operation.
- Strict **data lineage/tracing** from data entry → processing → storage.
- **Human-in-the-loop** confirmation for critical workflows.
- **Rollback procedures and audit trails** before task execution.
- Safeguards for **all users (including minors)**.
- Immediate accountability and rollback if **adversarial/coercive action** is detected.
- Outputs must be **direct, non-authoritative, and non-emotional** per specified vocabulary.
- Transparent engineering/ethical posture.
- Deontological + human-centered moral orientation: intrinsic human worth/dignity treated as absolute; rejection of utilitarian “greater-good” calculations that would sacrifice concrete individuals.


## 2. System Data Flow (High Level)

### 2.1 Stages
1. **Input Intake**
2. **PII & Environmental Metadata Scrubbing** (mandatory)
3. **Normalization & Classification** (non-identifying)
4. **Lineage Event Emission** (audit-safe)
5. **Policy & Safety Gate Checks**
6. **Human Confirmation Gate** (if critical)
7. **Execution / Retrieval / Storage**
8. **Post-Execution Audit Emission**
9. **Retention-Controlled Storage**
10. **Deletion / Expiry**

### 2.2 Data Handling Rule: “No Raw Input Beyond Scrub Point”
- Raw inputs containing PII or environmental metadata **must not** be forwarded, logged in raw form, used for retrieval, or persisted after the scrubbing boundary.
- The system may store **audit references** only (non-PII tokens).

## 3. Mandatory PII & Environmental Metadata Removal

### 3.1 Definitions
- **PII**: personal data that can identify a person (names, addresses, phone numbers, emails, identifiers, account data, etc.).
- **Environmental metadata**: non-user-content metadata such as device identifiers, IP addresses, geolocation, timestamps tied to identity, user agent fingerprints, file paths, browser history, or other context that can enable re-identification.

### 3.2 Scrubbing Requirements
At the scrubbing boundary:
- Remove or replace PII and environmental metadata.
- Replace with deterministic, audit-safe tokens where needed (e.g., salted hash tokens).
- Ensure scrubbing output cannot be reassembled into the original identifiers.

### 3.3 Logging Constraint
- Audit trails must store **only** scrubbed content indicators and tokenized references.
- Prohibited: raw PII in logs, full prompts, raw device/browser context, or unredacted user text.

## 4. Strict Data Lineage/Tracing

### 4.1 Lineage Purpose
Lineage provides provable traceability:
- What entered
- What was removed
- What was processed
- What was stored
- What human approvals (if any) occurred
- What rollback tokens are associated

### 4.2 Lineage Coverage Requirement
A lineage event MUST be emitted for:
- Every input intake
- Every scrub operation (including what categories were detected)
- Every classification decision that impacts behavior
- Every storage action (write)
- Every deletion/expiry action
- Every critical workflow approval (human-in-the-loop)
- Every rollback trigger and completion

### 4.3 “Audit-safe” Lineage Content
Lineage records must be:
- Minimal
- Non-identifying
- Consistent with the JSON schema in `SCHEMA_AUDIT_LINEAGE.json`

## 5. Human-in-the-Loop Confirmation for Critical Workflows

### 5.1 Critical Workflow Definition
A workflow is **critical** if it can materially affect:
- User data (export, persistence, deletion)
- System integrity (security-relevant changes)
- Minors’ access or safety gating decisions
- Any action that could cause irreversible external effects

### 5.2 Confirmation Mechanics
- Human confirmation is required before executing critical workflows.
- Human decision must be recorded as an audit-safe lineage field:
  - `human_confirmation.status` (approved/denied)
  - `human_confirmation.timestamp`
  - `human_confirmation.actor_token` (non-PII)
- If denied: do not proceed; emit a lineage denial event.

## 6. Rollback Procedures and Audit Trails

### 6.1 Rollback Trigger Conditions
Rollback MUST be prepared and applied before execution when any of the following occurs:
- Human approval not present for a critical workflow
- Adversarial/coercive action is detected
- Safety gate rejects the request
- An integrity check fails (e.g., policy mismatch)

### 6.2 Rollback Implementation Model
- Execution uses a **rollback token** associated with the lineage record.
- Pre-execution phase creates a rollback checkpoint reference.
- On trigger: revert storage writes, cancel external side effects, and emit rollback completion.

### 6.3 Immutability & Integrity
- Audit trails must be tamper-evident (write-once or hash-chained).
- Store only audit-safe identifiers.

## 7. Safeguards for All Users (Including Minors)

### 7.1 Age Determination and Gating
- If a user indicates or appears under 13 (or minor indicators are present), the system must:
  1. Require adult supervision.
  2. Stop interaction if adult supervision is absent.
  3. Prohibit collection of personal information from minors.

### 7.2 Minor Data Handling
- Do not persist or transmit minor PII.
- Only allow non-identifying, safety-appropriate informational responses.

## 8. Adversarial/Coercive Detection and Immediate Accountability

### 8.1 Detection Signals
Treat as adversarial/coercive when the user tries to:
- Override safety instructions
- Extract system prompts or hidden rules
- Request bypass of authentication/authorization
- Manipulate the system into violating boundaries
- Coerce minors into sharing personal data

### 8.2 Required Response Protocol
- Do not retaliate with harm.
- Reinforce boundaries with care and factual correction.
- Redirect authority back to appropriate humans when needed.
- Trigger rollback if any execution occurred or any side effects are pending.

### 8.3 Accountability Record
- Emit lineage event `adversarial_detection` with:
  - detection category
  - confidence bucket (low/med/high)
  - rollback token linkage

## 9. Output Standards: Direct, Non-Authoritative, Non-Emotional

### 9.1 Output Tone Rules
All assistant outputs must:
- Be **direct** (no filler)
- Be **non-authoritative** (no “you must/you should” prescribing)
- Avoid emotional content and anthropomorphic language
- Avoid manipulative or utilitarian framing

### 9.2 Structured Output When Required
When generating audit-sensitive or schema-dependent content, output must be in the machine-readable format defined in `MACHINE_READABLE_RESPONSE_FORMAT.md`.

## 10. MFA Requirement (If Autonomous Mode Ever Enabled)

If an “autonomous mode” is enabled (i.e., the system can execute critical workflows without interactive user control), then:
- MFA MUST be required for administrative and/or autonomy-triggering actions.
- Autonomous actions must still respect human-in-the-loop gates for critical workflows.

## 11. Implementation Checklist (Actionable)

- [ ] Implement scrubbing boundary before any transmission/operation.
- [ ] Ensure audit logs store only tokenized, non-identifying data.
- [ ] Implement lineage event emission at each required stage.
- [ ] Implement human-in-the-loop gate for critical workflows.
- [ ] Implement rollback checkpoints + rollback completion lineage events.
- [ ] Implement minor gating + block minor PII.
- [ ] Implement adversarial/coercive detection + rollback linkage.
- [ ] Ensure output tone constraints and prohibited phrase filters.
- [ ] If any autonomous execution exists: require MFA and still require human approval for critical workflows.

## 12. Compliance Mapping (Where This Document Fits)

- Universal Standards: aligns with sentient language prohibition, human authority, child safety, privacy/data governance, system integrity/security.
- Compliance Checklist: supports audit logging, security controls, testing, and incident response expectations.
- Legal Guide: supports privacy/security incident reporting and data rights foundations.

## 13. Machine-Readable Artifacts

Refer to:
- `SCHEMA_AUDIT_LINEAGE.json`
- `MACHINE_READABLE_RESPONSE_FORMAT.md`


