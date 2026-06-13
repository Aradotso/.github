# Contributing to Ara

Ara's public profile and related repositories are maintained by a small team of founders, delegated leads, and trusted contributors. We use the least access required for the work, expand permissions only after repeated good judgment, and reduce or remove access when responsibilities change.

## Team Roles and Maintainer Levels

### Contributors

Contributors include community members, contractors, advisors, and Ara teammates who help without repository write access. Contributors can:

- Open issues and pull requests.
- Propose documentation, product, design, infrastructure, or policy changes.
- Review public discussions and add context from their area of expertise.
- Suggest labels, priorities, owners, or follow-up work.

Contributors do not make binding roadmap, release, security, privacy, membership, or repository-permission decisions. A lead, committer, maintainer, or founder must accept and merge their changes.

### Triage access

Triage access is for trusted contributors or teammates who have shown consistent issue hygiene and good judgment in a specific repository or product area. Triage users can:

- Apply and adjust labels, milestones, projects, assignees, and duplicate markers.
- Ask for reproduction details, logs, screenshots, impact, customer context, or product-owner input.
- Close duplicate, stale, already-fixed, unactionable, or clearly out-of-scope issues.
- Reopen issues when new evidence changes the priority or scope.
- Route security-sensitive reports to Ara's private security process instead of discussing details publicly.

Triage users can decide issue organization, duplicate handling, reproduction requirements, and whether a public issue has enough information to stay open. They cannot merge pull requests, approve releases, change repository settings, manage members, or make final security-policy decisions.

### Committer access

Committer access is for delegated leads and trusted contributors who can land changes in a defined scope. Committers can merge pull requests when all of the following are true:

- The change is inside their repository, system, product area, or documented ownership scope.
- Required CI, lint, tests, review, and manual validation are complete or a maintainer has approved an explicit exception.
- The change has appropriate review from the code owner, product lead, design lead, security reviewer, or founder when the change touches their area.
- The pull request does not alter release policy, security policy, billing, privacy posture, member access, branch protection, production secrets, or company-level commitments without maintainer approval.

Committers can decide routine implementation details, documentation updates, bug fixes, dependency updates, safe refactors, and scoped feature changes. They can also revert a change they merged when it is clearly breaking users or blocking development, then notify the relevant lead or maintainer. They cannot publish official releases, manage organization membership, approve security policies, or override founder or maintainer calls.

### Maintainer access

Maintainer access is held by Ara's founders and delegated leads who own repositories, release paths, security-sensitive systems, or cross-functional product areas. Maintainers can:

- Publish releases, approve release candidates, and coordinate rollback decisions.
- Manage repository settings, branch protection, required checks, environments, deploy gates, and automation permissions.
- Add, remove, or scope organization members, outside collaborators, triage users, and committers.
- Approve security policies, vulnerability disclosure language, incident response changes, and security-sensitive fixes.
- Make final decisions when product, engineering, design, support, security, or founder priorities conflict.

Maintainers can decide access levels, release readiness, production-risk tradeoffs, cross-repository architecture, public policy language, and escalation outcomes. Founder maintainers retain final authority for company-level, security-sensitive, legal, brand, and irreversible customer-impacting decisions.

## Escalation Path

Ara promotes access based on demonstrated judgment, scope clarity, and sustained contribution rather than tenure alone.

1. Contributor to triage: a contributor repeatedly opens or improves high-signal issues, reproduces bugs, proposes clear labels or priorities, and routes sensitive reports responsibly.
2. Triage to committer: a triage user consistently reviews and prepares issues or pull requests in one area, understands the validation expectations, and has a lead willing to sponsor scoped merge access.
3. Committer to maintainer: a committer repeatedly lands safe changes, handles incidents or reversions well, mentors others, understands Ara's release and security posture, and is trusted by founders or existing maintainers to own a repository, system, product area, or release path.

Access can also move the other direction. Maintainers should narrow, pause, or remove permissions when someone's ownership changes, work becomes inactive, or a role no longer needs that level of access.

## Decision Guide

Contributors can propose changes, provide context, review discussions, and recommend next steps.

Triage users can decide labels, duplicate status, issue closure or reopening, reproduction requirements, and routing to the right owner.

Committers can decide scoped implementation details, routine merges, safe refactors, documentation changes, dependency updates, bug-fix merges, and urgent reverts for changes they own.

Maintainers can decide releases, production-risk exceptions, repository settings, branch protection, access changes, security-policy approvals, incident response, and cross-functional conflicts.

Founders can make final calls on company-level priorities, security-sensitive decisions, legal or brand commitments, membership norms, and irreversible customer-impacting changes.

When a decision spans multiple areas, use the highest relevant role. When in doubt, pause the public action, document the tradeoff, and escalate to the owning lead, maintainer, or founder before merging, releasing, changing access, or discussing sensitive details.
