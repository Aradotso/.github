# RFC: Lazy Worktree Creation on New Chat

**Status:** Draft  
**Author:** Ara (bg-agent)  
**Date:** 2026-06-11  
**Slack thread:** #ara-eng — feedback welcome

---

## Summary

When a user opens "New Chat", Ara currently allocates a git worktree immediately. This RFC proposes deferring that allocation until the user submits their first message — "lazy creation." The user sees a clean UI pre-seeded with `main`, and the worktree is spun up only when there is actual work to scope to it.

---

## Motivation

The current eager-creation model has two pain points:

1. Abandoned chats that never receive a message still consume a worktree slot and disk space.
2. The worktree name is chosen before the task context is known, so it cannot encode any semantics from the task.

Users who open many chat tabs — to think through options before committing to one — generate orphaned worktrees that accumulate silently.

---

## Proposed Design

### Phase 1 — New Chat UI (no worktree yet)

On "New Chat" click:
- Render the chat input pane as normal.
- Display the branch selector pre-populated with `main`.
- Do NOT call the worktree allocation API.
- Store the selected base branch in ephemeral UI state only (e.g., `pendingBaseBranch: "main"`).

### Phase 2 — First Message Submit

When the user submits their first message:
1. Generate a short random suffix (6 hex chars, e.g. `aebs3d`).
2. Construct the worktree name: `<baseBranch>-<suffix>` → `main-aebs3d`.
3. Call the worktree allocation API synchronously (or with an optimistic UI spinner).
4. Once the worktree is confirmed ready, dispatch the message into that worktree's git context.
5. Persist `worktreeId` to the chat record so subsequent messages route to the same slot.

### Phase 3 — Clone into Worktree Context

The message payload carries `worktreeId`. The backend attaches the agent's file tools to that worktree path before execution begins. No change to the agent protocol — worktree mounting is an infrastructure concern resolved before the agent sees the task.

---

## Tradeoffs

### Benefits

- Zero abandoned worktrees from chats that never get a message.
- First-message latency is hidden behind the spinner the user already expects when a model starts responding.
- Worktree name can encode a short hash derived from the message if desired (future work).
- UI simplifies: no intermediate "allocating…" states visible before the user has even typed.

### Costs

- First-message latency increases by ~the worktree-creation time (typically 200–600 ms for a local git-worktree add; longer if a remote clone is involved).
- The backend must handle the race: if the user submits a second message before the first worktree allocation completes, the system must queue or debounce.
- Error handling surface expands: worktree creation can fail (disk full, git lock, network) at a moment when the user expects a model response, not an infrastructure error.
- If branch selection is surfaced in the UI before submission, and the user changes it after typing a message but before submitting, the worktree must be created from the last-selected base — a subtle ordering constraint.

---

## Implementation Sketch

### AraDesktop (Swift)

```swift
// ChatViewModel.swift — on "New Chat"
struct PendingWorktreeContext {
    var baseBranch: String = "main"
    var worktreeId: String? = nil  // nil until first submit
}

// On first message submit:
func submitFirstMessage(_ text: String) async throws {
    guard viewModel.pendingContext.worktreeId == nil else { return }
    let suffix = String(UUID().uuidString.prefix(6).lowercased())
    let name = "\(viewModel.pendingContext.baseBranch)-\(suffix)"
    let wt = try await WorktreeService.shared.allocate(name: name)
    viewModel.pendingContext.worktreeId = wt.id
    await dispatchMessage(text, into: wt)
}
```

### AraWeb / API (Bun + Hono)

```typescript
// POST /worktrees  — called on first submit, not on new-chat
app.post("/worktrees", async (c) => {
  const { baseBranch, chatId } = await c.req.json();
  const suffix = crypto.randomBytes(3).toString("hex"); // 6 hex chars
  const name = `${baseBranch}-${suffix}`;
  const wt = await createWorktree({ name, base: baseBranch, chatId });
  return c.json({ worktreeId: wt.id, path: wt.path });
});
```

### State Machine

```
NEW_CHAT_OPENED
    → branch selector shows "main"
    → worktreeId = null

USER_SUBMITS_FIRST_MESSAGE
    → allocate worktree (async, spinner)
    → worktreeId = "main-aebs3d"
    → dispatch message

SUBSEQUENT_MESSAGES
    → worktreeId already set, skip allocation
```

---

## Risks

**Race on rapid double-submit.** If the user double-clicks Send, two allocation requests may fire. Mitigation: debounce submit handler; set a `isAllocating` flag to prevent concurrent calls.

**Allocation failure UX.** The user typed a message and hit send; if worktree creation fails, they see an error before the model even responds. Mitigation: surface a retry button in-thread rather than a modal, and preserve the message text.

**Git lock contention.** Heavy repos with active index operations may timeout on `git worktree add`. Mitigation: set a 5 s timeout and fall back to a temp directory outside git if exceeded.

**Branch mismatch on navigation.** If the user navigates away from the new-chat tab before submitting, the pending branch selection is lost. Mitigation: persist `pendingBaseBranch` to session storage keyed by tab ID.

**Telemetry gap.** Currently, worktree allocation is a proxy metric for "user started a task." Under lazy creation, this metric shifts to first-message submit, which is already tracked. Update dashboards accordingly (PostHog event rename: `worktree_allocated` → correlate with `chat_message_sent` order=1).

---

## Alternatives Considered

**Pre-warm a pool of ready worktrees.** Allocate worktrees ahead of time and assign on first message. Eliminates first-message latency but wastes resources for abandoned chats — the problem we are trying to solve.

**Keep eager allocation, GC quickly.** Allocate on New Chat as today, but run a garbage-collector that deletes worktrees with no messages after 60 s. Simpler code path, but introduces a GC race and does not simplify the UI state machine.

**Name worktree after chat UUID.** Use the chat's UUID as the worktree name rather than `<branch>-<suffix>`. Stable and collision-free, but less human-readable in `git worktree list` output.

---

## Open Questions

1. Should the branch selector in the New Chat UI be collapsed by default, showing only "main", with an expand affordance for advanced users?
2. What is the right timeout for worktree allocation before we surface an error vs. retry silently?
3. Should the suffix be derived from the first message's content (for readability) rather than random?

---

## Feedback

Drop questions or objections in **#ara-eng** on Slack. Tag `@sven` or `@adi` for architectural decisions. This RFC is open for one week before moving to "Accepted" or "Rejected."
