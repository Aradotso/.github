# AraDesktop startup optimization — prioritized issue list

Extracted from live boot profiling (`/private/tmp/ara-freeze.log` + `/private/tmp/ara-dev.log`),
the `2026-06-08-latency-audit.md`, `2026-06-10-app-weight-audit.md`, and `2026-06-11-perf-snappiness.md`
learnings. Three measured phases drive the felt cold-start lag.

---

## Measured baseline (cold launch, dev build)

| Phase | Duration | How measured |
|---|---|---|
| AppState.init → Main Window onAppear | 355ms | `ara-freeze.log` SCENE timestamps |
| applicationDidFinishLaunching (total) | 134ms | BOOT timestamps (165ms–299ms) |
| → of which: AnalyticsManager.initialize | **97ms** | BOOT timestamps (192ms–289ms) |
| Finish-launching → DATA LOAD start | 671ms | freeze.log vs dev.log wall-clock delta |
| Chat pane time-to-interactive (cold) | **1165ms** | `DATA LOAD: time-to-interactive 1165.3ms` |
| Chat pane time-to-interactive (warm) | 311–458ms | subsequent DATA LOAD entries |
| Post-launch main-thread stall | **1675ms** | `MAIN-THREAD STALL: round-trip=1675ms` |
| HermesSidecar: spawn → healthy | **1005ms** | dev.log `healthy after 1005ms` |

Cold-to-interactive total (process start → chat pane usable): **~2.5 seconds**.

---

## Issue 1 — AnalyticsManager.initialize blocks the main thread for 97ms

**Phase:** App init (`applicationDidFinishLaunching`)
**Measured cost:** 97ms synchronous on the main thread, between `logCodeSignatureStatus`
(`802571109.192443`) and `after AnalyticsManager.initialize` (`802571109.289481`).
This is the single largest serialized cost inside `applicationDidFinishLaunching`.

**Root cause:** `AnalyticsManager.initialize` (PostHog SDK init + session-replay setup)
runs synchronously on the main thread during `applicationDidFinishLaunching`. PostHog's
`setup(_:options:)` performs SDK configuration, writes to disk, and may synchronize
network state — all before the app's window is interactive.

**Optimizations (in priority order):**

1. **Defer to a background task** — move `AnalyticsManager.initialize` into a
   `Task.detached(priority: .utility)` fired at the end of `applicationDidFinishLaunching`.
   Analytics does not block UI display; it is safe to delay by one event-loop turn.
   All events queued before the SDK is ready should be buffered (PostHog supports this
   natively via its pre-init event queue). **Estimated savings: 80–95ms off cold-start.**

2. **Defer session-replay attachment** — `UIInteractionAnalytics.installNativeClickTracking`
   and `AnalyticsManager.appLaunched` follow immediately (5ms combined); defer them in
   the same detached task.

3. **Background thread analytics identify** — `AnalyticsManager.identify` at boot reads
   user profile data; ensure it doesn't re-sync on the main thread once deferred.

**Impact:** High — directly reduces `applicationDidFinishLaunching` by ~70%, shaving
97ms off measured cold-start. The user sees a responsive window 97ms sooner.

**Effort:** Low-medium — 1–2 hour change in `AppDelegate.swift`/`AnalyticsManager.swift`.
Risk is low because PostHog's SDK queues events fired before init completes.

**Files:**
- `AraDesktop/Desktop/Sources/AnalyticsManager.swift`
- `AraDesktop/Desktop/Sources/AppDelegate.swift` (the `applicationDidFinishLaunching` sequence)

---

## Issue 2 — SwiftUI view setup: 355ms pre-window + 671ms before chat DATA LOAD starts

**Phase:** SwiftUI view setup (`AppState.init ENTER` → DATA LOAD start)
**Measured cost:** 355ms from first `AppState.init ENTER` to `Main Window content onAppear`,
then a further 671ms from `applicationDidFinishLaunching EXIT` to `DATA LOAD: Starting data load`.
Total: **~1026ms** before the chat pane begins loading data.

