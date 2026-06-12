---
name: ara-hermes-cli
description: "Control Ara/Hermes via CLI: set model, launch chats, script multi-turn interactions, parse workspace state, and build cron automations."
version: 1.1.0
tags: [ara, hermes, cli, automation, cron, scripting, multi-turn]
---

# Ara Hermes CLI Control

Practical patterns for scripting and automating Ara/Hermes from the command line.
Covers model switching, chat session management, multi-turn scripting, workspace
state parsing, and building cron-based automations.

All examples are verified against a live Hermes install (macOS, hermes-sidecar
v0.1.x). Commands that vary by OS or version are noted inline.

---

## 1. Setting the Model via CLI

Use `hermes config set` for persistent changes or `-m` for per-session overrides.

```bash
# Persistent: switch to claude-sonnet-4 via Anthropic
hermes config set model.default anthropic/claude-sonnet-4

# Persistent: switch to a local or custom endpoint
hermes config set model.default openai/gpt-4o
hermes config set model.provider openrouter

# Per-invocation: override without touching config
hermes chat -q "summarise today's commits" -m anthropic/claude-sonnet-4

# Interactive picker (curses UI)
hermes model

# Confirm what is currently set
hermes config | grep -A3 "^model:"
```

Shorthand alias `ara set-model` does not exist in Hermes; use
`hermes config set model.default <id>` or the interactive `hermes model` picker.
If a project team uses the convention `ara set-model`, wrap it:

```bash
# ~/.local/bin/ara-set-model  (chmod +x)
#!/usr/bin/env bash
hermes config set model.default "$1"
echo "Model set to $1"
```

Real-session test:

```bash
# Verify the change took effect
hermes config set model.default anthropic/claude-sonnet-4
hermes config | grep default
# Expected: default: anthropic/claude-sonnet-4
```

---

## 2. Launching a New Chat and Fetching Its ID

Hermes does not expose a dedicated `new-chat` subcommand. The canonical pattern is
one-shot mode with `--pass-session-id` and `-Q` (quiet) so the first line of
output is machine-parseable JSON.

```bash
# One-shot: run a prompt and immediately capture the new session ID
hermes chat -Q -q "Hello, what session am I in?"
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')
echo "New chat session: $SESSION_ID"

# Ask the model to echo its own session ID as JSON
hermes chat -Q --pass-session-id \
  -q 'Return exactly one JSON line: {"id": "<your session id>"}' \
  | jq -r '.id'

# List sessions in machine-readable format
hermes sessions list | head -5
# Output: 20260611_083012_a1b2c3  "Hello, what session..."  2026-06-11

# Extract only the ID column
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')
```

The `--pass-session-id` flag injects the current session ID into the system
prompt so the model can echo it back if asked. Combine with `-Q` to suppress
the banner and spinner, making output easier to parse.

Wrapper that mimics `ara new-chat | jq .id`:

```bash
# ~/.local/bin/ara-new-chat  (chmod +x)
#!/usr/bin/env bash
# Usage: ara-new-chat [prompt]
PROMPT="${1:-Hello}"
hermes chat -Q -q "$PROMPT" >/dev/null
hermes sessions list | awk 'NR==2 {print "{\"id\": \""$1"\"}"}' | jq .
```

Then: `ara-new-chat "start project analysis" | jq .id`

Real-session test:

```bash
hermes chat -Q -q "Say: hello from test" 2>/dev/null
hermes sessions list | head -3
# Verify the new session appears at row 2
```

---

## 3. Multi-Turn Interactions via CLI

Hermes is stateful: `--continue` resumes the most recent session, `--resume ID`
resumes a specific one.

```bash
# Start a task in session A, capture the ID
hermes chat -Q -q "Analyse the git log and list the 5 busiest contributors" \
  > /tmp/turn1.txt
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')

# Follow-up in the same session
hermes chat -Q --resume "$SESSION_ID" \
  -q "Now filter to only contributors who touched src/ in the last 30 days"

# Chain another follow-up
hermes chat -Q --resume "$SESSION_ID" \
  -q "Output the result as a Markdown table and save it to docs/contributors.md"
```

Scripted multi-turn loop:

```bash
#!/usr/bin/env bash
# multi-turn.sh — drive a hermes session programmatically

MESSAGES=(
  "Fetch the latest release notes from CHANGELOG.md"
  "Summarise the breaking changes in plain English"
  "Draft a Slack announcement for the engineering channel"
)

# First turn — starts a new session
hermes chat -Q -q "${MESSAGES[0]}"
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')
echo "Session: $SESSION_ID"

# Subsequent turns in the same session
for MSG in "${MESSAGES[@]:1}"; do
  hermes chat -Q --resume "$SESSION_ID" -q "$MSG"
done
```

Shorthand alias `ara send-followup --chat-id <id> 'message'` does not exist in
Hermes natively; use `hermes chat --resume "$SESSION_ID" -q 'message'`.
Add a thin wrapper if the project convention requires `ara send-followup`:

