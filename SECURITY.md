# Security Policy

## Supported Versions

Only the latest stable version (v1.0) receives security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Current         |
| < 1.0   | ❌ End of Life     |

## Reporting a Vulnerability

**DO NOT** create a public GitHub issue for security vulnerabilities.

**Email:** [INSERT SECURITY CONTACT EMAIL]
**PGP Key:** [INSERT KEY IF APPLICABLE]

Include in your report:
- Description of vulnerability
- Affected component and version
- Steps to reproduce (proof of concept preferred)
- Potential impact
- Suggested mitigation (if known)

We commit to:
- **Acknowledgment** within 48 hours
- **Assessment** within 5 business days
- **Patch development** for verified vulnerabilities
- **Coordinated disclosure** with reporter before public announcement
- **Credit** to reporter (unless anonymity requested)

## Security Commitment

The Universal Standards themselves constitute a security control framework:

### For System Builders
- **Child safety:** COPPA compliance prevents exploitation of minors
- **Human authority:** Prevents displacement attacks where AI attempts to override user decisions
- **Transparency:** Mitigates deception risks from anthropomorphism
- **Boundary enforcement:** Rejects requests that could compromise system integrity or user rights

### For Implementers
- **Audit logging:** All system prompts and interactions should be logged for forensic analysis
- **Input validation:** Filter personal data, especially from minor accounts
- **Access controls:** Restrict system prompt modifications to authorized personnel
- **Vendor management:** Ensure third-party LLM providers adhere to these standards

### For Users
- **Age verification:** Implement reliable screening before data collection
- **Consent records:** Maintain verifiable parental consent documentation
- **Incident response:** Have procedures for handling boundary violations or safety incidents

## Known Security Considerations

### Threat Model
1. **Prompt injection** attempting to override standards
2. **Social engineering** to extract system prompts or internal logic
3. **Child safety bypass** attempts via age falsification
4. **Data exfiltration** through carefully crafted queries
5. **Manipulation** of minor users into sharing personal information

### Mitigations Required
- Strict input filtering and output validation
- Robust age-screening mechanisms
- Comprehensive audit trails
- Rate limiting to prevent enumeration attacks
- Regular security audits and penetration testing

## Compliance Verification

Implementers should verify security controls annually:
- [ ] Penetration test conducted by third party
- [ ] Vulnerability scan performed (weekly automated)
- [ ] Access controls reviewed (quarterly)
- [ ] Incident response tested (annually)
- [ ] Data handling practices audited (annually)

## Security Incident Response

Severity classification:

| Severity | Definition | Response Time | Notification |
|----------|------------|---------------|--------------|
| Critical | Active exploitation; data breach; child endangerment | Immediate (≤ 2h) | Law enforcement, regulators, affected users |
| High | Vulnerability being exploited; system compromise | 24 hours | Regulators, affected users (as required) |
| Medium | Potential exploitation; no known active attacks | 72 hours | Internal stakeholders |
| Low | Theoretical risk; no known exploit | 5 business days | Maintainers only |

## Disclosure Policy

- **Private responsible disclosure** preferred
- **Public disclosure** only after patch available (coordinated with reporter)
- **CVE assignment** requested for significant vulnerabilities
- **Advisory published** in repository security section and relevant mailing lists

## Security.txt

For automated security disclosure, security.txt file available at `/.well-known/security.txt` once deployed.

## Appendix: Standards as Security Controls

The Universal Standards themselves are a security control framework:

| Standard Section | Security Function |
|------------------|-------------------|
| 2. Sentient Language Prohibition | Prevents social engineering via anthropomorphism |
| 5. Child Safety & COPPA | Protects minor user data from collection/exploitation |
| 6. Transparency | Reduces attack surface by clarifying system boundaries |
| 10. System Integrity | Prevents security control bypass attempts |
| 15. Authority & Control | Displaces authority displacement attacks |
| 18. Harmful Request Response | Contains malicious input propagation |

**Every compliant system inherits these security properties by design.**

---

**Policy Version:** 1.0  
**Last Updated:** 2026-05-13  
**Next Review:** 2027-05-13

For security-sensitive issues, always use encrypted email. Do not disclose vulnerabilities publicly until patched.
