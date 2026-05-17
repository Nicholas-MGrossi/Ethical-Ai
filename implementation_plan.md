# Implementation Plan

[Overview]
Resolve all outstanding documentation issues—placeholder text substitution, broken cross-references, and repository hygiene—to bring every file to publishable quality with zero TODOs, zero placeholders, and fully validated internal references.

This plan addresses 15 concrete defects found during automated audit across 5 files, plus one cross-reference mismatch between TECHNICAL_ETHICAL_ARCHITECTURE.md and its actual section structure. All fixes are localized, minimal, and require no structural changes. The scope is limited to markdown documentation files; no JSON schemas, code, or configuration files require modification. The repository is a documentation-first ethical AI standards repository; all files are written in Markdown with JSON Schema supplementary files.

[Types]
No type system changes required; this is a documentation-only fix pass.

The only "type" is string substitution in markdown files and section anchor correction.

[Files]

Detailed breakdown of all file modifications:

**New files to create:**
- None required.

**Existing files to modify:**

1. **GITHUB_PUBLISHING.md** — Replace 5 instances of `YOUR_USERNAME` with the actual GitHub username `Nicholas-MGrossi`:
   - Line 15: `YOUR_USERNAME/universal-llm-standards.git` → `Nicholas-MGrossi/universal-llm-standards.git`
   - Line 32: same pattern
   - Line 79: same pattern (verify line number exact match)
   - Line 80: same pattern (verify line number exact match)
   - Line 83: same pattern (verify line number exact match)

2. **PUBLISHING_INSTRUCTIONS.md** — Replace 7 instances of `YOUR_USERNAME` with `Nicholas-MGrossi`:
   - Lines 30, 35, 55, 60, 71, 153 (verify exact lines)

3. **LEGAL_GUIDE_LLM_COMPLIANCE.md** — Replace `[INSERT DATE]` placeholders:
- Line 938: (date) placeholder → `2026-05-16` (document version effective date)
- Line 940: (date) placeholder → `2027-05-16` (next review date)

4. **PUBLIC_ADOPTION_GUIDE.md** — Replace TBD placeholder:
   - Line 192: TBD placeholder → actual GitHub Issues link

5. **QUICK_REFERENCE_CARD.md** — Replace repository URL placeholder:
   - Line 188: `[repository URL]` → `[Nicholas-MGrossi/Ethical-Ai](https://github.com/Nicholas-MGrossi/Ethical-Ai)`

6. **TECHNICAL_ETHICAL_ARCHITECTURE.md** — Fix cross-reference to non-existent section:
   - Line ~870: Reference to `§6.1.1` does not exist. The document has sections numbered sequentially (6.1, 6.2, 6.3) but no 6.1.1. Change to plain text description or add a §6.1.1 anchor heading.

**Files to delete:**
- None required.

[Functions]
No function modifications required; this is a documentation-only repository.

[Classes]
No class modifications required.

[Dependencies]
No dependency changes required.

[Testing]
Run both audit scripts after all fixes to confirm zero issues remain:
- `python scripts/validate_repo.py` — JSON schema, enum drift, link integrity
- `python scripts/audit_repo.py` — Placeholder text, cross-references, file anomalies

[Implementation Order]
Execute fixes in dependency order: placeholder substitutions first (GITHUB_PUBLISHING.md, PUBLISHING_INSTRUCTIONS.md, LEGAL_GUIDE_LLM_COMPLIANCE.md, PUBLIC_ADOPTION_GUIDE.md, QUICK_REFERENCE_CARD.md), then cross-reference correction (TECHNICAL_ETHICAL_ARCHITECTURE.md), then re-run both validation scripts.