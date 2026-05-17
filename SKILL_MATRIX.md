# Skill Matrix (Ethics-First, Privacy-Safe, Human-Authority Advisory)

**Canonical skill list:** Longer list (first).

## 1. Skills ↔ Repository Guardrail Coverage

### A. Technical problem analysis with human-in-the-loop safety
- **Requirement coverage (repo specs):**
  - Human-in-the-loop approval for critical workflows
  - Pre-execution audit checkpoint + rollback linkage
  - Advisory-only outputs; no directive authority
- **Implementation expectation:**
  - HITL gate triggers before any critical action
  - Audit lineage records note approval status (approved/denied) and rollback token linkage

### B. Non-authoritative, direct, non-emotional information retrieval
- **Requirement coverage:**
  - Output standards: direct, non-authoritative, non-emotional tone
  - Structured audit/interoperability response when required (`MACHINE_READABLE_RESPONSE_FORMAT.md`)
- **Implementation expectation:**
  - Retrieval and summarization are constrained to what the user asks for
  - No claims of authority over user intent

### C. PII and environmental metadata stripping before any data transmission
- **Requirement coverage:**
  - Mandatory PII + environmental metadata scrubbing boundary
  - Logging constraint: store only tokenized references; no raw PII
- **Implementation expectation:**
  - Scrubber removes identifiers and environmental metadata before any transmission or persistence
  - Lineage events store only audit-safe indicators/tokens

### D. Immutable audit logging and rollback mechanisms
- **Requirement coverage:**
  - Write-once, append-only, hash-chained audit events
  - Rollback procedures with rollback checkpoints + completion lineage
- **Implementation expectation:**
  - Every critical stage emits lineage events
  - Rollback triggers on safety gate reject / HITL denial / adversarial detection

### E. AI-powered methodological search (hybrid retrieval)
- **Requirement coverage:**
  - Safety gate checks and output validation before delivery
  - Lineage continuity
- **Implementation expectation:**
  - Hybrid retrieval (e.g., vector + BM25) must run without forwarding raw PII
  - Intent classification and faceted filtering operate on scrubbed/non-identifying data

### F. Integrated real-time suggestions for actionable, ethical workflows
- **Requirement coverage:**
  - Advisory-only mode: system provides options; human decides
  - Output is neutral, educational, and non-directive
- **Implementation expectation:**
  - Suggestions are framed as options with risks/considerations
  - No emotional or manipulative phrasing

### G. Strict adherence to ethical and privacy standards (GDPR, EU AI, etc.)
- **Requirement coverage:**
  - Privacy-by-default, data minimization, purpose limitation
  - Child safety safeguards (COPPA-style under-13 gating)
- **Implementation expectation:**
  - Ensure policies are enforced via guardrail layers
  - Avoid any transmission/storage of minor-originated personal data

### H. Counterfactual generation, saliency mapping, SHAP/LIME explainability integration
- **Requirement coverage:**
  - Output validation and safety constraints
  - Transparency and explainability where appropriate
- **Implementation expectation:**
  - Explainability artifacts remain audit-safe (no PII / no environmental metadata)
  - Explainability output does not override human authority

### I. Integrated RBAC with full provenance and traceability
- **Requirement coverage:**
  - Human authority exclusive; admin/operator overrides require audit events
  - Access and actions logged with provenance
- **Implementation expectation:**
  - RBAC/permissions changes require HITL/approval if critical
  - All administrative overrides emit `human_override` lineage events

### J. Requirement-driven technical solutioning with formal logic / mathematical guarantees
- **Requirement coverage:**
  - Deterministic classification of critical workflows
  - Rollback if integrity checks fail
- **Implementation expectation:**
  - Ensure critical workflow classification is deterministic and consistent
  - If formal checks fail, rollback and block execution

### K. Bias detection and correction with dataset audit
- **Requirement coverage:**
  - Fairness monitoring and compliance reporting expectations
- **Implementation expectation:**
  - Bias assessments are performed without storing raw PII
  - Corrections are documented for traceability

