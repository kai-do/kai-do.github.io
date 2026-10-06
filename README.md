# kai.do

Personal portfolio and learning blog for Nakai Zemer, built with [Quarto](https://quarto.org/) and served by GitHub Pages at https://kai.do.

## How the site is built

- Source: `.qmd` files at the root, plus `posts/`, `notes/`, and `projects/`.
- `quarto render` writes the site to `docs/`; GitHub Pages serves `main` / `/docs`. `docs/` is committed.
- `freeze: auto` stores executed code output in `_freeze/` (committed), so old posts never re-run on rebuild.
- Pages with `draft: true` are left out of the site, listings, search, and feeds.
- Theme: `assets/_light.scss`, `assets/_dark.scss`, and shared rules in `styles.scss`.
- Analytics: GoatCounter snippet in `assets/goatcounter.html` (commented out until a site code is added).

## How to publish a post

1. Copy `_templates/post.qmd` to `posts/YYYY-MM-DD-slug/index.qmd` (or `notes/YYYY-MM-DD-slug/index.qmd`).
2. Write the post: fill in the title, description, categories, and optional image.
3. Set `draft: false`.
4. Run `quarto render` (use `quarto preview` while writing).
5. Commit (including `docs/` and `_freeze/`) and push.

To embed a shinylive app, uncomment `filters: [shinylive]` and the `{shinylive-r}` block in the template.
