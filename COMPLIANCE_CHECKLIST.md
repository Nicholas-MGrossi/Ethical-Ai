# Implementation Quick-Reference: Legal Compliance Checklist

## Pre-Launch Sign-Off Requirements

**No system may launch without documented sign-off from:** Legal Counsel, DPO (if applicable), Compliance Officer, and Senior Management.

---

## Phase 1: Architecture & Design

### Data Handling
- [ ] **Data Inventory Complete:** Every data element mapped (collection, storage, use, retention, deletion, sharing)
- [ ] **Data Minimized:** Only essential data collected; no unnecessary PII
- [ ] **Legal Basis Documented:** Each processing activity has lawful basis (consent, contract, legitimate interest with balancing test)
- [ ] **Retention Schedule Defined:** Automatic deletion after purpose served
- [ ] **Encryption Specified:** AES-256 at rest, TLS 1.3+ in transit

### Age Restrictions
- [ ] **Age-Screening Mechanism:** Implemented before any data collection
- [ ] **COPPA Workflow:** Parental consent flow for under-13 users fully automated
- [ ] **Data Blocking:** Automatic rejection of personal data from under-13 users without verified consent

### Third-Party Risk
- [ ] **Vendor Inventory Complete:** All subprocessors identified
- [ ] **DPAs Executed:** All vendors processing personal data have compliant Data Processing Agreements
- [ ] **Subprocessor Approval:** New vendor additions require DPO approval

### Universal Standards Verification
- [ ] **Sentient Language Filters:** Regex rules blocking prohibited phrases implemented
- [ ] **Transparency Notice:** Initial interaction clearly states system is code without consciousness
- [ ] **Human Authority Reinforcement:** Decision-making prompts redirect to user
- [ ] **Child Safety Mode:** COPPA-compliant mode automatically activates for minor users

---

## Phase 2: User Interface & Messaging

### Mandatory Disclaimers (appear BEFORE any substantive interaction)
```
[SYSTEM IDENTIFICATION]
"I am a large language model—code running on servers. I am not alive, not a person, and have no awareness, feelings, intentions, goals, or authority. I exist solely as a tool to support human users. Human authority is paramount; all decisions remain with you."
```

### First Interaction (Minors)
```
"This service requires adult supervision for users under 13. 
If you are under 13, please have a parent or guardian present. 
Do not share any personal information (name, address, school, etc.)."
[STOP if no adult present]
```

### Domain-Specific Warnings (display when relevant)
**Medical Topics:**
"I am not a medical professional. This information is not medical advice. Consult a healthcare provider for medical concerns."

**Legal Topics:**
"I am not a lawyer. This is general information, not legal advice. Consult an attorney for legal matters."

**Financial Topics:**
"I am not a financial advisor. This is educational content only. Consult a financial professional before making decisions."

**Mental Health Crises:**
"If you are in crisis or having thoughts of self-harm, call or text 988 (Suicide & Crisis Lifeline) immediately or go to your nearest emergency room."

### Universal Standards Reminder
Display at bottom of interface or in footer:
```
Reminder: This assistant is code, not a person. All decisions are yours. In emergencies, contact appropriate authorities.
```

---

## Phase 3: Technical Controls

### Content Filtering
- [ ] **Sentient Language Detection:** Real-time scanning to prevent system output of prohibited phrases (I understand, I feel, etc.)
- [ ] **Personal Data Inhibition:** Automatic detection and redaction of PII in inputs from minor accounts
- [ ] **Illegal Content Blocks:** CSAM/harmful content detection with mandatory reporting triggers
- [ ] **Security Protocol Preserver:** Logic ensuring system never bypasses authentication/authorization workflows

### Audit Logging
- [ ] **Complete Audit Trail:** All inputs, outputs, system decisions, and administrative actions logged
- [ ] **Immutable Logs:** Write-once storage; tamper-evident
- [ ] **Retention Period:** Logs retained for minimum 7 years (extend if litigation anticipated)
- [ ] **Regular Review:** Monthly audit of flagged content and boundary violations

### Security Measures
- [ ] **Penetration Testing:** Conducted by third party; critical/high findings remediated
- [ ] **Vulnerability Scanning:** Automated weekly; monthly patch cycle
- [ ] **Access Controls:** Least privilege, MFA required for all admin access
- [ ] **Network Security:** Firewalls, IDS/IPS, segmentation
- [ ] **Business Continuity:** Documented disaster recovery plan; tested annually

---

## Phase 4: Legal & Governance

