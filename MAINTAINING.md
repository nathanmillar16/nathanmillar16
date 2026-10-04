# Maintaining this GitHub profile

This repository must be public and named `nathanmillar16` under the `nathanmillar16` account for GitHub to show its root README on the profile.

- Edit the readable content in `README.md`.
- Graphic assets live in `assets/`. SVG text, colour and animation are editable without build tooling.
- The hero uses SVG CSS animation, with reduced-motion support and a static fallback. GitHub does not execute JavaScript in READMEs.
- Keep alt text in sync when editing graphical cards.
- Use public project pages instead of links to private repositories.
- No analytics, visitor counters, API tokens, scheduled workflows, or third-party badge services are required. All graphics are local to this repository.
- `preview.html` is a local review page, not a GitHub Pages deployment. GitHub controls the actual README typography, spacing and image rendering.
- Run `python3 scripts/check.py` to verify assets and image references before publishing.

## Publish when ready

```sh
gh repo create nathanmillar16 --public --source=. --remote=origin --push --description "Nathan Millar — frontend engineering, projects and experience"
```

If the repository already exists, add its remote and push instead. Do not replace an existing profile without reviewing it first.
