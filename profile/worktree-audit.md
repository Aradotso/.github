# Worktree Audit – amp repo

**Date:** 2026-06-10

## Summary

`git worktree prune` was run against `/Users/sve/code/amp`. No stale entries were pruned.

## Inspected worktree: bg-c2c734d9-cf03-4d29-8d87-68fa521b-205a44

The task asked to inspect this worktree for staleness. It was not found:
- The `.git/worktrees/bg-c2c734d9-cf03-4d29-8d87-68fa521b-205a44/` directory does not exist.
- It does not appear in `git worktree list`.

Conclusion: the worktree was never created, or was already pruned by a prior run. No action required.

## Active worktrees (as of audit)

All 13 active `ara/bg/*` worktrees were created today (2026-06-10) and are currently in use by
background agent tasks. None qualify as stale (>7 days inactive).

## Result

Working state is clean. No pruning was necessary.
