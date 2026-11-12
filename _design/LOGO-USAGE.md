# Kaido Analytics logo

The mark: a gold star spiralling into a navy black hole, which launches a jet straight up and down.
The black hole sits at the exact center of the mark.

Marks (square), each drawn for one background:

- `kaido-mark-on-light.svg`: light page (#f7faff) or white.
- `kaido-mark-on-dark.svg`: navy page (#0c1b33).
- `kaido-mark-on-teal.svg`: the teal site header (#0e6b6b).

The fading spiral arms are pre-blended with that background, so use each file on the background it names.

Lockups pair the mark with the wordmark: `kaido-lockup-on-light.svg`, `kaido-lockup-on-dark.svg`.
The wordmark text is outlined (Spectral 500 and IBM Plex Mono 500, both SIL Open Font License), so no fonts are needed.

Icons: `png/app-icon-512.png`, `app-icon-180.png` (Apple touch icon) and `app-icon-32.png` are the mark on a navy rounded tile.
`svg/favicon.svg` is the mark for light browser tabs.

Quarto: put `favicon.svg` in the project and set `website: favicon: favicon.svg` in `_quarto.yml`;
use `kaido-mark-on-teal.svg` as `website: navbar: logo:`.
