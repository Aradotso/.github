# Security Policy

## Contact

If you find a security issue in this repository, email founders@ara.so. Please include enough detail for us to reproduce and understand the impact, such as affected files, steps to reproduce, proof-of-concept details, and any relevant screenshots or logs.

## Scope

This policy applies only to Ara's GitHub organization profile repository (`Aradotso/.github`) and the public-facing organization profile content it publishes on GitHub.

This repository does not contain the Ara application, production services, customer data systems, infrastructure, or private source code. Reports about Ara's app, APIs, browser/runtime behavior, production infrastructure, or customer-facing services should be submitted through Ara's primary security-reporting channel instead of this repository when that channel is available.

## Bug bounty and escalation

If Ara has an active formal bug bounty or HackerOne program for the affected asset, please use that program for eligible reports, especially for serious issues that may affect Ara products or production systems. Ara's likely HackerOne program is at https://hackerone.com/ara; if that page is unavailable or does not list the affected asset, email founders@ara.so.

For issues limited to this GitHub organization profile repository, founders@ara.so is the canonical contact.

## Responsible disclosure timeline

We ask researchers to give Ara a reasonable opportunity to investigate and fix confirmed security issues before public disclosure.

Our default timeline is:

- We aim to acknowledge reports within 7 days.
- We aim to provide an initial assessment or request for more information within 14 days.
- We aim to remediate confirmed issues within 90 days when a fix is required.
- If a fix cannot reasonably be completed within 90 days, we will try to agree on a revised disclosure timeline with the reporter.
- Please do not publicly disclose details before the timeline expires or before Ara confirms the issue is resolved.

## Out of scope

The following are out of scope for this repository's security policy:

- Social engineering, phishing, or physical attacks against Ara employees, contractors, users, partners, or vendors.
- Denial-of-service or resource-exhaustion testing, including DDoS attempts.
- Spam, content injection, or reputation-abuse reports that do not demonstrate a security impact in this repository.
- Reports about missing security headers, cookies, or runtime configuration for ara.so, app.ara.so, APIs, or other Ara-owned services unless they are submitted through Ara's main security-reporting channel and apply to an in-scope asset there.
- Vulnerabilities in GitHub, third-party platforms, browsers, package registries, or other vendors unless they directly create an exploitable issue in this repository's content.
- Automated scanner output without a clear, reproducible security impact.
- Public information disclosure that is already intentionally published in this repository or on Ara's public GitHub profile.

## Researcher expectations

Please act in good faith, avoid accessing or modifying data that is not your own, avoid service disruption, and stop testing once you have enough evidence to report the issue. We will not pursue legal action against researchers who follow this policy and make a good-faith effort to avoid privacy violations, data destruction, and service disruption.
