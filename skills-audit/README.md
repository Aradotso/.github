# Bundled Skills Audit — 2026-06-11

Inventory and compliance report for all skills shipped inside
`Ara 2.app/Contents/Resources/Ara_Ara.bundle/BundledSkills/`.

Audit run: 2026-06-11. Bundle timestamp: 2026-05-14 15:07.

---

## Summary

17 `.skill.md` files audited.

All 17 pass format compliance (YAML frontmatter present, `name` and `description` fields populated, markdown body follows).
All 17 are present in the live Hermes skill library and are byte-for-byte identical — no drift detected.
No skills require updates at this time.

---

## Inventory

| Skill | Category | Lines | Frontmatter Fields | Live Library Status |
|---|---|---|---|---|
| `ai-browser-profile` | integrations | 47 | name, description | In sync |
| `canvas-design` | productivity | 129 | name, description, license | In sync |
| `deep-research` | productivity | 856 | name, description | In sync |
| `doc-coauthoring` | documents | 375 | name, description | In sync |
| `docx` | documents | 481 | name, description, license | In sync |
| `find-skills` | productivity | 148 | name, description | In sync |
| `frontend-design` | productivity | 42 | name, description, license | In sync |
| `google-workspace-setup` | integrations | 132 | name, description, version | In sync |
| `pdf` | documents | 314 | name, description, license | In sync |
| `pptx` | documents | 232 | name, description, license | In sync |
| `social-autoposter` | integrations | 302 | name, description, user_invocable | In sync |
| `social-autoposter-setup` | integrations | 274 | name, description | In sync |
| `telegram` | integrations | 203 | name, description | In sync |
| `travel-planner` | productivity | 534 | name, description | In sync |
| `video-edit` | media | 105 | name, description | In sync |
| `web-scraping` | media | 58 | name, description | In sync |
| `xlsx` | documents | 232 | name, description, license | In sync |

---

## Format Compliance

All 17 files follow the required format:

- YAML frontmatter delimited by `---` at file start
- `name` field present and matches filename (without `.skill.md`)
- `description` field present; trigger phrases embedded inline in the description (no separate `triggers` key — this is the accepted pattern for bundled skills)
- Markdown body follows immediately after the closing `---`

Optional fields in use: `license` (6 skills), `user_invocable` (1 skill), `version` (1 skill). All are valid and recognized by the skill loader.

---

## Categorization

Skills are organized into four functional categories in the live library:

**documents** (5): docx, pdf, pptx, xlsx, doc-coauthoring

**productivity** (5): canvas-design, deep-research, find-skills, frontend-design, travel-planner

**integrations** (5): ai-browser-profile, google-workspace-setup, social-autoposter, social-autoposter-setup, telegram

**media** (2): video-edit, web-scraping

---

## Deprecation Check

No bundled skills are deprecated. Cross-referencing against the live Hermes skill index (148 active skills as of 2026-06-11):

- No bundled skill name appears in any archived or disabled entry
- No bundled skill has been superseded by a newer skill with a different name
- `web-scraping` and `frontend-design` are the lightest skills (58 and 42 lines respectively); their brevity is intentional — they serve as entry points that delegate to tool-specific instructions

---

## Sync Protocol

Bundled skills are shipped read-only inside the `.app` bundle. They are copied into
`~/Library/Application Support/Ara/hermes-sidecar/skills/<category>/<skill>/SKILL.md`
on first install or when Ara detects the live copy is absent.

To update a bundled skill in a release:
1. Edit the `.skill.md` file in the Xcode project under `Ara_Ara/BundledSkills/`
2. The build step copies it into the bundle at `Ara_Ara.bundle/BundledSkills/`
3. On next app launch, Ara detects version mismatch and re-copies to the live library

Manual overrides by the user in the live library are **not** overwritten by app updates — the live library takes precedence once a skill has been customized.

---

## Next Review

Schedule next audit when the app bundle version bumps past `v0.1.132.12-macos` or after 60 days (2026-08-11), whichever comes first.