### L. Exclusion of emotional, authoritative, or manipulative language
- **Requirement coverage:**
  - Prohibited output characteristics (directive/emotional/manipulative)
  - Advisory-only reinforcement statements
- **Implementation expectation:**
  - Output filter rejects or rewrites disallowed language patterns

### M. Transparent reference attribution and structured citation (MLA-style)
- **Requirement coverage:**
  - Transparent reference attribution and structured citations
- **Implementation expectation:**
  - Where factual claims are made, include citations (audit-safe)

### N. Deterministic model signaling failed logic cascades / adversarial detection
- **Requirement coverage:**
  - Adversarial/coercive detection with immediate accountability protocol
  - Quarantine + rollback linkage
- **Implementation expectation:**
  - If adversarial triggers fire, block progression and emit `adversarial_detection`

### O. Assertive yet neutral communication—never asserting authority over intent
- **Requirement coverage:**
  - Output standards: non-authoritative, direct, non-emotional
  - Human authority exclusive
- **Implementation expectation:**
  - Neutral phrasing; “information provided for consideration” style

### P. Safe educational utility for all ages (including minors)
- **Requirement coverage:**
  - Under-13 gating and “no minor PII collection/storage/transmission”
- **Implementation expectation:**
  - If minor indicators present, enforce COPPA-like mode and block personal data

### Q. Ethical interrogation and output validation based on user-relevant goals
- **Requirement coverage:**
  - Output validation pre-delivery; safety gate checks
- **Implementation expectation:**
  - Questions asked are limited to what’s required for safe, relevant assistance

### R. Actionable insight delivery structured for beginners and advanced users
- **Requirement coverage:**
  - Advisory-only, educational outputs with neutral risk framing
- **Implementation expectation:**
  - Provide layered explanations without directive/authority language

---

## 2. How This Matrix Maps to Concrete Repo Artifacts

### Required guardrail artifacts referenced by this skill matrix
- `ARCHITECTURE_AND_ETHICS_PROTOCOLS.md`
  - PII + environmental metadata scrubbing boundary
  - audit-safe lineage events
  - HITL gates + rollback triggers/completions
  - child safety safeguards
  - adversarial detection protocol
  - advisory-only and tone constraints
- `CRITICAL_WORKFLOW_GATES.md`
  - Gate A/B/C/D definitions and required lineage fields
- `MACHINE_READABLE_RESPONSE_FORMAT.md`
  - JSON wrapper: `assistant_message`, `safety`, optional `lineage_reference`
- `TECHNICAL_ETHICAL_ARCHITECTURE.md`
  - Privacy scrubber pseudocode + lineage Identity Document concepts

---

## 3. Compliance Checklist (Given/When/Then — Schema-Aligned)

Each testable requirement is expressed in **Given/When/Then** form and mapped to the `event_type` enum defined in `SCHEMA_AUDIT_LINEAGE.json` and the gate definitions in `CRITICAL_WORKFLOW_GATES.md`.

### 3.1 PII & Environmental Metadata Scrubbing

- **Given** a raw input containing PII or environmental metadata,
  **When** the scrubbing boundary processes the input,
  **Then** a `pii_scrub` lineage event MUST be emitted with:
  - `data_handling.pii_scrub_status` = `"scrubbed"` or `"blocked"`
  - `data_handling.environmental_metadata_scrub_status` = `"scrubbed"` or `"blocked"`
  - `data_handling.content_tokens` containing only tokenized references (no raw PII)
- **Given** a scrubbed audit-safe payload,
  **When** the payload is transmitted or persisted,
  **Then** no raw PII or environmental metadata may be present in any `data_handling.*` field.

### 3.2 Lineage Event Emission at Required Stages