**Root causes:**

- **332ms gap between cold `AppState.init EXIT` and scene re-init** — this is likely
  dyld/Gatekeeper/codesign overhead on first cold launch (outside our control), but is
  worth confirming with `DYLD_PRINT_STATISTICS_DETAILS`.
- **`AraPreviewCursorNarrator.bootstrap` takes 14.3ms** on the main thread — this is
  an accessibility/cursor subsystem; investigate whether it can be deferred.
- **671ms from finish-launching to DATA LOAD** — the main window's `onAppear` triggers
  SwiftUI body evaluation of `AraSettingsView` (the ~12k-line root view) before the
  `RunChatView`/chat provider starts its data fetch. This gap is the cost of the initial
  SwiftUI layout pass for the entire sidebar + content area.

**Optimizations:**

1. **Split `AraSettingsView` body into separately-constructed subtrees** — the current
   ~12k-line view body is evaluated as a single unit on every `@State` change. Breaking
   the sidebar, the tab-content router, and the content panes into `@StateObject`-owned
   sub-views reduces the cold-start layout cost and has a compounding benefit on every
   tab switch (see iteration 2 of the perf-snappiness loop: `withAnimation` on a huge
   body storms the whole tree for 140ms per switch). **Estimated savings: 100–300ms off
   the 671ms gap.** High uncertainty — needs measurement with `TimedOp`.

2. **Defer `AraPreviewCursorNarrator.bootstrap`** — 14.3ms on the main thread. If this
   is not needed before the first frame renders, push it to a `DispatchQueue.main.asyncAfter(deadline: .now() + 0.5)`.
   **Estimated savings: 14ms.** Low effort.

3. **Eagerly trigger DATA LOAD from `applicationDidFinishLaunching`** — instead of
   waiting for the SwiftUI view to appear and trigger `ChatProvider.startDataLoad`, fire
   the data fetch from `AppDelegate` right after `ChatProvider.init` (which takes only
   1.5ms). The data arrives before the view is fully laid out. **Estimated savings:
   200–400ms off chat pane TTI.** Medium effort — requires ChatProvider to accept a
   pre-view-open `startPrefetch()` call and wire results into the view's state on appear.

4. **Profile `DYLD_PRINT_STATISTICS_DETAILS`** on a real cold boot to attribute the
   332ms pre-scene gap. If it's a large statically-linked framework (Sentry, PostHog,
   GRDB), evaluate dynamic linking or lazy initialization.

**Impact:** High — the combined 1026ms pre-DATA-LOAD window is the dominant visual latency.
Shaving 300–500ms off it brings the felt launch time from ~2.5s to under 2s.

**Effort:** Medium-high — view refactor (item 1) is a 1–2 day change with behavior risk;
the others are lower risk and faster. Instrument with `mainwindow_tab_switch` `TimedOp`
before and after.

**Files:**
- `AraDesktop/Desktop/Sources/MainWindow/AraSettingsView.swift` (split body)
- `AraDesktop/Desktop/Sources/AppDelegate.swift` (defer bootstrap, eager data prefetch)
- `AraDesktop/Desktop/Sources/Providers/ChatProvider.swift` (prefetch entry point)

---

## Issue 3 — Chat pane time-to-interactive: 1165ms cold vs 311ms warm (HermesSidecar + decode)

**Phase:** Chat pane ready (`DATA LOAD: Starting data load` → `time-to-interactive`)
**Measured cost:** 1165ms cold, 311–458ms warm. Delta of **~750ms is entirely attributable
to HermesSidecar spawn**: `[HermesSidecar] spawned pid 950` at `17:25:11.633`,
`healthy after 1005ms` at `17:25:12.639` — the sidecar health-check adds over a second
on first cold open.

**Root causes:**

