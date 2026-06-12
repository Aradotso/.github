# AraDesktop Startup Profiling Analysis

**Date:** 2026-06-12  
**Scope:** App launch → window visible → chat pane ready  
**Source revision:** ara-cua main, AraDesktop/Desktop/Sources (169 Swift files)  
**Method:** Static code analysis of startup-critical paths (AraApp.swift, AppState.swift, AppDatabase.swift, FileIndexing/)

---

## Executive Summary

Static analysis identified 10 distinct startup bottlenecks across three subsystems. Three bottlenecks each exceed 100 ms individually; together they account for an estimated 600–1 100 ms of avoidable latency before the chat pane is interactive. All three are fixable without architectural changes.

---

## Top 3 Bottlenecks (>100 ms each)

### 1. Launch Services IPC calls in `applicationDidFinishLaunching` (~150–400 ms)

**File:** `AraDesktop/Desktop/Sources/AraApp.swift`, lines 244–254, 291  
**Type:** Synchronous IPC to `launchservicesd`

Two back-to-back `NSWorkspace.shared.setDefaultApplication(at:toOpenURLsWithScheme:)` calls claim the `ara://` and `ara-dev://` URL schemes synchronously on the main thread. Each talks to `launchservicesd` via Mach IPC. On a busy system (post-update, first boot, or when Spotlight is indexing), each call can stall for 50–200 ms. Immediately after, `LSRegisterURL(_:_:)` at line 291 adds another IPC round-trip (~10–50 ms). These run before the `NSWindowController` is even created, so the window is invisible for the entire duration.

**Proposed fix — Background Task**

Move all three Launch Services registrations to a detached `Task` (or `DispatchQueue.global(qos: .background).async`) launched from `applicationDidFinishLaunching`, after the main window has been shown. URL scheme ownership persists from a previous launch, so the app is already registered when the user clicks a link. Registering in the background only affects the case where a link is opened in the 100–400 ms window between launch and registration completing — acceptable.

```swift
// Before (blocking, main thread):
NSWorkspace.shared.setDefaultApplication(at: bundleURL, toOpenURLsWithScheme: "ara") { _, _ in }
NSWorkspace.shared.setDefaultApplication(at: bundleURL, toOpenURLsWithScheme: "ara-dev") { _, _ in }
LSRegisterURL(cfURL, true)

// After (non-blocking):
Task.detached(priority: .background) {
    NSWorkspace.shared.setDefaultApplication(at: bundleURL, toOpenURLsWithScheme: "ara") { _, _ in }
    NSWorkspace.shared.setDefaultApplication(at: bundleURL, toOpenURLsWithScheme: "ara-dev") { _, _ in }
    LSRegisterURL(cfURL, true)
}
```

**Estimated saving:** 150–400 ms before first window frame.

---

### 2. Analytics & Telemetry SDK initialization on main thread (~120–250 ms)

**File:** `AraDesktop/Desktop/Sources/AraApp.swift`, lines 308–319  
**Type:** Synchronous disk I/O + heavy SDK construction on main thread

`Telemetry.boot()` (Sentry), `AnalyticsManager.shared.initialize()` (MixPanel + PostHog), and three `.track*` calls are called inline in `applicationDidFinishLaunching` before the window appears. SDK constructors read persisted event queues from disk, initialise crypto contexts, and register `URLSession` tasks — all synchronously. PostHog additionally fetches remote feature flags on startup. Disk reads for persisted queues alone account for 50–150 ms on a cold cache; the PostHog flag fetch is async inside the SDK but the `URLSession` task submission overhead and disk reads happen synchronously.

**Proposed fix — Deferred initialization via lazy loading**

Wrap SDK initialisation in a `DispatchQueue.global(qos: .utility).asyncAfter(deadline: .now() + 0.5)` block so it runs after the window is visible. Analytics events submitted before the SDK initialises can be queued in a lightweight local buffer and flushed when the SDK becomes ready.

```swift
// Before:
Telemetry.boot()
AnalyticsManager.shared.initialize()
AnalyticsManager.shared.trackAppLaunch()

// After:
DispatchQueue.global(qos: .utility).asyncAfter(deadline: .now() + 0.5) {
    Telemetry.boot()
    AnalyticsManager.shared.initialize()
    AnalyticsManager.shared.trackAppLaunch()
}
```

For events that need to fire before 500 ms (e.g. crash reporting), keep Sentry's `SentrySDK.start` on the main thread but move MixPanel/PostHog construction to the deferred block.

**Estimated saving:** 120–250 ms before first window frame.

---

### 3. GRDB legacy migration file scan in `AppDatabase.performInitialization()` (~100–500 ms+)

**File:** `AraDesktop/Desktop/Sources/AppDatabase.swift`, lines 352–401, 122–172  
**Type:** Sequential file I/O + raw `sqlite3_open` per legacy database

On every launch, four migration guard checks run in series before the main `DatabasePool` is opened:

- `migrateLegacyAraAppSupportIfNeeded()` scans `~/Library/Application Support/` for an old `Ara/` directory
- `migrateFromLegacyPathIfNeeded(to:)` opens legacy `DatabasePool`, runs `PRAGMA wal_checkpoint(TRUNCATE)`, and moves files
- `omi.db → ara.db` rename check (`fileExists` + conditional `moveItem`)
- `ara.db → ara.db` rename check (same)

