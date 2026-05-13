# Contributing to Universal Standards v1.0

Thank you for your interest in contributing to the Universal Standards for LLM-Based Assistants.

## Important: Stability Notice

**Version 1.0 is ratified and stable.** No substantive changes to the standard's requirements are currently accepted. This ensures implementers have a fixed specification to comply with.

### What We Accept

1. **Non-normative improvements** to documentation clarity, examples, or formatting
2. **Translations** into other languages (with ISO language codes)
3. **Implementation guides** for specific platforms/frameworks (as separate documents)
4. **Case studies** demonstrating compliance (in the `/cases` directory)
5. **Bug reports** in published materials (typos, broken links, formatting errors)
6. **Infrastructure improvements** (website, publishing, CI/CD)

### What We Do NOT Accept

- Changes to the core standard text (sections 1–19)
- Additions or deletions of mandatory requirements
- Modifications to the Universal Definition
- Alterations to the child safety or human authority provisions
- Changes to prohibited behaviors or permitted language lists

## Amendment Process (Future Versions)

Substantive amendments follow an annual cycle:

### Step 1: Issue Discussion (Days 1–60)
1. Open an issue with clearly labeled "Amendment Proposal — [topic]"
2. Provide detailed rationale citing:
   - Implementation challenges
   - Legal/regulatory changes
   - Research findings
   - Harm mitigation needs
3. Engage community discussion (minimum 60-day comment period)
4. Maintain summary of arguments for and against

### Step 2: Drafting (Days 61–90)
1. Propose exact wording changes
2. Provide migration guidance for existing implementations
3. Conduct impact assessment (legal, technical, operational)
4. Draft press release and FAQ materials

### Step 3: Stakeholder Review (Days 91–120)
1. Circulate to identified stakeholder groups:
   - Industry associations
   - Civil society organizations
   - Academic researchers
   - Regulatory bodies
2. Collect written feedback
3. Revise based on substantive, good-faith concerns

### Step 4: Ratification (Days 121–150)
1. Maintainers vote (consensus preferred; 2/3 majority required)
2. Publish final text with change log
3. Announce via project channels
4. Update certification requirements

### Step 5: Implementation Window (1 year)
- Previous version remains certifiable for 12 months
- Both versions supported during transition
- Migration guides and tooling updates provided

## Translation Policy

Translations are welcome and encouraged. Requirements:
- Use professional translation or fluent bilingual contributor
- Include ISO 639-1 language code in filename (e.g., `UNIVERSAL_LLM_STANDARDS.es.md`)
- Add translator attribution page with credentials
- State clearly: "This is an unofficial translation; the authoritative version is the English original"
- Link back to source repository
- Notify maintainers for inclusion in official list

## Submitting Changes

### Documentation Fixes (Typos, Formatting)
```bash
git checkout -b fix/typo-section-5
# Make changes
git commit -m "Fix typo in section 5.2; clarify COPPA definition"
git push origin fix/typo-section-5
# Open PR
```

### New Implementation Guides
Place in `/docs/implementations/[framework-name]/` with:
- Framework overview
- Step-by-step integration
- Platform-specific code samples
- Compliance validation steps

### Case Studies
Place in `/cases/[organization-name]/` with:
- Organization description
- Implementation approach
- Challenges faced and solutions
- Audit results or compliance verification
- Lessons learned (failure modes included)

## Pull Request Process

1. **Fork** the repository
2. **Create feature branch** (`git checkout -b feature/your-feature`)
3. **Commit** changes (`git commit -am 'Add meaningful message'`)
4. **Push** to branch (`git push origin feature/your-feature`)
5. **Open Pull Request** with:
   - Clear description of changes
   - Link to related issue (if applicable)
   - Note on testing or validation performed
   - For translations: certification of accuracy

**Pull Request Review:**
- Automated checks (linting, link validation) must pass
- Maintainer review within 7 days
- Community feedback period (5 business days minimum)
- Merge by maintainer with commit message following [Conventional Commits](https://www.conventionalcommits.org/)

## Reporting Security Issues

**DO NOT** open public issues for vulnerabilities. Email: [INSERT SECURITY EMAIL]

Include:
- Affected component/version
- Detailed reproduction steps
- Potential impact description
- Suggested fix (if known)

We respond to security reports within 48 hours and follow coordinated disclosure.

## Recognition

Contributors are acknowledged in:
- `/ACKNOWLEDGMENTS.md` (documentation improvements)
- Release notes (substantive contributions)
- Project website (maintainers and translators)

## Questions

Open an issue with "Question:" prefix. For sensitive matters, email maintainers.

---

**Thank you** for helping ensure AI systems remain safe, transparent, and accountable.

*"The standard is not the ceiling; it is the floor."*
