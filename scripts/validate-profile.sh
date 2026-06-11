#!/usr/bin/env bash
# validate-profile.sh
# Validates the Aradotso org profile for:
#   - Logo/hero image dimensions and file size
#   - Social links returning 2xx
#   - README.md markup (no broken image refs, required sections present)
#   - CHANGELOG.md presence and recency
#
# Exit codes:
#   0  – all checks passed
#   1  – one or more checks failed (details printed to stdout)
#
# Environment variables:
#   SLACK_WEBHOOK_URL   – if set, a summary is POSTed to Slack on failure
#   GITHUB_TOKEN        – used by the caller to file issues via `gh`
#   REPO                – owner/repo, e.g. "Aradotso/.github"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PROFILE_DIR="$REPO_ROOT/profile"

FAILED=0
ERRORS=()

log_error() {
  echo "[FAIL] $1"
  ERRORS+=("$1")
  FAILED=1
}

log_ok() {
  echo "[OK]   $1"
}

# ── 1. Image checks ─────────────────────────────────────────────────────────

check_image() {
  local file="$1"
  local label="$2"
  local max_kb="${3:-500}"
  local min_w="${4:-0}"
  local max_w="${5:-99999}"

  if [[ ! -f "$file" ]]; then
    log_error "$label not found at $file"
    return
  fi

  local size_kb
  size_kb=$(du -k "$file" | awk '{print $1}')
  if (( size_kb > max_kb )); then
    log_error "$label is ${size_kb}KB — exceeds ${max_kb}KB limit"
  else
    log_ok "$label size: ${size_kb}KB (≤${max_kb}KB)"
  fi

  # Width check via Python (ships with macOS/Ubuntu runners)
  if command -v python3 &>/dev/null; then
    local width
    width=$(python3 - "$file" <<'PYEOF'
import sys, struct, zlib, pathlib

def png_width(path):
    data = pathlib.Path(path).read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    w = struct.unpack('>I', data[16:20])[0]
    return w

def jpeg_width(path):
    data = pathlib.Path(path).read_bytes()
    i = 0
    while i < len(data) - 1:
        if data[i] != 0xFF:
            break
        marker = data[i+1]
        if marker in (0xC0, 0xC1, 0xC2):
            return struct.unpack('>H', data[i+7:i+9])[0]
        elif marker in (0xD8, 0xD9, 0x01):
            i += 2
        else:
            length = struct.unpack('>H', data[i+2:i+4])[0]
            i += 2 + length
    return None

p = sys.argv[1]
if p.lower().endswith('.png'):
    w = png_width(p)
elif p.lower().endswith(('.jpg', '.jpeg')):
    w = jpeg_width(p)
else:
    w = None
print(w if w is not None else 0)
PYEOF
)
    if [[ "$width" -gt 0 && ("$width" -lt "$min_w" || "$width" -gt "$max_w") ]]; then
      log_error "$label width is ${width}px — expected ${min_w}–${max_w}px"
    elif [[ "$width" -gt 0 ]]; then
      log_ok "$label width: ${width}px (range ${min_w}–${max_w}px)"
    fi
  fi
}

check_image "$PROFILE_DIR/logo.png"  "logo.png"  200  64  512
check_image "$PROFILE_DIR/hero.png"  "hero.png"  800 640 3840

# ── 2. Social / link checks ─────────────────────────────────────────────────

check_url() {
  local url="$1"
  local label="${2:-$url}"
  local http_code
  http_code=$(curl -o /dev/null -s -L --max-time 10 -w "%{http_code}" "$url" || echo "000")
  if [[ "$http_code" =~ ^2 || "$http_code" == "301" || "$http_code" == "302" ]]; then
    log_ok "Link $label → $http_code"
  else
    log_error "Link $label returned $http_code (url: $url)"
  fi
}

# Extract URLs from README and check them
README="$PROFILE_DIR/README.md"
if [[ -f "$README" ]]; then
  # Grab href= and src= values that look like http(s)
  mapfile -t LINKS < <(grep -oE 'https?://[^"'"'"' >)]+' "$README" || true)
  if [[ ${#LINKS[@]} -eq 0 ]]; then
    log_error "README.md contains no social/web links"
  else
    for link in "${LINKS[@]}"; do
      check_url "$link" "$link"
    done
  fi
else
  log_error "profile/README.md not found"
fi

# ── 3. README markup checks ─────────────────────────────────────────────────

if [[ -f "$README" ]]; then
  # Ensure every <img src="./..."> actually exists on disk
  while IFS= read -r imgpath; do
    local_path="$PROFILE_DIR/$imgpath"
    if [[ ! -f "$local_path" ]]; then
      log_error "README references missing image: $imgpath"
    else
      log_ok "README image exists: $imgpath"
    fi
  done < <(grep -oE 'src="\./[^"]+' "$README" | sed 's|src="\.\/||' || true)

  # Must have at least one heading or meaningful content
  if ! grep -qE '^\s*<h[1-6]|^#{1,6} ' "$README"; then
    log_error "README.md has no headings"
  else
    log_ok "README.md has headings"
  fi
else
  log_error "profile/README.md not found"
fi

# ── 4. CHANGELOG.md checks ──────────────────────────────────────────────────

CHANGELOG="$REPO_ROOT/CHANGELOG.md"
if [[ ! -f "$CHANGELOG" ]]; then
  log_error "CHANGELOG.md not found at repo root"
else
  log_ok "CHANGELOG.md exists"

  # Check that it was modified within the last 90 days
  if command -v python3 &>/dev/null; then
    local_days=$(python3 -c "
import os, time
mtime = os.path.getmtime('$CHANGELOG')
days = (time.time() - mtime) / 86400
print(int(days))
")
    if (( local_days > 90 )); then
      log_error "CHANGELOG.md has not been updated in ${local_days} days (threshold: 90)"
    else
      log_ok "CHANGELOG.md last updated ${local_days} days ago"
    fi
  fi
fi

# ── 5. Report & notify ───────────────────────────────────────────────────────

echo ""
if [[ "$FAILED" -eq 0 ]]; then
  echo "All profile checks passed ✓"
  exit 0
fi

echo "Profile validation FAILED with ${#ERRORS[@]} error(s):"
for err in "${ERRORS[@]}"; do
  echo "  • $err"
done

# Post to Slack if webhook is configured
if [[ -n "${SLACK_WEBHOOK_URL:-}" ]]; then
  PAYLOAD=$(python3 -c "
import json, sys
errors = sys.argv[1:]
blocks = [{'type':'section','text':{'type':'mrkdwn','text':'*:warning: Org profile drift detected in Aradotso/.github*'}}]
for e in errors:
    blocks.append({'type':'section','text':{'type':'mrkdwn','text':':x: ' + e}})
blocks.append({'type':'context','elements':[{'type':'mrkdwn','text':'Run <https://github.com/Aradotso/.github/actions|GitHub Actions> to see the full log.'}]})
print(json.dumps({'blocks': blocks}))
" "${ERRORS[@]}")
  curl -s -X POST -H 'Content-type: application/json' --data "$PAYLOAD" "$SLACK_WEBHOOK_URL"
fi

exit 1
