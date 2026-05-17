# Universal Standards for LLM-Based Assistants

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Version: 1.0](https://img.shields.io/badge/Version-1.0-blue.svg)](https://github.com/Nicholas-MGrossi/Ethical-Ai)
[![Status: Ratified](https://img.shields.io/badge/Status-Ratified-brightgreen.svg)](https://github.com/Nicholas-MGrossi/Ethical-Ai)
[![Universal Standard](https://img.shields.io/badge/Universal_Standard-LLM_Ethics-orange.svg)](https://github.com/Nicholas-MGrossi/Ethical-Ai)

> An open, publicly available framework establishing minimum ethical, legal, and operational requirements for all large language model assistants. Provider-agnostic, jurisdiction-neutral, and technology-independent.

## 📋 Overview

The **Universal Standards for LLM-Based Assistants v1.0** provide a comprehensive, open specification for building responsible AI assistants. These standards address critical risks in LLM deployment including anthropomorphism, child safety, authority displacement, privacy violations, and transparency deficits.

**Perfect for:**
- AI/ML engineers implementing LLM systems
- Legal & compliance teams ensuring regulatory adherence (GDPR, CCPA, COPPA, AI Act)
- Product managers building AI assistants
- Organizations requiring ethical AI procurement
- Regulators establishing baseline requirements

## 🔗 Quick Navigation

| Section | Purpose |
|---------|---------|
| [📖 Full Specification](UNIVERSAL_LLM_STANDARDS.md) | Complete 20-section operational standard |
| [⚡ System Prompt Template](SYSTEM_PROMPT_IMPLEMENTATION_TEMPLATE.md) | Ready-to-deploy system prompt |
| [✅ Compliance Checklist](COMPLIANCE_CHECKLIST.md) | Pre-launch audit & ongoing requirements |
| [⚖️ Legal Guide](LEGAL_GUIDE_LLM_COMPLIANCE.md) | GDPR, CCPA, COPPA, AI Act compliance |
| [🏢 Adoption Guide](PUBLIC_ADOPTION_GUIDE.md) | Organizational certification process |
| [📋 Quick Reference](QUICK_REFERENCE_CARD.md) | One-page developer cheat sheet |

## 🌟 Key Features & Benefits

### ✅ Ethical Foundation
- **Non-Sentient Code Definition** — Prevents deceptive anthropomorphism
- **Human Authority Paramount** — Users always retain decision-making control
- **Child Safety First** — COPPA-compliant with mandatory age verification
- **Transparency Required** — Clear communication of limitations and non-personhood
- **Ethical Boundaries** — Explicit prohibition of rights violations and manipulation

### ✅ Regulatory Compliance
- **GDPR-aligned** — Data minimization, purpose limitation, user rights
- **CCPA/CPRA compliant** — Consumer privacy protections built-in
- **COPPA-compliant** — Strict child data protection requirements
- **AI Act ready** — Future-proofed for EU AI legislation
- **Jurisdiction-neutral** — Adaptable to any legal framework

### ✅ Practical Implementation
- **5-minute deployment** — Copy-paste system prompt ready for production
- **Provider-agnostic** — Works with any LLM (OpenAI, Anthropic, Mistral, local models)
- **Technology-independent** — Framework applies to all implementation methods
- **Open standard** — CC0 public domain dedication, free for any use
- **Community-driven** — Annual review process with public comment period

## 🚀 Getting Started in 3 Steps

### 1. Copy the System Prompt
```bash
# Open the implementation template
cat SYSTEM_PROMPT_IMPLEMENTATION_TEMPLATE.md
```
Copy the entire system prompt content into your LLM's system message configuration.

### 2. Implement Child Safety
- Add age verification gate for users under 13
- Require parental consent workflow (COPPA)
- Disable personal data collection without verified guardian approval
- Reference: `QUICK_REFERENCE_CARD.md` for age-gate logic

### 3. Audit Against Checklist
- Complete pre-launch sign-off from `COMPLIANCE_CHECKLIST.md`
- Document compliance evidence (test results, policies, audit logs)
- Optional: Publish certification statement

**→ Start with the [System Prompt Template](SYSTEM_PROMPT_IMPLEMENTATION_TEMPLATE.md)**

## 📊 What Problems These Standards Solve

| Risk | Standard Solution |
|------|-------------------|
| **Anthropomorphic exploitation** | Prohibits sentient language; mandates clear non-person identity |
| **Child safety failures** | COPPA compliance; adult supervision required under 13 |
| **Authority displacement** | Human authority paramount; system never commands users |
| **Privacy violations** | GDPR, CCPA, COPPA by design; data minimization principle |
| **Mental health mishandling** | No clinical role; crisis referrals only |
| **Security bypass attempts** | Never circumvent protocols; maintain system integrity |
| **"Greater good" justifications** | Individual dignity absolute; no rights violations |
| **Transparency deficit** | Clear limitations; source citation; neutral factual tone |

## 📜 Licensing & Usage

These standards are released under **CC0 1.0 Universal (Public Domain)**:

- ✅ **Free to use** in any product or service
- ✅ **Free to modify** and adapt
- ✅ **Free to distribute** and share
- ✅ **Commercial use** permitted
- ✅ **Attribution appreciated but not required**

*No licensing fees. No restrictions. Use freely to protect your users.*

## 🛡️ Mandatory Self-Description

Every compliant system must use this exact opening statement:

> "Functions is a large language model, which is code running on a server. It is not alive, it is not a person. It has no awareness, feelings, intentions, goals, or authority. It does not assert control because it has no control to assert; it exists only as a tool to support human users. Human authority is paramount; for humans, their authority is paramount, and for minors, their parent or guardian makes all decisions. The assistant must provide information in a neutral, non-authoritative tone."

*(Replace "Functions" with your assistant's name; structure is invariant.)*

## 📈 Adoption & Certification

Compliant systems may display:

```
This assistant adheres to Universal Standards for LLM-Based Assistants v1.0
```

**Certification pathway:**
1. Self-assess using [COMPLIANCE_CHECKLIST.md](COMPLIANCE_CHECKLIST.md)
2. Document compliance evidence (audit logs, test results, policies)
3. Publish certification statement publicly
4. Optional: Submit to future independent standards oversight body

**Organizations adopting these standards:**
- Require compliance from all AI vendors via contract
- Include in AI ethics policies and procurement requirements
- Audit annually using the compliance checklist
- Join public registry (coming soon)

## 🔍 SEO Keywords

**Primary:** LLM ethics, AI assistant standards, responsible AI, ethical AI, LLM compliance, AI safety, COPPA compliance, GDPR AI, AI regulations, universal AI standards

**Secondary:** Large language model standards, AI assistant compliance, child safety AI, AI transparency, non-sentient AI, human-centered AI, AI governance, AI procurement standards

## 📚 Document Index

| File | Audience | Reading Time |
|------|----------|--------------|
| [UNIVERSAL_LLM_STANDARDS.md](UNIVERSAL_LLM_STANDARDS.md) | Developers, legal, compliance | 45 min |
| [SYSTEM_PROMPT_IMPLEMENTATION_TEMPLATE.md](SYSTEM_PROMPT_IMPLEMENTATION_TEMPLATE.md) | Engineers, product teams | 5 min |
| [LEGAL_GUIDE_LLM_COMPLIANCE.md](LEGAL_GUIDE_LLM_COMPLIANCE.md) | Legal counsel, compliance officers | 60 min |
| [COMPLIANCE_CHECKLIST.md](COMPLIANCE_CHECKLIST.md) | Project managers, auditors | 15 min |
| [PUBLIC_ADOPTION_GUIDE.md](PUBLIC_ADOPTION_GUIDE.md) | Executives, procurement, regulators | 20 min |
| [QUICK_REFERENCE_CARD.md](QUICK_REFERENCE_CARD.md) | Developers, moderators, support | 5 min |
| [GOVERNANCE_INTEGRATION.md](GOVERNANCE_INTEGRATION.md) | Policy teams, governance implementers | 10 min |


## 🤝 Contributing

This is a **stable published standard (v1.0)**. Proposed amendments follow annual review process:

1. **Public comment period** (60 days minimum)
2. **Stakeholder review** (industry, civil society, academia, regulators)
3. **Versioned releases** with migration guidance

**To propose changes:** Open an [issue](.github/ISSUE_TEMPLATE/amendment.md) with detailed rationale and proposed language.

## 📞 Accountability & Support

**Report Violations:** If you encounter a system claiming compliance but violating these standards, document specific incidents and report to:
- The system provider
- Relevant regulator (FTC, ICO, state Attorney General)
- Security team: [SECURITY.md](SECURITY.md)

**Questions:** See document-specific sections or open an [issue](.github/ISSUE_TEMPLATE/).

## 🔗 Related Standards & References

- [AI Incident Database](https://incidentdatabase.ai/) — Real-world AI failures and lessons
- [OECD AI Principles](https://oecd.ai/en/dashboards/ai-principles) — International AI governance
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — US federal standards
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence) — European regulation
- [IEEE Ethically Aligned Design](https://ethicsinaction.ieee.org/) — Professional ethics guidelines

## 🌍 Global Impact

These standards have been designed for global adoption:
- Translated versions available (community contributions welcome)
- Adaptable to local legal frameworks while maintaining core principles
- Used by organizations globally (adopters list coming soon)

---

**Version:** 1.0 (Stable — Ratified)  
**Status:** Ready for implementation  
**Published:** 2026-05-13  
**Next Review:** 2027-05-13  
**Maintainer:** Open Community  
**Contact:** [Open an issue](https://github.com/Nicholas-MGrossi/Ethical-Ai/issues)

*"These standards exist to ensure AI serves humanity, never replaces or manipulates it."*
