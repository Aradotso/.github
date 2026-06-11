# Skill Audit: `ara-project-brain-generate-suggestions`

**Audit date**: 2026-06-11
**Skill location**: `infra/ara-project-brain-generate-suggestions/SKILL.md`
**Companion skill**: `devops/project-brain-synthesis-generate-chat-suggestions/SKILL.md`

## What was tested

The skill workflow was run against the live ara-cua project at `~/ara-experiments/ara-cua` (version `0.1.56`). Git history, branch list, plans/, learnings/, untracked files, and the ara-cua-context.md reference were evaluated for accuracy and completeness.

## Verdict: Skill is structurally sound, context references are stale

The core synthesis algorithm (gather → identify → rank → construct → emit) is correct and well-specified. The JSON Lines output format, confidence scoring rubric, and pitfalls section are all solid. The issue is that the supporting reference files encode ara-cua project state from early June 2026 that is now outdated, and two architectural gaps exist in the main SKILL.md.

## Gaps found

### 1. Missing `OpenAra/` subproject (HIGH)

Both context files (`ara-cua-heuristics.md` and `ara-cua-context.md`) describe the project as having three subprojects: AraDesktop, AraWeb, and chat.ara.so. The real repo now has a fourth active subproject, `OpenAra/` (the open-source CUA brain, will be npm-published as `open-cua`). It is untracked in git status and actively developed. Brain sweeps that don't know about OpenAra will miss a significant signal source and generate suggestions that ignore it entirely.

**Fix**: Add `OpenAra/` to the context reference and assign it a commit prefix.

### 2. Stale active work streams in ara-cua-context.md (HIGH)

The context file lists active work streams as of June 7, 2026. The real git log (as of June 11, 2026) shows completely different active areas:

- `notch/maxview` UI redesign (header, archive/resume, hover-aware threads)
- `acp-bridge` cursor tint forwarding to Codex/opencode/cursor
- `ci/auto-release` tuning (cron from */30 to */15)
- `session-replay` viewer + list/manifest endpoints
- Multiple active feature branches: `feat/cua-non-intrusive-workspace`, `feat/hard-paywall-toggle`, `feat/onboarding-watch-me-drive-demos`, `feat/simplify-pricing`

None of these appear in the context reference. A brain sweep using the stale context will suggest work from the previous sprint rather than the current one.

**Fix**: Update `ara-cua-context.md` work streams to reflect post-0.1.50 state.

### 3. Commit prefix format mismatch (MEDIUM)

The SKILL.md and context reference say to look for `(AraDesktop)` parenthetical prefix format to identify active subprojects. But the real commit log uses bare lowercase keywords: `notch/maxview:`, `observability:`, `ci(auto-release):`, `acp-bridge:`, `release:`. The parenthetical prefix is used for workspace-level commits but not for most feature work. A skill that looks only for `(AraDesktop)` commits will miss the bulk of the signal.

**Fix**: Note that this repo uses both formats. Keyword-based prefixes (no parens) are the dominant pattern in recent history.

### 4. `plans/` folder is stale for signal extraction (MEDIUM)

The SKILL.md says to check `plans/` for pre-vetted follow-up work. The actual `plans/` folder only contains docs from 2026-05-04 and 2026-05-05. These are design docs for completed work (OpenAra rebrand, auth custom domain, brand polish). Treating these as forward signals will generate wrong suggestions.

**Current signal sources that work better**:
- Active git branches (14 open feature/canary/ci branches)
- Untracked directories: `OpenAra/`, `scripts/`, `AraWeb/emails/`
- `learnings/` folder has more recent context than `plans/`

**Fix**: Add a note that `plans/` may be stale; cross-check branch names as a stronger signal source.

### 5. Confidence cap not explicit in main SKILL.md (LOW)

The `ara-cua-heuristics.md` reference shows a scoring example where boosts sum to 0.98 and then get capped at 0.76. But the main SKILL.md has no explicit rule about a confidence cap or anti-inflation guard. An agent reading only the main skill could legitimately score a suggestion at 0.99 by accumulating boosts.

**Fix**: Add an explicit anti-inflation rule to the main SKILL.md: raw boost totals above a threshold should be capped, and the rationale for the cap should be documented.

### 6. No version field in frontmatter (LOW)

The `ara-project-brain-generate-suggestions` skill has no `version:` field. The companion skill (`project-brain-synthesis-generate-chat-suggestions`) has `version: 1.0`. Without versioning, it's impossible to tell which copy is authoritative or when it was last reviewed.

**Fix**: Add `version: 1.1` to signal this reviewed/patched iteration.

### 7. Bundled skills assessment: Not suitable for consumer bundle (FINDING)

The `~/Downloads/Misc/Ara 2.app/Contents/Resources/Ara_Ara.bundle/BundledSkills/` directory contains general-purpose consumer-facing skills (canvas-design, deep-research, docs, video-edit, etc.). The `ara-project-brain-generate-suggestions` skill is a developer/power-user workflow tightly coupled to the ara-cua project structure, Sentry org slugs, PostHog event names, and Sven's personal preferences. It is NOT a good candidate for the consumer bundle. It should remain as a private profile skill.

## Session search performance

Session search responses are fast (< 2s for limit=5 queries). No performance issues observed. The existing pitfall about `>200KB` truncation is correct and the mitigation (extract metadata from summary) is good practice.

## Recommendation

1. Patch the main SKILL.md: add version, explicit confidence cap rule, note on dual commit prefix formats, note on stale plans/ fallback.
2. Update `ara-cua-context.md`: add OpenAra subproject, replace June 7 work streams with June 11 state.
3. Do NOT add to bundled skills — this skill is project-specific, not consumer-facing.

Patches have been applied directly to the live skill files as part of this audit.