1. **HermesSidecar starts on-demand (lazy)** — the Python sidecar process is not spawned
   until the first chat page opens. Its 1005ms startup (Python interpreter + sidecar
   provisioning + health check with 2 polls) delays the first chat from interactive.

2. **Chat history decode on the main thread (partially fixed)** — the 2026-06-08 latency
   audit found and fixed the `ConversationHistorySection` 10s-periodic main-thread decode.
   However the initial DATA LOAD still decodes history during the `time-to-interactive`
   window; warm opens (311ms) show the decode itself is fast once data is cached.

3. **`searchCandidates` O(chats × projects) rebuild** — fixed in the 2026-06-08 pass for
   the search page, but the underlying per-open data indexing may still pay this on first
   DATA LOAD open.

**Optimizations:**

1. **Pre-warm HermesSidecar at app launch** — spawn the sidecar process in a
   `Task.detached` immediately after `applicationDidFinishLaunching`, racing it against the
   SwiftUI layout phase. By the time the user opens a chat, the sidecar will already be
   healthy. **Estimated savings: 750–900ms off cold chat pane TTI** (eliminating the
   delta vs warm). This is the single highest-leverage startup optimization available.

2. **Increase health-check poll frequency or use a ready-signal** — the sidecar waits
   for 2 polls at some interval. If the polling interval is ≥500ms, switching to a
   UNIX domain socket readiness signal (the sidecar writes a byte when healthy) would
   cut the detection lag to <10ms from when the sidecar is actually ready.

3. **Persist sidecar PID across launches** — if the sidecar process survives app restarts
   (e.g. as a LaunchAgent), the 1005ms spawn cost is never paid after first install.
   This is a larger infrastructure change but eliminates the cost entirely.

4. **Cap history rows for initial DATA LOAD** — the 1165ms cold TTI suggests the first
   history decode is heavier than warm (311ms). If `ConversationHistorySection` fetches
   uncapped rows on first open, apply the same LRU cap (already used elsewhere) to limit
   the initial decode to the most recent N messages.

**Impact:** Very high — **pre-warming the sidecar alone cuts cold chat-pane TTI by ~65%**
(from ~1165ms to ~310ms, matching warm behavior). This is the highest felt-latency win
available without touching the UI layer.

**Effort:** Low — pre-warm is a 1–2 hour change in `AppDelegate`. Poll-to-signal and
PID persistence are medium.

**Files:**
- `AraDesktop/Desktop/Sources/AppDelegate.swift` (spawn sidecar early)
- `AraDesktop/Desktop/Sources/Providers/HermesSidecar.swift` (or equivalent sidecar manager)
- `AraDesktop/Desktop/Sources/Providers/ChatProvider.swift` (pre-warm coordination)

---

## Summary: prioritized order

| # | Issue | Effort | Estimated savings | Priority |
|---|---|---|---|---|
| 3a | Pre-warm HermesSidecar at launch | Low (1–2h) | ~750ms cold chat TTI | **P0** |
| 1 | Defer AnalyticsManager.initialize to background | Low-medium (1–2h) | ~97ms finish-launching | **P1** |
| 2c | Eagerly trigger DATA LOAD from AppDelegate | Medium (4–6h) | 200–400ms chat TTI | **P1** |
| 2b | Defer AraPreviewCursorNarrator.bootstrap | Low (30min) | 14ms | **P2** |
| 2a | Split AraSettingsView into subtrees | High (1–2 days) | 100–300ms layout | **P2** |
| 3b | Sidecar readiness signal (socket vs poll) | Medium (4h) | 0–200ms detection lag | **P2** |
| 3c | Sidecar as LaunchAgent (persistent) | High (1 day) | eliminates spawn entirely | **P3** |
| 2d | Profile DYLD stats for 332ms pre-scene gap | Low (1h investigation) | TBD | **P3** |

**Quick wins (do first):** items 3a + 1 together take one engineer ~half a day and
recover **~850ms** of cold-start latency with minimal risk.
