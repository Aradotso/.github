# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Ara or any Aradotso-maintained project, please report it responsibly. **Do not open a public GitHub issue.**

Send a detailed report to: **security@ara.so**

Include as much of the following as possible:

- A description of the vulnerability and its potential impact
- The affected repository, component, or version
- Steps to reproduce or a proof-of-concept (even partial is helpful)
- Any suggested mitigations you have in mind

We aim to acknowledge receipt within **2 business days** and will keep you informed as we investigate and resolve the issue. We ask that you give us a reasonable window — typically **90 days** — to address the vulnerability before any public disclosure.

We do not currently operate a formal bug bounty program, but we genuinely appreciate responsible disclosure and will acknowledge contributors in our release notes when a fix ships (unless you prefer to remain anonymous).

## Supported Versions

We actively backport security patches to the latest stable release. Older versions may not receive security updates. If you are using an older release, we recommend upgrading to the latest version.

| Version       | Supported          |
|---------------|--------------------|
| Latest stable | ✅ Yes             |
| Older releases| ❌ No guarantee    |

## Our Security Practices

We take security seriously across our development lifecycle:

**Code Review** — all changes to main branches require peer review before merging. Sensitive areas (auth, payments, secrets handling) receive additional scrutiny.

**Static Analysis (SAST)** — we use automated static analysis tools in CI to catch common vulnerability classes before code ships.

**Secrets Scanning** — secret detection is enabled on all repositories to prevent accidental credential commits. We use Infisical for centralized secrets management and do not store sensitive values in source code.

**Dependency Auditing** — we regularly audit third-party dependencies for known CVEs and update them promptly when vulnerabilities are disclosed upstream.

**Principle of Least Privilege** — services and integrations are granted only the permissions they need. API keys and tokens are scoped narrowly and rotated periodically.

**Incident Response** — in the event of a confirmed vulnerability, we prioritize a fix, notify affected users as appropriate, and publish a post-mortem for significant incidents.

## Contact

For non-security issues (bugs, feature requests), please use GitHub Issues in the relevant repository.

For security matters: **security@ara.so**
