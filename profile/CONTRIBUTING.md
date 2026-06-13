# Contributing to Ara

Ara is built by founders, delegated leads, and trusted contributors working across product, infrastructure, agent runtime, design, and customer-facing systems. This guide explains how contribution access grows with demonstrated judgment while keeping production, security, and member-management decisions tightly scoped.

## Team Roles and Maintainer Levels

Ara uses least-privilege access. Access is granted for the repositories, systems, or product areas where someone is actively responsible, and it can be narrowed or removed when that responsibility changes.

### Contributors

Contributors propose issues, improvements, documentation updates, designs, tests, and pull requests. Contributors do not need repository write access to participate.

Contributors can make decisions about:

- Whether to open an issue, discussion, or draft pull request.
- How to explain the user problem, reproduction steps, proposed behavior, or tradeoff they are seeing.
- Whether a small documentation or test improvement is ready to request review.

Contributors should not make final calls on product commitments, release timing, security policy, repository permissions, or merges unless a committer or maintainer has explicitly delegated that decision for a scoped task.

### Triage access

Triage access is for trusted contributors, support owners, and area leads who keep GitHub issues and discussions actionable. Triage access does not include merging code or changing repository settings.

People with triage access can:

- Apply labels, milestones, projects, and ownership markers.
- Ask for reproduction details, logs, screenshots, product context, or acceptance criteria.
- Mark duplicates, link related issues, and summarize the current state of an issue.
- Close issues that are duplicates, out of scope, stale after requested information is not provided, or already resolved.
- Reopen issues when new evidence changes the decision.

Triage owners can make decisions about issue hygiene, routing, priority signals, and whether an issue is ready for engineering or product review. They should escalate anything involving security, privacy, production incidents, roadmap commitments, legal concerns, or member access to a maintainer.

### Committer access

Committer access is for delegated leads and trusted contributors who have repeatedly shipped correct, reviewable work in a specific repo or product area. Committer access is scoped: a committer for one surface is not automatically a committer everywhere.

Committers can merge pull requests when all of the following are true:

- The pull request is within their owned or delegated area.
- Required checks pass, or a maintainer has approved a documented exception.
- The change has the required review for its risk level.
- The pull request description, tests, rollout notes, and follow-up issues are sufficient for the change.
- The change does not alter security policy, production secrets, billing behavior, member permissions, release authority, or company-level commitments without maintainer approval.

Committers can make decisions about implementation approach, test coverage, low-risk refactors, documentation updates, bug fixes, dependency updates, and scoped product behavior. They can also revert their own or clearly broken changes when reverting is the safest path, then notify the relevant lead or maintainer.

### Maintainer access

Maintainer access is for Ara founders and delegated senior leads who are accountable for repository health, release safety, security posture, and team access. Maintainers are expected to use this access conservatively and document decisions that affect other teams.

Maintainers can:

- Cut releases, approve release candidates, and coordinate rollbacks.
- Manage repository settings, branch protection, required checks, environments, and automation rules.
- Add, remove, or scope organization members, outside collaborators, teams, and repository permissions.
- Approve security policies, vulnerability handling, private forks, embargoed fixes, and disclosure language.
- Make final calls on cross-functional product, infrastructure, privacy, or operational tradeoffs.
- Delegate triage or committer access to trusted contributors for a defined area.

Founders hold final authority for company-level, security-sensitive, legal, privacy, billing, and irreversible production decisions. Delegated maintainers and leads own day-to-day decisions inside their areas and escalate when a decision crosses team, customer, security, or release boundaries.

## Escalation Path

Access grows from contribution history and judgment, not tenure alone.

1. Contributor: starts by opening useful issues, submitting focused pull requests, reviewing docs or tests, and showing clear communication.
2. Triage: granted when a contributor reliably understands Ara's priorities, routes issues well, and knows when to ask for help.
3. Committer: granted when a triage owner or contributor repeatedly ships safe changes, reviews others well, and can own merge decisions in a scoped area.
4. Maintainer: granted when a committer or lead demonstrates sustained ownership of a repository, product area, release path, or security-sensitive system.

Promotion can be proposed by a maintainer, founder, or delegated lead. The proposal should name the scope of access, the evidence for the change, the decisions the person is expected to make, and the maintainer who will help them ramp. If the scope changes later, access should be updated to match the current responsibility.

## Decision Guide

Use the lowest role that can safely make the decision.

- Issue labels, duplicates, stale reports, and routing: triage access or higher.
- Closing an issue as duplicate, out of scope, or resolved: triage access or higher.
- Reopening an issue with new evidence: triage access or higher.
- Merging documentation, tests, refactors, or low-risk fixes inside an owned area: committer access or higher.
- Merging customer-visible product behavior, infrastructure changes, or migrations: committer access with the right area ownership, required checks, and risk-appropriate review; maintainer approval when scope crosses teams or systems.
- Emergency revert of a broken change: committer access or higher in the affected area, followed by maintainer notification when production, security, or customer impact is involved.
- Release timing, release candidates, rollbacks, and production deployment policy: maintainer access.
- Security policy, vulnerability disclosure, privacy posture, production secrets, and incident response: maintainer access, with founder involvement for company-level decisions.
- Member invitations, permission changes, outside collaborators, branch protection, required checks, and repository settings: maintainer access.
- Public roadmap commitments, pricing, legal language, customer promises, or company-level prioritization: founders or delegated leads with founder-aligned authority.

When in doubt, pause the irreversible action, summarize the tradeoff, and escalate to the relevant lead or maintainer. Ara favors fast ownership, but not at the expense of user trust, security, or clear accountability.
