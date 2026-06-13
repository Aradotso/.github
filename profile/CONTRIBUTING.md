# Contributing to the Ara profile

This repository backs the public GitHub organization profile shown from
`profile/README.md`. Treat it as a published surface for Ara, not as a
scratchpad. Every profile change should be traceable to a canonical source,
validated locally, and reviewed before it reaches `main`.

## Profile source of truth

The GitHub profile is synced from canonical Ara sources rather than edited
from memory. Use the current public copy on [ara.so](https://www.ara.so) for
external messaging, links, product positioning, and brand language. Use
approved internal docs for private rollout notes, launch timing, team
membership, partner references, or anything not yet public.

When a profile update is requested, first identify the canonical source that
justifies it. Prefer copying exact language from ara.so for public claims. If
an internal doc is the only source, keep the profile wording public-safe.
Remove implementation details, roadmap dates, customer names, or unreleased
feature names unless they are already approved for publication.

A normal sync flow is:

1. Check the canonical public page or approved internal doc that owns the
   update.
2. Update `profile/README.md` and any local assets in `profile/`.
3. Keep generated or compressed assets committed only when they are the final
   public artifact.
4. Run the local validation steps below.
5. Open a PR for review instead of pushing directly to `main`.

Background agents should follow the repository documentation workflow captured
in the `ara-bg-agent-write-repo-docs` skill. Related patterns also live in
`background-coding-workflows`, especially the profile README, badge, branding,
and image-optimization references.

## Health-check rules

Profile health checks catch changes that make the organization profile look
broken on GitHub. They should stay conservative and easy to reproduce locally.

Logo and image validation:

- `profile/logo.png` must remain square, at least 256x256, and small enough
  for fast GitHub rendering. The current target is 512x512.
- `profile/hero.png` should remain landscape, use the approved Ara brand
  treatment, and avoid text that becomes unreadable on narrow screens.
- Referenced local images in `profile/README.md` must exist in `profile/` and
  should use relative paths such as `./logo.png`.
- Image alt text must describe the Ara brand or graphic and should not be
  empty.

Social-link validation:

- Public links in the README should use HTTPS.
- The canonical website link is `https://www.ara.so` unless the source of
  truth explicitly changes.
- Avoid adding personal social links, private docs, staging links, or tracking
  URLs to the public profile.
- If a new social or community link is added, verify that the destination is
  public and controlled by Ara.

Markdown validation:

- The README must render cleanly on GitHub, including embedded HTML blocks used
  for centered layout.
- Links must not be broken or point to local-only files outside `profile/`.
- Markdown should pass linting with a practical GitHub profile configuration.
  Inline HTML is allowed when it is needed for alignment or image sizing.
- Keep headings, image widths, and link labels consistent with the existing
  profile style.

## Run validation locally

For a docs-only profile update, do not run unrelated application builds.
Validate the files that GitHub will render.

Run Markdown linting when Node tooling is available:

```sh
npx --yes markdownlint-cli2 "profile/**/*.md"
```

If inline HTML rules need to be relaxed for the profile layout, use the same
lint configuration as CI or run the equivalent local command from the workflow.
Do not silence a real broken link or missing asset by disabling a rule globally.

Run a lightweight asset and link check from the repository root:

```sh
python3 - <<'PY'
from pathlib import Path
import re
from PIL import Image

profile = Path('profile')
readme = profile / 'README.md'
text = readme.read_text()
for src in re.findall(r'<img[^>]+src="([^"]+)"', text):
    if src.startswith('./'):
        path = profile / src[2:]
        assert path.exists(), f'missing image: {src}'
        with Image.open(path) as image:
            width, height = image.size
        if path.name == 'logo.png':
            assert width == height, 'logo.png must be square'
            assert width >= 256, 'logo.png must be at least 256px wide'
        if path.name == 'hero.png':
            assert width > height, 'hero.png should be landscape'
for href in re.findall(r'href="([^"]+)"', text):
    assert href.startswith('https://'), f'non-HTTPS link: {href}'
assert 'https://www.ara.so' in text, 'canonical ara.so link missing'
print('profile validation passed')
PY
```

If Pillow is not installed locally, install it in a temporary environment or
use the image-size check provided by CI. Do not commit local virtualenv files or
generated caches.

## CI, CD, and approvals

PRs into `main` should run profile health checks before merge. The expected CI
flow is Markdown linting, asset validation, link validation, and any
repository-specific sync check that confirms the profile still matches the
canonical public or internal source.

The approval flow is:

1. Contributor opens a PR with the source of truth linked in the description
   when possible.
2. CI validates Markdown, image dimensions, local image references, and public
   social links.
3. A maintainer reviews brand voice, public-safety, and whether the source of
   truth is authoritative.
4. Brand-sensitive updates such as a new logo, hero image, tagline, or launch
   messaging require approval from the owner of the canonical ara.so or
   internal-doc source.
5. After merge to `main`, GitHub renders the updated profile from
   `profile/README.md`. If the profile looks wrong after merge, revert quickly
   and follow up with a smaller corrected PR.

Background agents should not push directly to `main`. They should work on a
throwaway branch, commit the documentation or asset change, push that branch,
and let Ara create the review PR.

## Common profile updates

New team member:

- Confirm the person is approved for public listing in ara.so or internal team
  docs.
- Add the name, role, and link only if that information is public-safe.
- Prefer company-controlled links over personal social links.
- Run Markdown and link validation before review.

New logo:

- Confirm the logo is the approved brand asset.
- Export `profile/logo.png` as a square PNG, currently targeting 512x512.
- Keep the README image width reasonable for GitHub rendering. The current
  displayed width is `120`.
- Run the image validation script and inspect the README diff before review.

Messaging refresh:

- Start from the approved ara.so copy or internal launch doc.
- Keep the GitHub profile concise; link to ara.so for deeper product
  explanation.
- Remove stale claims in the same PR so old positioning does not conflict with
  new copy.
- Ask reviewers to check tone, public-safety, and link destinations, not only
  spelling.

Social link change:

- Verify the destination is public, canonical, and controlled by Ara.
- Use clean HTTPS URLs without tracking parameters.
- Keep link labels human-readable and consistent with the rest of the README.
- Include the reason for the link change in the PR body.
