# David Blazar — Website Shell

A [Quarto](https://quarto.org) website shell built as a starting point, not a finished product. All content was assembled from public sources (UMD College of Education directory, CALDER Center, Google Scholar, EdWorkingPapers) — nothing here came from David directly, so treat every fact as "probably right, please verify."

## Structure

- `index.qmd` — home page: bio, research tags, recognition, contact/social links
- `research.qmd` — research overview, working papers, journal articles, policy briefs
- `teaching.qmd` — courses taught, advising
- `cv.qmd` — embeds `files/David-Blazar-CV.pdf`
- `styles.scss` / `styles.css` — theme (colors, fonts, layout helpers)
- `files/` — CV PDF, placeholder headshot/favicon (SVG initials)
- `_quarto.yml` — site config, nav, footer

## To preview locally

```
quarto preview
```

## To build

```
quarto render
```

Output goes to `_site/`.

## Checklist to finish this site

1. **Photo** — replace `files/headshot-placeholder.svg` with a real headshot. Easiest: add `files/headshot.jpg` and change the `src` in `index.qmd`'s `.hero-photo` block.
2. **Bio voice** — the "About" paragraph on `index.qmd` is written in third person from public bio text. Rewrite it in David's own voice/framing.
3. **CV** — `files/David-Blazar-CV.pdf` is David's last *public* CV, dated May 2022. Swap in a current file (keep the same filename, or update the two links that reference it in `cv.qmd` and `index.qmd`).
4. **Publications** — `research.qmd` lists working papers from EdWorkingPapers (2022–2026) and selected journal articles from the 2022 CV. Several of those working papers have likely since been published — update citations, and add anything from 2023–2026 that's missing. Cross-check against [Google Scholar](https://scholar.google.com/citations?user=atIXv0UAAAAJ&hl=en).
5. **Socials** — currently linked: email (dblazar@umd.edu), X (@david_blazar), LinkedIn, Google Scholar, EdWorkingPapers, UMD faculty profile. Confirm these are current, add/remove as needed (e.g., Bluesky, ORCID, personal site).
6. **Teaching** — course list on `teaching.qmd` is from 2022; confirm what's still being taught.
7. **Remove the orange "editor note" callouts** (the `.editor-note` blocks at the top of each page) once content is finalized — they're placeholder flags, not meant to ship.
8. **Site URL / deploy** — `_quarto.yml` has a placeholder `site-url`. If publishing to GitHub Pages: `quarto publish gh-pages`.

## Design notes

Palette is a warm cream background (`#FAF6EF`) with a terracotta accent (`#B5502D`) and near-black text, deliberately distinct from typical navy/maroon academic templates. Headings use Fraunces (serif), body text uses Inter — both loaded from Google Fonts in `styles.scss`. Swap either in `styles.scss` if a different feel is wanted.