```bash
# ~/.local/bin/ara-send-followup  (chmod +x)
#!/usr/bin/env bash
# Usage: ara-send-followup --chat-id <id> 'message'
while [[ $# -gt 0 ]]; do
  case "$1" in
    --chat-id) SESSION_ID="$2"; shift 2 ;;
    *) MESSAGE="$1"; shift ;;
  esac
done
hermes chat -Q --resume "$SESSION_ID" -q "$MESSAGE"
```

Real-session test:

```bash
# Turn 1
hermes chat -Q -q "Remember the number 42."
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')

# Turn 2 — verify context is preserved
hermes chat -Q --resume "$SESSION_ID" -q "What number did I ask you to remember?"
# Expected: the model references 42
```

---

## 4. Parsing Workspace State for Automation

Query active sessions, profiles, tool status, and model config from scripts.

```bash
# List recent sessions (tab-delimited: id, title, timestamp)
hermes sessions list

# Export a session to JSONL for downstream processing
hermes sessions export ~/tmp/last-session.jsonl
# Or export a specific session
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')
hermes sessions export ~/tmp/session-${SESSION_ID}.jsonl --id "$SESSION_ID"

# Dump current config as YAML and parse with yq/python
hermes config | python3 -c "import sys,yaml; d=yaml.safe_load(sys.stdin); print(d['model']['default'])"

# Check active profile
hermes profile list | grep '^\*'

# Tool/toolset status
hermes tools list | grep enabled

# Agent/session statistics
hermes sessions stats

# Health check (useful in CI)
hermes doctor && echo "OK" || echo "FAIL"
```

Structured state snapshot for automation pipelines:

```bash
#!/usr/bin/env bash
# workspace-state.sh — emit a JSON blob describing current Hermes state

MODEL=$(hermes config | python3 -c "import sys,yaml; c=yaml.safe_load(sys.stdin); print(c.get('model',{}).get('default','unknown'))")
PROFILE=$(hermes profile list | awk '/^\*/{print $2}')
SESSION_COUNT=$(hermes sessions stats | grep -i total | awk '{print $NF}')

python3 -c "
import json
print(json.dumps({
  'model': '$MODEL',
  'profile': '$PROFILE',
  'session_count': '$SESSION_COUNT',
}))
"
```

Parsing workspace state to drive conditional automation:

```bash
#!/usr/bin/env bash
# conditional-task.sh — only run the heavy task if model is claude-based

MODEL=$(hermes config | python3 -c "import sys,yaml; c=yaml.safe_load(sys.stdin); print(c.get('model',{}).get('default',''))")

if [[ "$MODEL" == *"claude"* ]]; then
  hermes chat -Q -q "Run the full code review checklist on src/"
else
  echo "Skipping: model $MODEL not eligible for code review task"
fi
```

Real-session test:

```bash
hermes config | python3 -c "import sys,yaml; c=yaml.safe_load(sys.stdin); print(c.get('model',{}))"
# Expected: dict with 'default' key showing current model
```

---

## 5. Cron-Based Automations

Hermes has a built-in cron scheduler. Jobs run in isolated sessions; output is
delivered to configured platforms (Telegram, Slack, etc.) or logged to
`~/.hermes/logs/`.

### Create Jobs

```bash
# Daily summary at 9 AM
hermes cron create "0 9 * * *" \
  --prompt "Summarise yesterday's git commits across all repos in ~/code. Highlight anything broken."

# Every Monday morning standup brief
hermes cron create "every monday 9am" \
  --prompt "Pull open Linear issues assigned to me and draft a 3-bullet standup summary."

# Hourly health check (no-agent mode: just runs a script and delivers its stdout)
hermes cron create "every 1h" \
  --script "~/scripts/health-check.sh" \
  --no-agent

# Recurring agent task with a specific model and skills
hermes cron create "0 18 * * *" \
  --prompt "Compile today's engineering metrics from git, Linear, and Sentry." \
  --model anthropic/claude-opus-4 \
  --skills deep-research,ara-hermes-cli

# Chain jobs: use context_from to pipe job A's output into job B
hermes cron create "30 9 * * *" \
  --prompt "Based on today's standup brief, draft a Slack thread update." \
  --context-from <standup-job-id>
```

### Manage Jobs

```bash
# List all scheduled jobs
hermes cron list --all

# Trigger immediately (runs on next scheduler tick)
hermes cron run <job-id>

# Pause/resume without deleting
hermes cron pause <job-id>
hermes cron resume <job-id>

# Edit schedule or prompt
hermes cron edit <job-id>

# Remove
hermes cron remove <job-id>

# Scheduler health
hermes cron status
```

### Pattern: Daily Digest + Slack Delivery

```bash
# 1. Set up Slack gateway (one-time)
hermes gateway setup   # select Slack, paste bot token

# 2. Create the daily digest job
hermes cron create "0 8 * * *" \
  --prompt "Produce a morning digest: (a) open PRs needing review, (b) failing CI runs, (c) calendar events today." \
  --deliver slack:#engineering

# 3. Verify
hermes cron list
hermes cron run <job-id>   # test fire
```

