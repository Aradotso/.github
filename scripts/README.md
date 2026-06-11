# scripts/

Local scripts used by CI workflows.

## validate-profile.sh

Validates the org profile (`profile/`) for:

- **Logo & hero image**: file size and pixel-width constraints
- **Social links**: HTTP 2xx reachability check for every URL in `profile/README.md`
- **README markup**: all local `<img src="./...">` refs resolve; at least one heading present
- **CHANGELOG.md**: exists at repo root and was modified within the last 90 days

On failure the script exits with code 1 and prints a list of errors.

### Slack notifications

Set the `SLACK_PROFILE_WEBHOOK_URL` repository secret to an incoming-webhook URL and the script will POST a Block Kit message to that channel whenever the scheduled run finds drift.

### Running locally

```bash
bash scripts/validate-profile.sh
```
