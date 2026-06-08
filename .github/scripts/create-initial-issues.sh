#!/usr/bin/env bash
set -euo pipefail

# Check if gh CLI is installed and authenticated
if ! command -v gh &> /dev/null; then
  echo "Error: gh CLI is not installed." >&2
  exit 1
fi

if ! gh auth status &> /dev/null; then
  echo "Error: gh CLI is not authenticated. Please run 'gh auth login' first." >&2
  exit 1
fi

echo "Creating initial triage labels..."
# Create labels from our yaml spec if gh label exists
# Fallback to direct creation
gh label create bug --color "d73a4a" --description "Something isn't working" --force || true
gh label create enhancement --color "a2eeef" --description "New feature or request" --force || true
gh label create triage --color "fbca04" --description "Needs review and prioritization" --force || true
gh label create p1 --color "e11d21" --description "High priority issue" --force || true
gh label create p2 --color "f9d0c4" --description "Medium priority issue" --force || true
gh label create p3 --color "cccccc" --description "Low priority issue" --force || true
gh label create worktree --color "bfd4f2" --description "Related to git worktrees, background agent slots, or repo syncing" --force || true
gh label create gateway --color "1d76db" --description "Related to API Gateway routing, headers, or communication" --force || true
gh label create cua --color "006b75" --description "Computer Use Agent desktop, multi-display, or scale optimization" --force || true
gh label create suggestions --color "c5def5" --description "Contextual New Chat suggestions and synthesis engine" --force || true

echo "Creating roadmap issues..."

gh issue create \
  --title "[FEATURE] Implement Lazy-Created git worktrees in desktop UI" \
  --body "Delay git worktree creation until the first chat prompt is submitted or when a background task actually triggers. This eliminates upfront workspace preparation latency." \
  --label "enhancement,worktree,p1,triage"

gh issue create \
  --title "[FEATURE] Proactive 'New Chat' suggestion engine synthesis" \
  --body "Create a background daemon that synthesizes recent workspace signals, git diffs, session history, and user memories to formulate actionable starting prompt cards for a new session." \
  --label "enhancement,suggestions,p2,triage"

gh issue create \
  --title "[BUG] Custom scaling omissions on multi-display sweep-display-sizes" \
  --body "Address situations where scaling is native (scaling:off) or completely omitted in displayplacer lists. Robustly parse the scaling output to prevent coordinate calculation mismatches in browser automation." \
  --label "bug,cua,p1,triage"

gh issue create \
  --title "[FEATURE] Validate and sanitize custom conversation ID headers in AraWeb Gateway" \
  --body "Ensure x-ara-conversation-id header is correctly propagated from AnthropicMessagesClient/Sender, checking that any special value keys are correctly validated as UUIDs to prevent log spoofing or injection." \
  --label "enhancement,gateway,p2,triage"

echo "All tasks successfully registered."