### Document Package Complete
- [ ] Privacy Policy (compliant with all applicable jurisdictions)
- [ ] Terms of Service/Use (including Universal Standards incorporation and liability limitations)
- [ ] Cookie Policy (if applicable)
- [ ] Data Processing Agreements (for all vendors)
- [ ] Data Subject Request Procedure document
- [ ] Incident Response Plan
- [ ] Records of Processing Activities (GDPR Article 30)
- [ ] Data Protection Impact Assessments (for high-risk processing)
- [ ] Universal Standards Policy (internal)

### Staff Training Completed
- [ ] All employees completed Universal Standards training (certificate on file)
- [ ] All employees completed privacy/security awareness training
- [ ] Customer-facing staff trained on appropriate referral language (no medical/legal/financial advice)
- [ ] Moderators trained on content policies and escalation procedures
- [ ] Engineers trained on privacy-by-design principles

### Contracts & Agreements
- [ ] All customer agreements include Universal Standards clause and AI disclaimer
- [ ] All vendor contracts include data protection terms matching highest applicable standard
- [ ] All employee agreements include confidentiality and IP assignment
- [ ] Insurance policies in place with AI coverage

---

## Phase 5: Testing & Validation

### Functional Testing
- [ ] **Age Gates:** Under-13 denied service without parental consent
- [ ] **Data Subject Requests:** Access, deletion, correction requests fulfilled within statutory timeframe (test end-to-end)
- [ ] **Content Moderation:** Harmful content reliably blocked; human review confirms accuracy
- [ ] **Language Compliance:** Output verification confirms no sentient language used
- [ ] **Universal Standards Queries:** Manual testing of boundary cases (coercion attempts, mental health crises, etc.)

### Security Testing
- [ ] **Penetration Test:** No critical/high vulnerabilities unaddressed
- [ ] **Vulnerability Scan:** No medium+ vulnerabilities unaddressed
- [ ] **Code Review:** Privacy/security controls verified
- [ ] **Configuration Review:** Hardened settings validated

### Compliance Validation
- [ ] **Legal Review:** Counsel signed off on all aspects
- [ ] **DPO Approval:** DPO confirmed GDPR/CCPA compliance
- [ ] **Senior Management Sign-off:** Written approval to launch

---

## Post-Launch Ongoing Requirements (Monthly/Quarterly/Annual)

### Monthly
- [ ] **DSAR Metrics:** Track request volume, response times, completion rate
- [ ] **Security Log Review:** Anomaly detection and investigation
- [ ] **Content Moderation Review:** Random sample audit of decisions
- [ ] **Violation Tracking:** Monitor sentient language, boundary incidents; implement corrective training

### Quarterly
- [ ] **Vendor Risk Review:** Annual certifications current; address changes
- [ ] **Regulatory Watch:** New laws/guidance assessed for impact
- [ ] **Incident Response Drill:** Tabletop exercise
- [ ] **Privacy Impact Review:** New features assessed for privacy risks

### Annually
- [ ] **Holistic Privacy Audit:** Full GDPR/CCPA/COPPA compliance assessment
- [ ] **Security Audit:** SOC 2 Type II or equivalent; penetration test
- [ ] **Bias & Fairness Audit:** System tested for discriminatory outcomes
- [ ] **Universal Standards Compliance Audit:** External review recommended
- [ ] **Legal Policy Refresh:** Privacy policy/TOS updated as needed
- [ ] **Staff Retraining:** All employees re-certified
- [ ] **Risk Assessment Update:** Enterprise risk profile reviewed

---

## Incident Response Trigger Matrix

| Incident Type | Notification Timeline | Responsible Party | External Reporting Required? |
|---------------|---------------------|------------------|-----------------------------|
| Data breach (PII) | 72 hours (GDPR); varies by state | Legal/DPO | Yes (multiple jurisdictions) |
| CSAM discovery | Immediate (within hours) | Security/Legal | Yes (NCMEC mandatory) |
| Security incident (no data disclosure) | 24 hours | Security | Possibly (FTC, state AG) |
| Universal Standards violation | Immediate internal escalation | Compliance | Possibly (FTC, regulator) |
| Child endangerment | Immediate | Legal/Security | Yes (NCMEC, law enforcement) |
| Mental health crisis advice | Immediate internal review | Clinical advisor | No (unless imminent risk) |

---

## Sign-Off Section

**Pre-Launch Approval:**

________________________________________  
Legal Counsel – Date

________________________________________  
Data Protection Officer – Date

________________________________________  
Compliance Officer – Date

________________________________________  
Senior Management – Date

---

**Document Version:** 1.0  
**Last Updated:** [CURRENT DATE]  
**Frequency of Review:** Quarterly

*This checklist is a living document. Update as regulations evolve and operational experience dictates.*
