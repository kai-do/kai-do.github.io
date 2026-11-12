Kaido Analytics is a data science and reporting practice. Its look is deep navy and teal with warm copper and gold, on cool navy-tinted neutrals and soft pastels. Keep it calm, exact and data-first.

## Color

- Use the semantic tokens (`surface`, `ink`, `brand`, `accent`, `callout`) so light and dark both work. Reach for the palette names only when a chart, cover or logo must keep an exact color.
- The core is `prussian-blue`, `stormy-teal`, `copperwood` and `gold`. Navy and teal carry structure; `gold` marks the one thing to look at; `copperwood` is the deeper warm tone for secondary emphasis.
- Set text in `ink` on `surface`, `surface-raised` or `surface-sunken`. Use `ink-muted` for captions.
- `brand` (teal) is for links, primary buttons and the first chart series; put `on-brand` text on a `brand` fill.
- `accent` (gold) is fills only: the key series, one highlight. Gold is too light for text on light grounds; gold-family text is `accent-text` (`copper-deep` in light). On light surfaces a gold mark is 2.3:1 against the ground, so give it a label or a navy neighbor.
- Neutrals `neutral-50` to `neutral-800` are grays tinted with prussian blue. Use them for grounds, gridlines, table bands and secondary text; never use pure gray. `neutral-500` is for edges and placeholders, not body text; text starts at `neutral-600`.
- Pastels (`teal-50`/`100`, `gold-50`/`100`, `navy-50`/`100`, `frosted-mint`) are soft backgrounds: info panels, callouts, selected rows, table bands. Put `prussian-blue` text on any of them; `stormy-teal` and `copper-deep` text also read on all of them.
- A key finding sits in a `callout` box (`gold-50` in light) with its label in `accent-text`.
- `muted-teal` (sage) is the link and button color in dark, the tip callout edge, and a quiet chart color; never text on light grounds.
- Dark-mode body text is `neutral-100`, not mint; `frosted-mint` is currently unused.
- The site header is `header-bg` (teal) in both themes, with `header-text` and `header-text-hover`.
- Tags: client tags are `tag-client-bg` with `tag-client-text`; subject tags use `tag-subject-bg`; tool tags (R, SQL, Shiny) use `tag-tool-bg`. Tag text is `ink` unless a tag token says otherwise.
- Callouts: key finding is `callout` with a `callout-key-edge`; notes and blockquotes are `callout-note-bg`; tips take `callout-tip-edge`; warnings take `callout-warning-edge`.
- Text selection is `selection`; table rows alternate with `table-stripe`.
- Control edges and meaningful borders use `border-strong`; `border` is decorative only. Focus is a solid 2px `focus-ring`.
- Chart series order: `stormy-teal`, `prussian-blue`, `gold` (the one to look at), `muted-teal`, `copperwood`, then `neutral-400`. Never put `copperwood` and `gold` side by side.
- The brand has no status colors. When a chart needs good/bad, pair color with a word or icon and keep the two apart in lightness, not red against green.

## Type

- Headings that open a page or report use `display-xl`, `display-lg` or `heading-1` in the display family. Everything else uses `heading-2`, `body`, `body-sm` and `label` in the sans family.
- Figures, IDs, SQL and code use `data` (mono). Right-align numbers in tables.
- The families are system stacks, not licensed brand faces; swap in real font files in `fonts/` and `type.fonts` when the brand picks them.

## Space and shape

- Space comes from `space-1` to `space-16`; card padding is `space-4`, page margins `space-12`.
- Corners are small and precise: `radius-md` on buttons, inputs and cards, `radius-lg` on panels, `radius-sm` on chart bars.
- Separate surfaces with a `border` hairline or a step in surface, not shadows.

## Name and mark

- Write the name as "Kaido Analytics". The wordmark sets "Kaido" in Spectral 500 over "ANALYTICS" in IBM Plex Mono 500, tracked wide; use the lockup files rather than retyping it.
- The mark is a gold star spiralling into a navy black hole, on a plane seen at an angle; the star trails a copper arm and the black hole a teal one, both fading outward. The black hole, ringed in its own color, launches one jet straight up and down. It stands for precision, mathematics and astronomy.
- The black hole is the mark's exact center. Align the mark on it, not on the spirals.
- Files under `assets/Logos/`: `kaido-lockup-on-light` / `-on-dark` (mark and wordmark), `kaido-mark-on-light` / `-on-dark` / `-on-teal` (mark alone, square), `app-icon-512.png` (mark on a navy rounded tile).
- Each file names its background. The fading arms are pre-blended with that background, so use each only on the ground it names. On `header-bg` use `kaido-mark-on-teal`.
- Never recolor, stretch or rotate the mark.
