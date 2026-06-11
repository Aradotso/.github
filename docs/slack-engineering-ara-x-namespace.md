# Slack post for #engineering — `ara x` experimental namespace

**Channel:** #engineering
**Author:** Sven / Ara bot
**Status:** Ready to post (paste the block below)

---

## Draft post

Hey team 👋 — there's a hidden experimental CLI namespace baked into the AraDesktop bundle that you can now use for local development and debugging. Sharing the details here so anyone scripting against the running app can give it a spin and tell us what's missing.

**How to enable:** set `ARA_CLI_EXPERIMENTAL=1` in your shell before running any `ara x` subcommand. Without it every subcommand (except `ara x help`) exits with a usage error. The namespace is intentionally hidden from `ara --cli-help` so it doesn't clutter the stable surface.

```
export ARA_CLI_EXPERIMENTAL=1
```

**Subcommands**

`ara x control <command> [--json]`
Generic passthrough to any `com.ara.control` distributed notification. Today's handlers: `getState`, `dumpAutosuggest`, `generateSuggestions`, `runBuilds`, `setAutosuggestEnabled`, `discardBuild`. Anything unrecognised is posted and silently dropped by the app (shows in console as "unknown command"), so this stays forward-compatible as new handlers land.

```
ara x control getState --json
ara x control runBuilds --project MyProject --enabled true
```

`ara x doctor [--json]`
Readiness probe. Checks that the app is running, the Hermes sidecar is reachable, resolves the effective user + DB path, and exits non-zero if anything is missing. Good first step before scripting against the running app.

```
ara x doctor
# app: running | hermes: ok (http://127.0.0.1:8765) | user: <uid> (UserDefaults) | db: /.../.../ara.db (present)
```

`ara x tail [--session …] [--task …] [--since …] [--limit N] [--json]`
Live-streams new `chat_messages` rows (user + ai sides) until Ctrl-C. WAL-safe, reads the same `ara.db` the GUI uses. With `--json` emits one compact JSON object per line for `while read` / `jq` consumers.

```
ara x tail --json | jq .messageText
```

`ara x sql "SELECT …" [--limit N] [--json]`
Read-only single `SELECT` or `WITH` against the per-user `ara.db`. Prefix-checked (must start `SELECT` or `WITH`), no semicolons, runs inside a GRDB read transaction. Same DB + user resolution as `ara hermes`.

```
ara x sql "SELECT session_id, COUNT(*) n FROM chat_messages GROUP BY session_id ORDER BY n DESC LIMIT 5" --json
```

`ara x wait [--timeout N] [--json]`
Blocks until the in-flight turn settles (`isAILoading` + `isStreaming` both false), then exits 0. Default timeout 60 s (exit 3 on timeout). Prompt-agnostic; pair with `ara chat` when you want to wait on a specific prompt.

```
ara chat "explain the diff" && ara x wait && echo "done"
```

`ara x history [--task <routine-id>] [--limit N] [--json]`
Reads local chat rows produced by a scheduled routine (`taskId LIKE routine-%`). Different from `ara hermes runs <id>` (which reads sidecar output files) — this reads the actual AI reply text from the DB.

```
ara x history --limit 5 --json
```

**Caveats**
This namespace is **unsupported and volatile**. Subcommand signatures, output formats, and the env flag may change or disappear in any build. Don't put `ara x` calls in shared CI or anything another person depends on without checking first. If a subcommand hangs or crashes, `Ctrl-C` is always safe (the app is unaffected — we only read the DB and post notifications).

Happy to harden or promote any of these to the stable surface if they're actually useful. Drop reactions or replies here and I'll spin up a followup design chat.

---

## Followup chat setup

**Recurring prompt (paste into Ara "New Agent" / cron):**

```
Check #engineering Slack (or the ara-cua repo PRs) for any new reactions, replies, or issues related to the `ara x` experimental CLI namespace post. Summarise new feedback in a bullet list, flag any crash reports or format-change requests as high priority, and draft a response thread if needed. Then propose concrete changes to any affected subcommands (control / doctor / tail / sql / wait / history).
```

**Suggested cadence:** every Monday until the namespace is either promoted to stable or explicitly retired.
