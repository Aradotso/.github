# Ara Public Roadmap

Ara is building the agent-native workspace for people who want useful automations that actually run: power users, developers, founders, and teams turning repeatable computer work into dependable agent loops.

This roadmap mirrors the direction shared on [ara.so/roadmap](https://ara.so/roadmap): Ara should understand your product and codebase, pick up high-value next steps, run them across files, browsers, terminals, and review surfaces, then keep what it learns as reusable memory and skills.

Dates are directional, not promises. We update this roadmap as capabilities ship, customer feedback changes priorities, or safety requirements reshape the order of work.

## Now

### Background coding agents

Ara can take scoped coding tasks in isolated worktrees, make changes headlessly, validate them, and hand off branches for review. Near-term work focuses on making these runs more reliable for real repositories:

- Stronger worktree setup and cleanup for parallel agent tasks.
- Better validation defaults for docs, frontend, backend, and desktop projects.
- Clearer PR handoff summaries with the exact files changed and test evidence.
- Safer branch and push behavior so background agents never disturb `main`.

### Skills, memory, and repeatable workflows

Every successful run should make the next run better. Ara is improving how it captures durable project conventions, reusable procedures, and user preferences without turning temporary task state into long-term memory.

- More precise skill creation after complex runs.
- Better skill repair when a workflow becomes stale.
- Cleaner separation between personal preferences, project knowledge, and one-off task history.
- More transparent summaries of what Ara learned from each run.

### Mission control for agent work

Ara is making long-running and parallel work easier to supervise without babysitting it.

- Clearer run status, validation state, and handoff outcomes.
- Better visibility into active chats, background branches, files, browser panes, and terminal surfaces.
- Lightweight review surfaces that show what changed before a human merges it.

## Next

### Planned agent types

Ara’s next agent templates are focused on work founders and developers repeat every week:

- Product growth agents that inspect funnels, analytics, and landing pages, then propose or ship experiments.
- Documentation agents that keep READMEs, onboarding guides, changelogs, and public profile pages current.
- QA and release agents that run checks, reproduce issues, prepare release notes, and watch post-release signals.
- Customer and founder support agents that summarize inbound messages, draft follow-ups, and turn repeated questions into product work.
- Research agents that monitor competitors, technical references, and customer signals, then produce actionable briefs.

### Platform enhancements

Ara is investing in the platform layer that makes agent work dependable on a real Mac and across real apps:

- More robust browser, terminal, file, and workspace coordination.
- Safer long-running task orchestration with resumable context and clearer failure recovery.
- Richer project understanding from git history, open sessions, docs, and learned skills.
- Better review gates for risky operations such as production deploys, billing changes, and broad refactors.
- More explicit permissions and audit trails for what an agent changed and why.

### Integrations

Ara should meet teams where work already happens. Planned integrations prioritize the tools common to builders and operators:

- GitHub and Linear for issue triage, branch handoff, PR review, and release tracking.
- Slack and email for founder/customer loops, summaries, and approval requests.
- Vercel, Railway, Supabase, and similar platforms for deploy and environment-aware automation.
- Sentry, PostHog, Stripe, and analytics tools for incident, growth, and revenue workflows.
- Knowledge tools such as docs, notes, and shared drives so agents can ground their work in team context.

## Later

### Self-driving loops

Ara’s longer-term direction is compounding autonomy: agents that notice the next valuable improvement, run it safely, ship it for review, learn the method, and queue the next loop.

This means:

- Scheduled agents that keep products, docs, analytics, and operations moving without a fresh prompt every time.
- Feedback loops that connect production signals back into product and engineering work.
- Better controls for when Ara can act alone, when it should ask for review, and when it must stop.
- Team-level memory and skills that improve with every approved run.

### Agent marketplace and shared playbooks

As agent workflows mature, Ara plans to make the best patterns easier to reuse:

- Public and private agent templates for common founder, developer, and operator jobs.
- Shareable skills and playbooks that teams can adapt to their stack.
- Safer defaults for installing, reviewing, and customizing community workflows.

## How we prioritize

We prioritize work that makes agents more useful, safer, and easier to trust:

- Does it help a user finish a real job end to end?
- Does it reduce repeated manual steering?
- Does it make background work more visible and auditable?
- Does it improve safety around files, browsers, terminals, accounts, and production systems?
- Does it help Ara learn from successful runs without preserving stale or sensitive details?

## Update cadence

We review this public roadmap quarterly and update it when shipped work, customer feedback, or safety requirements change the product direction.

If you are building automations with Ara and want something prioritized, start from [ara.so](https://ara.so) or open a discussion in this organization.