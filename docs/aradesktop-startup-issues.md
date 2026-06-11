# AraDesktop Startup Timeline — Profiling Analysis & Prioritized Issues

Sourced from static analysis of the launch path (June 2026) and prior bg-session
profiling output. Files examined: AraApp.swift, AppState.swift, AppDatabase.swift,
AuthService.swift, AraHomeRoot.swift.

## Critical path

Process start → `@StateObject AppState()` init →
`applicationDidFinishLaunching` (800 ms budget, logged as `cold_launch_did_finish`) →
main window first frame.

The three dominant phases are:

1. **App init** — `AuthService.configure()` + `AppState.init()` run on the main thread
   while SwiftUI evaluates the first scene body.
2. **SwiftUI view setup** — `AraHomeRoot.ensureLayout()` + analytics boot chain +
   `AraMCPServer.startIfNeeded()` complete before the root view body is useful.
3. **Chat pane ready** — `AppDatabase` migrations (especially the araV5 FTS5 backfill)
   must finish before the chat list can load.

---

## Top 3 Slowest Phases

### Phase 1 — App init: keychain + memory bootstrap (AuthService.configure)

**Location:** `AuthService.swift` → `configure()` → `restoreAuthState()`

`AuthTokenStore.idToken` and `AuthTokenStore.refreshToken` are read synchronously
on the main thread — each is an XPC call to `securityd` that can stall 30–150 ms on
cold boot or post-sleep. Immediately after, `bootstrapNativeMemory()` reads, parses,
and rewrites memory-store files for signed-in users (50–200 ms for large stores).
Both run before the first SwiftUI frame is painted.

**Estimated cost:** 110–350 ms (combined, cold launch, returning user)

---

### Phase 2 — SwiftUI view setup: layout migration + analytics chain

**Locations:**
- `AraHomeRoot.swift` → `ensureLayout()` — filesystem enumeration + file moves
- `AraApp.swift` → 7+ analytics SDK calls (Sentry, PostHog, Mixpanel, Telemetry)
- `AraApp.swift` → `AraMCPServer.shared.startIfNeeded()` — TCP socket bind

All three run synchronously on the main thread during `applicationDidFinishLaunching`,
delaying the point at which `AraHomeRoot.body` first returns a usable view.

**Estimated cost:** 60–280 ms (combined, typical user)

---

### Phase 3 — Chat pane ready: FTS5 backfill blocks database actor

**Location:** `AppDatabase.swift` → `migrate()` → migration `araV5`

The araV5 migration runs
`INSERT INTO chat_messages_fts SELECT … FROM chat_messages`
synchronously, blocking the GRDB database actor. No chat-list query can run until
this completes. For users with large histories it can stall for 1–5 seconds.

**Estimated cost:** 100 ms – 5 s (history-size dependent; worst case is a launch blocker)

---

## Prioritized Issue List

### Issue 1 — Async-ify keychain reads in AuthService (HIGH / effort: S)

**Phase:** App init
**Fix:** Move `configure()` body to `Task.detached`. Render the UI optimistically
from the cheap `UserDefaults`-backed `AuthState.shared` (already tracks
`auth_isSignedIn` / `auth_userEmail`). Reconcile token state when the async read
completes.
**Impact:** 60–150 ms saved on every cold launch for signed-in users.
**Effort:** Small — isolate keychain reads, add a loading state to `AuthState`.

---

### Issue 2 — Defer FTS5 backfill to post-launch background task (HIGH / effort: M)

**Phase:** Chat pane ready
**Fix:** Split the araV5 migration: keep the `CREATE VIRTUAL TABLE chat_messages_fts`
DDL in the migration, but move the `INSERT INTO … SELECT …` backfill to a
`Task.detached(priority: .background)` that runs after first paint. Gate on a
`UserDefaults` flag (`fts_v5_backfill_done`) so it runs once and is skipped thereafter.
Until the flag is set, disable the search UI (show "indexing…") rather than blocking launch.
**Impact:** Eliminates a 100 ms – 5 s launch blocker for users with large histories.
**Effort:** Medium — migration refactor, UserDefaults gate, search-UI loading state.

---

### Issue 3 — Move memory bootstrap + layout migration off main thread (HIGH / effort: S–M)

**Phase:** App init + SwiftUI view setup
**Fix (3a):** Wrap `HermesSidecar.shared.bootstrapNativeMemory()` in
`Task.detached(priority: .utility)` inside `configure()`. The sidecar is async anyway.
**Fix (3b):** Move `AraHomeRoot.ensureLayout()` to `Task.detached(priority: .utility)`.
Gate the README rewrite on a `UserDefaults` version stamp instead of scanning content
every launch. Gate the legacy folder migration on a one-shot flag.
**Impact:** 70–280 ms saved combined.
**Effort:** Small-to-medium — no API contract changes; needs smoke test on first launch.

---

### Issue 4 — Bundle analytics SDK init into one background task (MEDIUM / effort: S)

**Phase:** SwiftUI view setup
**Fix:** Wrap all 7+ analytics boot calls in a single `Task.detached(priority: .utility)`.
Only `UIInteractionAnalytics.installNativeClickTracking()` needs the main thread — call
`await MainActor.run { }` for that one step inside the task.
**Impact:** 30–100 ms saved.
**Effort:** Small — already grouped in `applicationDidFinishLaunching`.

---

### Issue 5 — Async TCP socket bind for AraMCPServer (MEDIUM / effort: XS)

**Phase:** SwiftUI view setup
**Fix:** Wrap `AraMCPServer.shared.startIfNeeded()` in
`Task.detached(priority: .userInitiated)`. The call is already idempotent.
**Impact:** 10–100 ms saved.
**Effort:** Extra-small — single-line change.

---

### Issue 6 — Gate AppState.loadEnvironment() on #if DEBUG (MEDIUM / effort: XS)

**Phase:** App init
**Fix:** The five `String(contentsOfFile:)` calls in `loadEnvironment()` probe for
`.env` files at init time. One path is a hardcoded dev path
(`/Users/matthewdi/ara/.env`) that always misses in production. Gate the entire call
on `#if DEBUG`.
**Impact:** 5–30 ms saved in production builds; also removes a stale dev path.
**Effort:** Extra-small.

---

### Issue 7 — Defer LaunchServices + NSImage registration (LOW / effort: XS)

**Phase:** App init
**Fix:** Dispatch `setDefaultApplication(at:toOpenURLsWithScheme:)` (×2) and
`LSRegisterURL()` + `NSImage(contentsOf:)` to `Task.detached(priority: .background)`
or `DispatchQueue.main.async` after first runloop cycle.
**Impact:** 30–200 ms saved (worst case); URL scheme ownership does not need to be
claimed before first paint.
**Effort:** Extra-small.

---

## Aggregate Saving Estimate

Issues 1–3 together (H1 + H2 + H3):
- Conservative: ~210 ms
- Worst case eliminated: ~5.35 s (large DB + slow keychain + large memory store)

Issues 4–7 add another 75–430 ms on top.

---

## Instrumentation Recipe

To confirm timings before/after each fix:

```
sudo purge   # simulate cold cache
xcrun instruments -t "Time Profiler" -D /tmp/ara-startup.trace /Applications/Ara.app
```

Enable "Record Waiting Threads" to catch XPC stalls (keychain, launchd, distnoted).
Use System Trace for XPC message send/receive detail (best for Issues 1, 5, 7).
The existing `os.signpost` IDs in `AppDatabase.performInitialization` give named
intervals. Add signposts around `AuthService.configure()`,
`AraMCPServer.startIfNeeded()`, `ensureLayout()`, and the analytics chain for a
complete picture.
