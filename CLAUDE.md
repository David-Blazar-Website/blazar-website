# CLAUDE.md: David Blazar's website

Personal academic website for David Blazar (University of Maryland College of Education), built with [Quarto](https://quarto.org) and hosted on GitHub Pages.

- **Repo:** https://github.com/David-Blazar-Website/blazar-website. The org owners are David Blazar (`davidblazar`) and Wesley Morris (`WesleyTMorris`).
- **Live site:** https://david-blazar-website.github.io/blazar-website/ (until a custom domain is attached; see To-do).
- More than one person edits this repo, so **always `git pull` before changing anything.**

## Workflow

```
git pull                      # get the other person's changes first
quarto preview                # local preview with live reload
# ...edit .qmd files...
git add -A && git commit -m "Short description of the change"
git push origin main          # source of truth is main
quarto publish gh-pages       # renders and pushes the built site to gh-pages
```

- `main` holds the source. `gh-pages` holds only the built site and is written by `quarto publish gh-pages`, so never edit it by hand.
- Pushing to `main` does **not** update the live site; you have to run `quarto publish gh-pages` as well. Pages builds take about 1 minute.
- `_site/` and `.quarto/` are build output and are in `.gitignore`. Don't commit them.
- Keep commits small, with a message saying what changed.
- After publishing, open the live URL and check that the change shows up.

## Structure

| File | Contents |
|---|---|
| `index.qmd` | Home: headshot, title, bio (3 short paragraphs), research tags, "In the News" auto-scrolling carousel, Connect links |
| `research.qmd` | Work in Progress, Journal Articles (newest first), Invited Articles, Selected Grants, Service and Affiliations |
| `media.qmd` | Maryland Equity Project policy briefs, research briefs and public writing, In the News list |
| `teaching.qmd` | Courses, program development, advising and mentoring |
| `cv.qmd` | Download button, "Last updated" date, embedded PDF |
| `_quarto.yml` | Site title, `site-url`, navbar, footer, social icons, theme |
| `styles.scss` / `styles.css` | Theme: palette, fonts, and the layout classes below |
| `files/` | `David-Blazar-CV.pdf`, `headshot.jpg`, `favicon.svg` |

### Conventions
- **Publication lists** use raw HTML, `<ul class="pub-list">`, with `<li>` entries in APA style. Put an optional `<span class="pub-note">` after an entry for awards or coverage, and `<span class="pub-authors">` for co-author or role lines. Escape `&` as `&amp;`. Link titles to the DOI or an open-access PDF when one exists.
- **News carousel** (`index.qmd`): each item is a `::: {.news-card-h}` block with `.news-outlet-h`, `.news-headline-h` and `.news-date-h`, newest first. When you add a press item, add it to the carousel **and** to the In the News list on `media.qmd`, keeping both newest first.
- Other classes: `.hero`, `.tag-row` / `.tag-chip`, `.section-rule` (an `<hr>` between sections), `.connect-card`, `.btn-accent`, `.btn-outline`.
- **Social links** appear in three places: the `_quarto.yml` navbar, the `_quarto.yml` footer, and the Connect card on `index.qmd`. Change all three together.
- **Design:** cream background `#FAF6EF`, terracotta accent `#B5502D`, near-black text `#232323`. Headings are in Fraunces (serif) and body text in Inter, both loaded from Google Fonts in `styles.scss`. Keep these unless David asks for a change.

## Writing rules
- Third person ("David studies…"), professional and academic, but plain and readable. Prefer short sentences over long lists joined by semicolons.
- Avoid filler and marketing language ("sits at the intersection of", "substantial record", "made possible by"). Don't stack em dashes.
- Don't put notes to editors on public pages (such as "add more here" or "verify this"). Keep those in this file or the README.
- **Don't add facts that aren't confirmed.** Titles, dates, grant amounts, co-authors and journal details must come from David's CV, the publication itself or another source David has confirmed. If something is uncertain, ask rather than guess.
- When a paper moves from Work in Progress to published, move it into Journal Articles with full citation details and remove it from Work in Progress.
- When you replace the CV PDF, update the "Last updated" date on `cv.qmd`.

## To-do
- [ ] **Custom domain** (David has purchased one; the name and registrar are still needed).
  1. Add a `CNAME` file containing the domain, and list it under `project: resources:` in `_quarto.yml` so `quarto publish` keeps it.
  2. Set `site-url` in `_quarto.yml`.
  3. Add the DNS records at the registrar: A records for the bare domain pointing to 185.199.108.153, .109.153, .110.153 and .111.153, plus `www` as a CNAME to `david-blazar-website.github.io`. Don't touch existing email (MX) records.
  4. Set the domain under repo Settings → Pages, verify the domain at the org level, and turn on Enforce HTTPS.
- [ ] Higher-resolution headshot (the current one is 260×260 px, from the UMD directory).
- [ ] Current CV PDF (the site currently has the July 2025 version).
- [ ] Confirm the Bluesky handle (`davidblazar.bsky.social`) and the other social links; consider adding ORCID.
- [ ] Check Work in Progress and the course and advising lists each semester.
- [ ] Optional: a GitHub Action to publish automatically on every push to `main`, so editors don't need Quarto installed.
