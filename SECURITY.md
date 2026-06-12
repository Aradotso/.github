# Security Policy

## Reporting a Vulnerability

We take security seriously at Ara. If you discover a vulnerability, please report it responsibly so we can address it before public disclosure.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, email us at **security@ara.so** with:

- A clear description of the vulnerability and its potential impact
- Steps to reproduce or a proof-of-concept (if applicable)
- Any relevant environment details (OS, version, configuration)

We aim to acknowledge your report within **2 business days** and provide a resolution timeline within **7 business days**. We will keep you informed throughout the process and credit you in the fix (unless you prefer otherwise).

## Supported Versions

We release security patches for the versions listed below. If you are on an unsupported version, please upgrade to a supported release before reporting.

| Version | Supported |
|---------|-----------|
| Latest stable release | Yes |
| Previous major release | Yes (critical fixes only) |
| Older releases | No |

## Our Security Practices

We work continuously to keep Ara and its products secure:

- **Code review**: All code changes require peer review before merging into main.
- **Static analysis (SAST)**: Automated static analysis runs on every pull request to catch common vulnerability patterns early.
- **Secrets scanning**: We use automated secrets scanning in CI to prevent accidental credential leaks in source code and git history.
- **Dependency management**: Dependencies are audited regularly and updated to address known CVEs.
- **Least-privilege access**: Internal services and integrations follow least-privilege principles — components only receive the permissions they need.
- **Responsible disclosure**: We follow coordinated disclosure practices and aim to ship a fix before public details are shared.

## Scope

This policy covers all software and services developed and operated by Ara (ara.so), including the Ara desktop app, Ara web services, and published SDKs or libraries.

Third-party services integrated into Ara (e.g., LLM providers, cloud infrastructure) are outside our direct control. Vulnerabilities in those should be reported directly to the respective vendor.

## Thank You

We appreciate the security research community and responsible reporters who help keep Ara safe. Thank you for taking the time to disclose issues responsibly.
