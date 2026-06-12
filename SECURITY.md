# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Ara, please report it responsibly by emailing **security@ara.so**. Do not open a public GitHub issue for security-related matters.

Please include as much detail as possible:

- A description of the vulnerability and its potential impact
- Steps to reproduce or a proof-of-concept (if available)
- Any relevant environment details (OS, version, configuration)

## Response SLA

We take security seriously and will respond promptly:

| Stage | Target |
|---|---|
| Initial acknowledgement | Within 2 business days |
| Triage and severity assessment | Within 5 business days |
| Status update | Every 7 days until resolved |
| Patch or mitigation | Based on severity (see below) |

**Severity-based patch targets:**

- Critical: 7 days
- High: 14 days
- Medium: 30 days
- Low: 90 days

## Disclosure Timeline

We follow a coordinated disclosure process:

1. Reporter submits vulnerability to security@ara.so.
2. Ara acknowledges receipt within 2 business days.
3. Ara investigates and develops a fix.
4. Ara notifies the reporter when a fix is ready, shares a draft advisory, and requests the reporter's review.
5. Fix is released and a public security advisory is published (typically 30–90 days after initial report, depending on severity and complexity).
6. The reporter is credited (unless they prefer to remain anonymous).

We ask reporters to give us a reasonable window to resolve the issue before any public disclosure.

## Responsible Disclosure Pledge

We commit to:

- Acknowledging your report promptly and keeping you informed throughout the process
- Working with you collaboratively and in good faith to understand and resolve the issue
- Not pursuing legal action against researchers who follow this policy
- Crediting you for your discovery in the public advisory (if desired)
- Never disclosing your personal information without your explicit consent

In return, we ask that you:

- Give us a reasonable time to investigate and fix the issue before disclosing publicly
- Avoid accessing, modifying, or deleting user data beyond what is necessary to demonstrate the vulnerability
- Do not disrupt Ara services or degrade the experience for other users

## Scope

This policy applies to all Ara products and services, including ara.so and associated APIs.

Out of scope: third-party services and dependencies (please report those to their respective maintainers).

---

Thank you for helping keep Ara and its users safe.
