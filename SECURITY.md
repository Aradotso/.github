# Security Policy

We take security seriously at Ara. If you believe you've found a vulnerability in any Ara-owned repository, please follow the process below so we can address it responsibly.

## Supported Versions

We actively maintain and patch the latest stable release. Older versions do not receive security fixes.

| Version        | Supported |
| -------------- | --------- |
| Latest stable  | ✅ Yes    |
| Older releases | ❌ No     |

## Reporting a Vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.** Public disclosure before a fix is in place puts all users at risk.

Instead, send an email to **security@ara.so** with the following information:

- A clear description of the vulnerability
- Step-by-step instructions to reproduce it
- An assessment of the potential impact (who is affected and how)
- Any supporting material such as proof-of-concept code, screenshots, or logs

We will acknowledge your report within **48 hours** and share a resolution timeline within **5 business days**.

## Coordinated Disclosure

We follow a coordinated disclosure process. Once a fix is ready and deployed, we will:

1. Notify you before public disclosure
2. Credit you in the release notes or advisory (unless you prefer to remain anonymous)
3. Publish a security advisory through GitHub's Advisory Database

We ask that you give us reasonable time to investigate and remediate before sharing details publicly. We will work as quickly as possible to keep that window short.

## Our Security Practices

We maintain several controls to keep Ara's codebase and infrastructure secure:

- **Code review** is required for every pull request — no code ships without a second set of eyes.
- **Automated SAST** runs in CI on every push and pull request to catch common vulnerabilities early.
- **Secrets scanning** is enabled across all repositories to prevent accidental credential exposure.
- **Dependency vulnerability alerts** are active, and we triage and patch flagged dependencies promptly.

Thank you for helping keep Ara and its users safe. We genuinely appreciate responsible security research and will do our best to respond quickly and treat your report with the seriousness it deserves.
