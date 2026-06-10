# Security Policy

## Reporting a Vulnerability

Please **do not** file a public GitHub issue for security vulnerabilities.

Report security issues through one of the following channels:

- **Email:** security@ara.so — include a clear description of the issue, reproduction steps, and any relevant proof-of-concept.
- **GitHub Security Advisories:** Use the [Report a vulnerability](https://github.com/Aradotso/.github/security/advisories/new) form on this repository.

We treat all reports confidentially. Your name will only appear in acknowledgements if you explicitly consent.

## Response SLA

| Stage | Target |
|---|---|
| Initial acknowledgement | 2 business days |
| Triage & severity assessment | 5 business days |
| Status update (fix timeline or decision) | 10 business days |
| Critical/High severity patch release | 14 days from confirmation |

## Scope

The following assets are **in-scope**:

- **ara.so** — marketing and authentication surfaces
- **chat.ara.so** — the Ara web chat application
- **api.ara.so** — the Ara backend API (Railway-hosted)
- **AraDesktop** — the macOS native application (published via the App Store and direct download)
- Any subdomain under `ara.so` that handles user data or authentication

**Out of scope:**

- Third-party services we integrate with (Supabase, Stripe, Vercel, etc.) — report those directly to the relevant vendor
- Social-engineering attacks against Ara employees
- Denial-of-service attacks
- Issues already known and tracked internally (we will indicate this in our response)

## Bug Bounty

We do not currently operate a formal paid bug bounty programme. For significant, responsibly disclosed vulnerabilities we may offer swag, recognition, or discretionary compensation at our sole discretion. We will communicate this during triage.

## Supported Versions

We only apply security patches to the **latest released version** of AraDesktop and the current production deployment of ara.so / chat.ara.so. Older versions are not supported.

## Disclosure Policy

We follow coordinated disclosure. We ask that you give us a reasonable time to fix the issue (aligned with the SLA above) before public disclosure. We will work with you to agree on a disclosure timeline and will credit you in the release notes.