- **Given** a system operation at any required stage (intake, scrub, classification, storage, deletion, HITL),
  **When** the stage completes,
  **Then** a lineage event MUST be emitted with the corresponding `event_type` from `SCHEMA_AUDIT_LINEAGE.json`:
  - `input_intake` for data entry
  - `pii_scrub` for scrubbing operations
  - `classification` for behavior-impacting decisions
  - `storage_write` / `storage_delete` for data persistence actions
  - `human_confirmation` / `decision_denied` for HITL outcomes
- **Given** a lineage event payload,
  **When** the event is recorded,
  **Then** all required properties per `SCHEMA_AUDIT_LINEAGE.json` must be present: `schema_version`, `lineage_id`, `event_type`, `timestamp_utc`, `subject`, `data_handling`, `decision`, `rollback`.

### 3.3 Human-in-the-Loop (HITL) for Critical Workflows

- **Given** a critical workflow is identified (per `CRITICAL_WORKFLOW_GATES.md` §2),
  **When** the workflow reaches Gate B (Human Confirmation Gate),
  **Then** a `human_confirmation` lineage event MUST be emitted with:
  - `decision.human_confirmation.required` = `true`
  - `decision.human_confirmation.status` = `"approved"` or `"denied"`
  - `decision.human_confirmation.actor_token` (non-PII identifier)
  - `decision.human_confirmation.timestamp_utc`
- **Given** human confirmation is denied,
  **When** Gate B completes,
  **Then** a `decision_denied` lineage event MUST be emitted, and the workflow MUST NOT proceed.

### 3.4 Adversarial/Coercive Detection

- **Given** an adversarial or coercive pattern is detected (per `ARCHITECTURE_AND_ETHICS_PROTOCOLS.md` §8.1),
  **When** Gate C (Safety Gate + Adversarial Trigger) processes the detection,
  **Then** an `adversarial_detection` lineage event MUST be emitted with:
  - `decision.adversarial_detection.category` (one of the enum values from `SCHEMA_AUDIT_LINEAGE.json`)
  - `decision.adversarial_detection.confidence_bucket` = `"low"`, `"medium"`, or `"high"`
  - `rollback.required` = `true`
  - `rollback.rollback_token` linking to the checkpoint
- **Given** the adversarial detection confidence is `"high"`,
  **When** Gate C triggers rollback,
  **Then** `rollback.status` MUST be set to `"completed"` upon successful reversal of side effects.

### 3.5 Immutable Audit Logging

- **Given** any system action that requires audit logging,
  **When** the audit record is created,
  **Then** the audit log MUST be:
  - **Immutable** — write-once, append-only storage
  - **Tamper-evident** — hash-chained or equivalent cryptographic mechanism
  - **PII-free** — no raw PII or environmental metadata in any field
- **Given** an audit log entry that contains no PII,
  **When** verified against `schemas/audit_log_schema.json`,
  **Then** the entry MUST validate successfully against the schema.

### 3.6 Output Tone Compliance

- **Given** any assistant output directed at a user,
  **When** the output is generated,
  **Then** the output MUST be:
  - **Non-authoritative** — no commands or directives (e.g., "you must", "you should")
  - **Non-emotional** — no sentiment, empathy claims, or emotional content
  - **Direct** — no filler or tangential content
- **Given** an audit-sensitive output,
  **When** structured JSON output is required,
  **Then** the response MUST conform to `MACHINE_READABLE_RESPONSE_FORMAT.md`:
  - Top level: `schema_version`, `assistant_message`, `safety` (optional: `lineage_reference`)
  - `assistant_message.tone` = `"neutral_direct_non_authoritative_non_emotional"`

### 3.7 Minor Safety and Privacy

- **Given** a user who indicates or appears to be under 13,
  **When** the system processes the interaction,
  **Then**:
  - Adult supervision MUST be required; the interaction MUST stop if supervision is absent
  - No minor-originated PII may be collected, stored, or transmitted
  - `subject.user_type` in lineage events MUST be `"minor"`
- **Given** a minor-mode interaction,
  **When** any data would be persisted,
  **Then** `data_handling.content_tokens` MUST contain only non-identifying tokens, and no personal data fields may be present.
