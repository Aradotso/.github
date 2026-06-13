# Contributing to Ara

Ara is built by a small core team, product and engineering leads, and trusted contributors. This guide explains how contribution access works so people know who can make which calls and how responsibility grows over time.

## Team Roles and Maintainer Levels

### Contributors

Contributors are community members, customers, advisors, contractors, and teammates who open issues, propose improvements, submit pull requests, write docs, test releases, or share reproducible feedback.

Contributors can decide to:

- Open and comment on issues or discussions.
- Propose pull requests and documentation updates.
- Recommend labels, priorities, owners, and release notes.
- Ask for review from a lead when a change affects product behavior, security, billing, privacy, infrastructure, or Ara's public voice.

Contributors cannot close issues, merge pull requests, cut releases, change repository settings, approve security policy changes, or add/remove members unless that access has been explicitly granted at one of the levels below.

### Triage access

Triage access is for trusted contributors and team members who help keep Ara's repositories actionable. This level is usually granted by a founder, maintainer, or responsible lead after someone has shown good judgment in issues, support reports, docs, or review threads.

People with triage access can decide to:

- Apply and remove issue and pull-request labels.
- Link duplicates and related reports.
- Request missing reproduction details, logs, screenshots, or ownership context.
- Close issues that are duplicates, cannot be reproduced after a good-faith follow-up, are outside the repository scope, or have been resolved by a merged change.
- Reopen issues when new evidence shows the problem is still active.

Triage access does not include merging code, approving security-sensitive changes, cutting releases, managing members, changing branch protection, or making product commitments on behalf of Ara.

### Committer access

Committer access is for Ara engineers, product leads, design leads, and repeat contributors who can land changes safely in their area of ownership. It is granted by maintainers after a contributor has a track record of clear pull requests, review responsiveness, tests or validation notes, and respect for Ara's product and security boundaries.

People with committer access can decide to:

- Merge pull requests in areas they own or have been asked to steward.
- Approve low-risk docs, examples, tests, internal tooling, and product polish changes.
- Land urgent fixes when the risk is contained and a maintainer or responsible lead has been notified.
- Revert their own or team-approved changes when a regression is discovered.
- Close issues that are fixed by merged work.

Committers should merge only when the pull request has passed required checks, has a clear validation note, respects branch protection, and has review from the relevant owner when the change affects product behavior, customer data, billing, security, release automation, infrastructure, or company positioning. Committer access does not include cutting production releases, approving security policies, changing repository permissions, or adding/removing organization members.

### Maintainer access

Maintainer access is held by Ara's founders and the leads they delegate for specific repositories or systems. Maintainers are accountable for repository health, release safety, security posture, and membership decisions.

People with maintainer access can decide to:

- Cut, approve, or halt releases.
- Manage repository settings, branch protection, required checks, environments, and release automation.
- Add, remove, or change member access after confirming business need and least-privilege scope.
- Approve security policies, responsible disclosure language, vulnerability handling process, and private security fixes.
- Make final calls on cross-functional product, infrastructure, privacy, billing, brand, or customer-impacting tradeoffs.
- Delegate scoped ownership to leads and revoke access when responsibilities change.

Maintainers should consult the relevant founder or lead before decisions that materially affect customers, public commitments, data handling, costs, compliance posture, or Ara's company direction.

## Escalation Path

Access grows through demonstrated judgment, not tenure alone.

1. Contributor to triage: a contributor consistently files useful reports, helps reproduce issues, improves docs, or reviews discussions with good context. A maintainer or lead may grant triage access for a specific repository.
2. Triage to committer: a triage member repeatedly identifies the right owner, prepares high-quality changes, responds well to review, and understands the product or system boundary they want to own. Maintainers may grant committer access scoped to that repository or area.
3. Committer to maintainer: a committer reliably protects release quality, handles incidents calmly, reviews others well, understands security and privacy tradeoffs, and is trusted by Ara's founders or delegated leads. Founders or existing maintainers approve the promotion and document the scope.
4. Scope changes: access can be narrowed, paused, or removed when someone changes roles, leaves a project, is inactive for an extended period, or no longer needs the permission.

When in doubt, escalate upward: contributors ask triage members or committers; triage members ask committers or leads; committers ask maintainers; maintainers ask Ara's founders for company-level, security-sensitive, or customer-impacting decisions.

## Decision Guide

- Issue hygiene: triage members can label, deduplicate, request context, close stale or fixed issues, and reopen issues with new evidence.
- Pull requests: committers can merge scoped, reviewed, passing changes; maintainers resolve disputed, high-risk, cross-team, or release-blocking pull requests.
- Releases: maintainers approve release timing, release notes, rollout plans, rollback decisions, and production release automation.
- Security and privacy: maintainers approve security policy changes, private vulnerability handling, member access to sensitive systems, and disclosure decisions.
- Product commitments: founders and delegated leads make final calls on customer-facing commitments, roadmap promises, pricing, billing, and company positioning.
- Membership and permissions: maintainers manage repository access using least privilege and remove access when it is no longer needed.

Ara's default operating mode is to trust contributors, keep decisions close to the people doing the work, and escalate quickly when a decision affects customers, security, privacy, releases, or company direction.
