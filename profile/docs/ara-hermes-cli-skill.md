# ara-hermes-cli Skill

This document describes the new `ara-hermes-cli` skill added to the Ara/Hermes
skill library. The skill provides scripting patterns and automation recipes for
controlling Hermes from the command line.

## What it covers

1. **Setting the model** — `hermes config set model.default <id>` for persistent
   changes; `-m <id>` per-invocation override; `hermes model` interactive picker.

2. **Launching a new chat and capturing its ID** — one-shot mode with `-Q` and
   `--pass-session-id`; extracting the session ID from `hermes sessions list`.

3. **Multi-turn scripted interactions** — `hermes chat --resume <id> -q <msg>` to
   chain follow-up turns; a reusable `multi-turn.sh` wrapper for looping over a
   message array in the same session.

4. **Parsing workspace state** — `hermes config`, `hermes sessions stats`,
   `hermes profile list`, `hermes tools list`; a `workspace-state.sh` snippet that
   emits a JSON blob with model, profile, and session count.

5. **Cron-based automations** — `hermes cron create` with duration, "every" phrase,
   and 5-field cron schedules; patterns for daily digests delivered to Slack,
   recurring agent tasks that commit to a repo, and job chaining via `--context-from`.

6. **Testing examples** — a checklist of one-liners that verify each feature against
   a live Hermes install.

## Skill location

The skill is installed at:
`~/Library/Application Support/Ara/hermes-sidecar/skills/workflow-management/ara-hermes-cli/SKILL.md`

## Notes

- The CLI commands in this skill are grounded in the Hermes Agent `hermes-agent`
  base skill (v2.1.0) and verified against the Hermes CLI reference.
- `ara set-model` and `ara send-followup --chat-id` are not native Hermes commands.
  The skill provides thin shell wrapper patterns for teams that adopt that convention.
- Cron delivery to Slack/Telegram requires the gateway to be configured and running.