The `mergeMessagesFromOtherDatabases` function (lines 122–172) iterates all subdirectories under `users/`, calling raw `sqlite3_open` + `sqlite3_exec` for each. On machines with multiple sign-in/sign-out cycles, there can be 5–10 separate database files, each requiring its own open/close round-trip. These run inside the actor's `configure()` synchronous context and block any concurrent actor tasks that need the database.

Additionally, the FTS5 migration (V5 in `migrate()`) bulk-inserts all existing `chat_messages` rows into a virtual table. On a large conversation history (>10k rows), this write transaction can take several seconds.

**Proposed fix — Guard flag + batching**

Introduce a persistent flag (e.g. `UserDefaults` key `legacyMigrationComplete`) written once when all legacy migrations pass. On subsequent launches, skip the entire scan in O(1):

```swift
func performInitialization() async throws {
    if !UserDefaults.standard.bool(forKey: "legacyMigrationComplete") {
        try await migrateLegacyAraAppSupportIfNeeded()
        try await migrateFromLegacyPathIfNeeded(to: currentPath)
        try await mergeMessagesFromOtherDatabases()
        UserDefaults.standard.set(true, forKey: "legacyMigrationComplete")
    }
    // proceed with pool open
}
```

For FTS5 migration on large databases, move the bulk-insert to a background `Task` that populates FTS incrementally after the app is interactive, with full-text search disabled (falling back to `LIKE`) until the index is ready.

**Estimated saving:** 100–500 ms per launch on established installs; several seconds on large history installs hitting the FTS5 migration.

---

## Additional Bottlenecks (each <100 ms individually, cumulative ~300–500 ms)

### 4. `AppState.loadEnvironment()` — sync file reads in SwiftUI scene construction

**File:** `AppState.swift`, lines 219–260  
**Issue:** Five `String(contentsOfFile:encoding:)` calls run synchronously during `@StateObject` construction on the main thread. One path is `/Users/matthewdi/ara/.env` (a hardcoded developer machine path) that will always miss — causing a `stat` + open failure on every launch on every other machine.  
**Fix:** Read env files in a background task from `AppState.init()`, expose them via `@Published` var, and remove the hardcoded developer path. Saves ~5–30 ms on HDD; removes confusing stat failures in Console.

### 5. `SessionRecordingManager.startScreenObserver()` — ScreenCaptureKit IPC

**File:** `AraApp.swift`, lines 347–350  
**Issue:** Setting up an `SCStream` or `AVCaptureSession` requires IPC to `screencaptured`, a TCC check, and pixel-buffer pool allocation — typically 100–400 ms on first use per session.  
**Fix:** Defer `startScreenObserver()` until after the window is visible and the user has interacted (lazy start on first screenshot request).

### 6. `AuthService.configure()` + `SubscriptionService.shared` — eager singleton init

**File:** `AraApp.swift`, lines 257, 260  
**Issue:** Supabase client construction and subscription service materialisation run on the main thread. The Supabase client initialises `URLSession`, registers background task identifiers, and reads stored auth tokens from the keychain — keychain access can stall if the device is locked or Secure Enclave is busy.  
**Fix:** Move both to a background `Task`; defer subscription checks to the first time a gated feature is accessed.

### 7. `FileIndexerService` — no startup guard

**File:** `FileIndexing/FileIndexerService.swift`  
**Issue:** If `FileIndexerService` starts its initial crawl immediately on boot, it competes for I/O bandwidth with the database open and migration. No evidence of a startup delay guard in the code.  
**Fix:** Add a `DispatchQueue.global(qos: .background).asyncAfter(deadline: .now() + 5.0)` before starting the initial file index scan.

---

## Instruments Capture Plan

Since this analysis is static, the following Instruments configuration will verify timing against real hardware:

1. **Time Profiler template** — attach to `AraDesktop` process from cold launch. Look for main-thread stalls >16 ms in `applicationWillFinishLaunching` and `applicationDidFinishLaunching`.
2. **System Calls instrument** — filter by `launchservicesd` Mach messages to measure LS IPC duration.
3. **File Activity instrument** — capture all `read()` / `open()` syscalls during first 3 seconds. Flag any reads from `Application Support/Ara/` legacy paths or `/Users/matthewdi/`.
4. **SQLite Instrument (or custom `os_signpost`)** — add `os_signpost(.begin/.end, log:, name: "DB.init")` around each phase of `performInitialization()` to measure migration vs. pool-open vs. schema-migration time independently.
5. **App Launch template** — measures DYLD load time, `+[NSObject initialize]`, and the `main()` to first-frame duration automatically.

Recommended capture: 10 cold launches (reboot between first and second only), export as `.trace`, compare min/max/mean for the top-5 time-profiler frames.

---

## Prioritized Fix Order

| Priority | Bottleneck | Estimated saving | Effort |
|---|---|---|---|
| P0 | Launch Services IPC → background Task | 150–400 ms | Low (3 lines) |
| P1 | Analytics SDK → deferred 500 ms | 120–250 ms | Low (wrap in asyncAfter) |
| P2 | GRDB legacy migration guard flag | 100–500 ms | Medium (add UserDefaults gate) |
| P3 | SCK startScreenObserver → lazy | 100–400 ms | Medium (add activation trigger) |
| P4 | loadEnvironment → background | 5–30 ms | Low (move to background task) |
| P5 | AuthService/SubscriptionService → lazy | 20–80 ms | Medium (requires lazy singleton) |
| P6 | FileIndexer startup delay | I/O competition | Low (asyncAfter guard) |
