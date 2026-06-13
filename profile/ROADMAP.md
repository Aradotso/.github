# Ara Public Roadmap

Ara is an agent-building agent for macOS: a way to create, run, and refine agents that can work across your real desktop, browser, codebase, and connected tools. This roadmap sets public expectations for the next few quarters without exposing internal implementation details or committing to exact launch dates.

We review this roadmap quarterly so external users and contributors can see what is current, what is planned, and where help is most useful.

_Last reviewed: Q2 2026. Next review: Q3 2026._

## Current Focus

Ara is focused on making useful agents feel native on the Mac. The near-term work is about reliability, visibility, and control: agents should understand the task, operate the right apps, keep users informed, and leave behind reviewable work such as commits, diffs, notes, or completed workflows.

Today, the core product direction centers on:

- Desktop agents that can use Mac apps and browser surfaces in practical workflows.
- Background coding agents that work in isolated branches, commit changes, and prepare reviewable pull requests.
- Reusable skills and memory so agents improve from completed runs instead of starting from scratch every time.
- Connected app workflows across developer, product, and operating tools.

## Next 1–2 Quarters

### More transparent agent runs

We are improving how agent work is displayed while it is happening and after it finishes. Users should be able to see the plan, key actions, artifacts, validation results, and any assumptions the agent made.

### Stronger background coding workflows

Background coding agents will continue getting better at isolated worktrees, branch hygiene, validation, PR handoff, and recovery from common repo-specific issues. The goal is reviewable work that fits existing team workflows rather than a separate automation lane.

### Better skills and learning loops

Ara's skills system will become easier to author, inspect, reuse, and improve. We want agents to capture durable procedures from successful runs while keeping temporary task state out of long-term memory.

### Deeper app integrations

We are expanding practical integrations with the tools teams already use for engineering, support, product planning, analytics, and knowledge management. The priority is reliable end-to-end work, not shallow one-off connections.

## Next 2–4 Quarters

### Multi-agent workstreams

Ara will support richer handoffs between agents, including parallel research, implementation, review, and follow-up workflows. Users should be able to start a larger outcome and still understand which agent did what.

### Evaluation and reliability tooling

We plan to make agent behavior easier to test and improve over time with repeatable task evals, regression checks, and clearer success criteria for common workflows.

### Contributor-friendly extension points

We want external contributors to be able to improve skills, integrations, docs, and examples without needing internal context. Public contribution paths should make it clear where help is welcome and how changes will be reviewed.

## How to Contribute

The most useful public contributions are:

- Clear bug reports with the goal, expected behavior, actual behavior, and any safe-to-share logs or screenshots.
- Documentation improvements that explain real workflows end to end.
- Skills and examples for repeatable agent tasks.
- Integration ideas or prototypes for tools teams use every day.
- Reliability tests that capture common workflows and edge cases.

Open an issue in the relevant Ara repository or start from [ara.so](https://www.ara.so) if you are not sure where a contribution belongs.

## Roadmap Principles

This roadmap is intentionally public-facing. It avoids customer-private, security-sensitive, and internal-only details. Timing may change as we learn from users, but the direction should stay useful: agents that do real work, explain what happened, learn safely, and keep humans in control.
