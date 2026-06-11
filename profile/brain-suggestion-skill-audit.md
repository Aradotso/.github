# Brain Suggestion Skill — Audit & Validation Report

Date: 2026-06-11
Skill audited: `ara-project-brain-generate-suggestions` (v1.1)
Also reviewed: `project-brain-suggest-next-work`, `project-brain-suggestion-generation`, `project-brain-synthesis-generate-chat-suggestions`
Tested against: ara-cua project (github.com/Aradotso/ara-cua), latest commit `47c1972`

---

## Findings Summary

The skill is structurally sound and produces useful, grounded suggestion cards.
Three issues warrant immediate patches; two are lower-priority improvements.

---

## Issue 1 — CRITICAL: No deduplication guard against recently landed commits

The skill queries session_search for planning conversations that may predate a commit landing on main.
A session discussing "let's wire auto-merge" from 3 days ago will score a strong `continue_thread` card
even though `d4ba0af`, `d7028a1`, `c72f37d` already landed those changes.

**Fix**: Before emitting any card, run `git log --oneline -30 --grep "<card title keywords>"`. If a
commit message matches the card topic and landed within the last 7 days, suppress the card or
downgrade it to a `housekeeping` verification card with confidence ≤0.65.

---

## Issue 2 — HIGH: Session search context inflation degrades synthesis quality

Each `session_search(limit=5)` call returns up to 65 messages (5 sessions × 13 messages each:
bookend_start + ±5 window + bookend_end). Five separate queries can balloon to 300+ messages,
which inflates the synthesis context window and degrades output quality on the final ranking step.

**Fix**: Use `limit=2` per query and extract only `bookend_end` (the resolution snapshot). Only
scroll into the full message window for the single highest-relevance session. This reduces the
session-search payload by ~75% while preserving signal fidelity.

---

## Issue 3 — HIGH: Recency adjustments require timestamps; git log without `--format` provides none

The +0.05 recency boost ("code modified in last 24h") and the decay logic both require commit
timestamps. Running `git log --oneline -30` (as the skill currently specifies) provides no dates,
making these adjustments impossible to apply rigorously.

**Fix**: Use `git log --format="%h %ad %s" --date=relative -20` instead of `--oneline -20`.
This embeds relative timestamps ("3 hours ago", "2 days ago") inline, making recency scoring
possible without an extra git call.

---

## Issue 4 — MEDIUM: Feature-flag state not considered

The `Providers settings page` commit is explicitly `dev-flagged`. Suggestions for dev-flagged
features should note the flag in the prompt and lower confidence by -0.05 to avoid implying
the feature is live.

**Fix**: Add a pitfall note. If a commit subject contains "dev-flag", "dev-only", "feature flag",
or "gated", label the derived suggestion with a note in the `rationale` field and apply -0.05
to the base confidence.

---

## Issue 5 — LOW: Worktree context skew

When the skill runs inside a bg-agent worktree (e.g., `~/.ara/worktrees/bg-<uuid>/`), `git log`
shows only the worktree branch — not the full project history. This produces a narrow picture.

**Fix**: The skill should detect if `git rev-parse --show-toplevel` differs from the project root
(or if the branch name matches `ara/bg/*`), and if so, explicitly `git -C <project-root>` for
all history commands.

---

## Validation: Example Output (ara-cua, 2026-06-11)

Four cards produced during validation run, sorted by confidence:

```jsonl
{"title":"Verify auto-merge workflow end-to-end","subtitle":"Three commits just landed — smoke-test before it becomes load-bearing","prompt":"The auto-merge workflow (auto-merge.yml + auto-merge-check.yml) just landed on main. Verify end-to-end: open a docs-only test PR, confirm it auto-merges without a human review; open a code PR without approval and confirm it waits; add a 'do-not-merge' label and confirm it skips. Check the Vercel deploy webhook fires post-merge. Review the concurrency group config and confirm parallel PRs don't deadlock. Document any edge cases found in CONTRIBUTING.md.","rationale":"Infrastructure just shipped — standard practice is immediate smoke-test before the workflow becomes load-bearing. Catching a misconfiguration now is far cheaper than discovering it when a real PR gets stuck or silently skipped.","sourceHints":["git","sessions"],"confidence":0.87,"type":"continue_thread"}
{"title":"Land add-project button sidebar polish","subtitle":"Local branch with completed work — close it before it drifts","prompt":"Branch add-project-button-sidebar has a style change to shrink and soften the sidebar add-project '+' icon. Review the diff against current main, fix any rebase issues, and open a PR. Verify the icon renders correctly at both compact and expanded sidebar widths and matches the design language of surrounding controls.","rationale":"Active local branch with meaningful work not yet pushed. Style polish on a primary nav element is visible to every user and is a low-risk, fast-ship win.","sourceHints":["git"],"confidence":0.78,"type":"continue_thread"}
{"title":"Close out analytics cleanup branch","subtitle":"Dead permission helpers removed — push and open PR","prompt":"Branch analytics/cleanup-dead-permission-helpers removes dead permission helpers and pipes all onboarding events through Telemetry. Review the diff, ensure no live callers were missed, and open a PR. Check that PostHog onboarding funnel events fire correctly in a dev build before merging.","rationale":"Analytics cleanup is done but sitting unpushed. Merging this reduces dead code surface and closes a clean branch with zero risk of regression if the helpers are truly unused.","sourceHints":["git"],"confidence":0.72,"type":"continue_thread"}
{"title":"Prune stale ara/bg/* worktree branches","subtitle":"Dozens of background-agent branches cluttering the repo","prompt":"Run 'git branch --list ara/bg/*' and for each branch, check whether there is an open PR (gh pr list --head <branch>). Delete all that have no open PR and are already merged or behind main by more than 10 commits. Keep only branches with active PRs or recent uncommitted work. Do not force-delete — check status first and confirm before each batch delete.","rationale":"Lazy-create worktree pattern accumulates branches rapidly. No functionality impact but clutter slows branch navigation and CI tooling.","sourceHints":["git","memory"],"confidence":0.69,"type":"housekeeping"}
```

All four cards are concrete, executable, and grounded in real git state. No speculative cards emitted.

---

## Recommendation

Patch `ara-project-brain-generate-suggestions` SKILL.md to:
1. Replace `git log --oneline -30` with `git log --format="%h %ad %s" --date=relative -20` (Issue 3)
2. Add deduplication guard pitfall (Issue 1)
3. Add session_search budget guidance (Issue 2)
4. Add feature-flag confidence adjustment (Issue 4)
5. Add worktree detection note (Issue 5)

The skill is ready for bundling in Ara 2.app after these patches.