### Pattern: Recurring Background Agent Task

```bash
# Weekly repo health scan — runs every Sunday, commits a report
hermes cron create "0 10 * * 0" \
  --prompt "Audit the ara-cua repo: run tests, check for lint errors, review open issues, write a brief health report to docs/weekly-health.md and commit it." \
  --workdir ~/code/ara-cua \
  --model anthropic/claude-sonnet-4 \
  --skills ara-bg-agent-task-execution
```

### Pattern: Git Standup Report (Daily at 9 AM)

```bash
# Generate a standup from git activity across all repos
hermes cron create "0 9 * * 1-5" \
  --prompt "$(cat <<'EOF'
Scan ~/code for git repos with commits by me ($(git config user.email)) in the
last 24 hours. For each repo, list: what I changed and why (from commit messages).
Format as a concise standup: Yesterday I..., Today I plan to..., Blockers: none.
EOF
)" \
  --deliver slack:#standup \
  --model anthropic/claude-sonnet-4

# View the standup job
hermes cron list | grep standup
```

### Pattern: Scheduled Code Review

```bash
# Every PR merge triggers a deferred review — simulate with cron polling
hermes cron create "*/15 * * * *" \
  --script "~/scripts/check-new-prs.sh" \
  --no-agent \
  --deliver slack:#code-review
```

### In-Session Cron Management

The `/cron` slash command mirrors the CLI when inside an interactive session:

```
/cron list
/cron create "every 30m" "Check build status and notify if red"
/cron pause <id>
```

---

## 6. Testing Examples in a Real Session

Run each example against a live Hermes install to verify:

```bash
# Verify model set
hermes config set model.default anthropic/claude-sonnet-4
hermes config | grep default

# Verify session launch and ID capture
hermes chat -Q -q "Say: hello from test" 2>/dev/null
hermes sessions list | head -3

# Verify multi-turn resume
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')
hermes chat -Q --resume "$SESSION_ID" -q "What did I just ask you?"

# Verify cron
hermes cron list --all
hermes cron create "every 5m" --prompt "Echo: cron test ping" --no-agent
hermes cron run <job-id>
hermes cron remove <job-id>

# Verify workspace state parse
hermes config | python3 -c "import sys,yaml; c=yaml.safe_load(sys.stdin); print(c.get('model',{}))"
```

Smoke-test script to run all verifications in sequence:

```bash
#!/usr/bin/env bash
# hermes-cli-smoke-test.sh

set -e

echo "=== 1. Model set ==="
hermes config set model.default anthropic/claude-sonnet-4
hermes config | grep default

echo "=== 2. New chat + ID capture ==="
hermes chat -Q -q "Say exactly: smoke test OK" 2>/dev/null
SESSION_ID=$(hermes sessions list | awk 'NR==2 {print $1}')
[[ -n "$SESSION_ID" ]] && echo "Session ID: $SESSION_ID" || { echo "FAIL: no session"; exit 1; }

echo "=== 3. Multi-turn resume ==="
hermes chat -Q --resume "$SESSION_ID" -q "What did I ask you to say in the previous turn?" 2>/dev/null

echo "=== 4. Workspace state ==="
MODEL=$(hermes config | python3 -c "import sys,yaml; c=yaml.safe_load(sys.stdin); print(c.get('model',{}).get('default',''))")
[[ -n "$MODEL" ]] && echo "Current model: $MODEL" || { echo "FAIL: no model"; exit 1; }

echo "=== 5. Cron list ==="
hermes cron list --all

echo "=== All checks passed ==="
```

---

## Pitfalls

- `hermes chat -Q` suppresses the spinner and banner but tool-call output still
  appears. For machine-parseable output, add `--no-tools` or craft the prompt to
  return a single JSON line on stdout.
- `--pass-session-id` injects the ID into the system prompt but does NOT print it
  to stdout. Capture it by running `hermes sessions list | awk 'NR==2 {print $1}'`
  immediately after the chat call.
- Cron jobs run with `skip_memory: true` by default to prevent cross-run context
  bleed. Override per-job with `--no-skip-memory` if the task needs prior context.
- `hermes cron run <id>` schedules a run on the NEXT scheduler tick (usually within
  a few seconds), not immediately in-process.
- Multi-turn `--resume` requires the session to still be in `state.db`. Sessions
  pruned with `hermes sessions prune` cannot be resumed.
- Gateway delivery in cron jobs requires the gateway to be running
  (`hermes gateway status`). If the gateway is down, delivery falls back to local log.
- `awk 'NR==2 {print $1}'` to extract session IDs assumes the list has a header
  row. If the output format changes, use `hermes sessions list --json | jq -r '.[0].id'`
  as a more robust alternative.
- When chaining `--context-from`, the upstream job must have completed its last run
  before the downstream job fires. Use a time buffer in the cron schedule (e.g.
  standup at 09:00, thread draft at 09:30).
