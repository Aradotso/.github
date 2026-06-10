# .github — Ara Org Profile

This is the [`Aradotso/.github`](https://github.com/Aradotso/.github) special repository.
GitHub uses it to display a public profile for the **Aradotso** organization at
[github.com/Aradotso](https://github.com/Aradotso).

See [GitHub's docs on org profile READMEs](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile) for how this works.

## What goes where

`profile/` — public-facing assets rendered on the org's GitHub profile page:
- `README.md` — the profile text and layout shown on github.com/Aradotso
- `hero.png` — hero banner image
- `logo.png` — org logo

`.github/` (not yet present) — if added later, this is the place for org-wide issue templates,
PR templates, and reusable workflow files that GitHub picks up across all repos in the org.

## How to update the profile

Edit `profile/README.md` (and swap out images as needed), then push to `main`.
GitHub reflects changes within a few minutes.

```
# Example
vi profile/README.md
git add -A && git commit -m "profile: update org description"
git push
```

Changes sync automatically to [github.com/Aradotso](https://github.com/Aradotso) on push.
