# David Blazar — Website Shell

A [Quarto](https://quarto.org) website shell built as a starting point, not a finished product. All content was assembled from public sources — David's own CV (the current July 2025 version, hosted at `education.umd.edu/media/21698/download`), the UMD College of Education directory, Google Scholar, EdWorkingPapers, and a few journal/press pages — nothing here came from David directly, so treat every fact as "probably right, please verify."

## Structure

- `index.qmd` — home page: bio, research tags, recognition, contact/social links
- `research.qmd` — in-progress work, full journal article list, current grants, affiliations
- `media.qmd` — policy briefs, public writing, press mentions
- `teaching.qmd` — courses taught, program development, advising/mentoring
- `cv.qmd` — embeds `files/David-Blazar-CV.pdf`
- `styles.scss` / `styles.css` — theme (colors, fonts, layout helpers)
- `files/` — CV PDF, headshot (from UMD directory), favicon (SVG initials)
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

1. **Photo** — `files/headshot.jpg` was pulled from the UMD faculty directory (260×260, so on the small side). Swap in a better/current one if David has one.
2. **Bio voice** — the "About" paragraph on `index.qmd` is written in third person from public bio text. Rewrite it in David's own voice/framing.
3. **CV** — `files/David-Blazar-CV.pdf` is David's July 2025 CV (the most recent one found publicly). Three papers have already been published since then (now reflected on `research.qmd`), so the CV itself is a bit behind the site — worth asking David for whatever's most current, and re-dating the "CV last updated" line on `cv.qmd` when you swap it in.
4. **Publications** — `research.qmd`'s journal article list and "In Progress" section reflect the July 2025 CV plus three papers confirmed published since (Disparate Pathways; Localized Teacher Recruitment/Grow-Your-Own; Professional Staff Diversity — all 2026). Re-check the "In Progress" list periodically, since those are the ones most likely to have moved to publication.
5. **Media page** — `media.qmd` is new. The "In the News" section is intentionally thin (just what turned up in a general search) — David will know about interviews, podcast appearances, or press hits that don't show up that way.
6. **Socials** — currently linked: email (dblazar@umd.edu), Bluesky (@davidblazar.bsky.social — found by handle/description match, not confirmed by David), LinkedIn, Google Scholar, EdWorkingPapers, UMD faculty profile, Maryland Equity Project. Confirm these are current, add/remove as needed (e.g., ORCID).
7. **Teaching** — course list and advising roster on `teaching.qmd` reflect the July 2025 CV; both will drift as semesters pass.
8. **Site URL / deploy** — `_quarto.yml` has a placeholder `site-url`. If publishing to GitHub Pages: `quarto publish gh-pages`.

## Design notes

Palette is a warm cream background (`#FAF6EF`) with a terracotta accent (`#B5502D`) and near-black text, deliberately distinct from typical navy/maroon academic templates. Headings use Fraunces (serif), body text uses Inter — both loaded from Google Fonts in `styles.scss`. Swap either in `styles.scss` if a different feel is wanted.

## Why it's structured this way

A review of ~24 peer education-policy researchers' personal sites (or lack thereof) informed a few choices here:

- Most researchers at this level have **no personal site at all** — just a university directory page plus Google Scholar. Having a real site already puts David ahead of most peers; the goal here was to make it substantial rather than a bare portal.
- A separate **Media & Public Writing page** (`media.qmd`) mirrors what the few peers who do maintain real sites almost always include (a press/news section) — it's the most consistent differentiator observed.
- **Publications link out to DOIs/open PDFs where available**, rather than being bibliography-only text, following the pattern on the strongest peer sites (e.g., Jing Liu's, David's own UMD colleague).
- The CV page states its **last-updated date** explicitly, since stale, undated CVs were a common weak point among peer sites.
