# CLAUDE.md: David Blazar's website

Personal academic website for David Blazar (University of Maryland College of Education), built with [Quarto](https://quarto.org) and hosted on GitHub Pages.

- **Repo:** https://github.com/David-Blazar-Website/blazar-website. The org owners are David Blazar (`davidblazar`) and Wesley Morris (`WesleyTMorris`).
- **Live site:** https://davidblazar.com once DNS is switched over (held until David approves launch). The default address, https://david-blazar-website.github.io/blazar-website/, redirects there.
- More than one person edits this repo, so **always `git pull` before changing anything.**
- **Read `DECISIONS.md` first.** It records what David has decided about the site (structure, link rules, what goes where). Add to it when he makes a new call.

## Workflow

```
git pull                      # get the other person's changes first
quarto preview                # local preview with live reload
# ...edit files...
git add -A && git commit -m "Short description of the change"
git push origin main          # publishing happens automatically
```

- `main` holds the source. Every push to `main` runs `.github/workflows/publish.yml`, which renders the site and deploys it to GitHub Pages (about 1–2 minutes). Check progress on the repo's Actions tab; "Run workflow" there redeploys without a change.
- Repo Settings → Pages → Source must be "GitHub Actions". `quarto publish gh-pages` is no longer used, and the old `gh-pages` branch can be deleted once the Actions deploy is confirmed.
- `_site/` and `.quarto/` are build output and are in `.gitignore`. Don't commit them.
- Keep commits small, with a message saying what changed.
- After a deploy, open the live URL and check that the change shows up.

## Structure

Three pages, driven by two data files. To add or change a paper or media item, edit the YAML, run the thumbnail script, and render; you rarely need to touch the `.qmd` pages.

| File | Contents |
|---|---|
| `index.qmd` | Home: headshot, title, roles, social buttons, "Latest" carousel (featured items from both data files), About bio, research tags |
| `research.qmd` | Note pointing to MEP and MLDS short versions; Working Papers; Published Articles (both listings from `data/research.yml`) |
| `media.qmd` | Press-inquiries note; Opinion & Commentary, Podcasts & Interviews, In the News, Policy Briefs (all from `data/media.yml`) |
| `data/research.yml` | One entry per paper, in display order (working papers, then published newest first). Field guide at the top of the file |
| `data/media.yml` | One entry per op-ed, podcast, news item or brief. Field guide at the top of the file |
| `_listings/*.ejs` | Templates for the carousel, paper list and media list. In Quarto's EJS, `<%= %>` outputs raw HTML and `<%- %>` escapes. Keep template lines unindented, or Pandoc reads them as code blocks |
| `scripts/make_thumbnails.py` | Writes `images/research/*.svg` and `images/media/*.svg` from the data files: a key-finding chart when a paper has a `finding:` block, otherwise a topic icon; a typographic card for media |
| `images/` | Generated thumbnails (commit them; the publish workflow does not run the script) |
| `files/` | `David-Blazar-CV.pdf` (linked from the navbar and home page), `headshot.jpg`, `favicon.svg` |
| `_quarto.yml` | Site title, `site-url`, navbar (Home, Research, Media, CV), footer, social icons, theme, `resources` |
| `styles.scss` / `styles.css` | Theme and component styles |

### Adding things
- **New paper or working paper:** add an entry to `data/research.yml` in the right place, with `topic:` for its icon. To feature it in the carousel, add `featured: true`, a `date`, and a one-sentence `summary`. A `finding:` block turns its thumbnail into a key-finding chart; only use numbers that appear in the paper. Then `python3 scripts/make_thumbnails.py`.
- **New op-ed, podcast or press item:** add an entry to `data/media.yml` with `type:`; set `featured: true` and a `summary` for the newest few so the carousel stays fresh, and remove `featured` from older ones (the carousel shows up to 8, newest first). Then run the thumbnail script.
- Prefer the original outlet's URL; when only a republication is verified, use it and say so in `note:`.
- Don't use photos from news articles (they're licensed to the publisher). Use the generated cards, a figure redrawn from the paper's own numbers, or a freely licensed photo with credit.

### Conventions
- Citations are assembled in APA style by `_listings/research.ejs` from the data fields; David's name is bolded automatically.
- **Social links** appear in three places: the `_quarto.yml` navbar, the `_quarto.yml` footer, and the social buttons on `index.qmd`. Change all three together.
- Other classes: `.hero`, `.social-row` / `.social-btn`, `.tag-row` / `.tag-chip`, `.section-rule`, `.brief-note`, `.press-card`.
- **Design:** cream background `#FAF6EF`, terracotta accent `#B5502D`, near-black text `#232323`. Headings are in Fraunces (serif) and body text in Inter, both loaded from Google Fonts in `styles.scss`. Keep these unless David asks for a change.

## Writing rules
- Third person ("David studies…"), professional and academic, but plain and readable. Prefer short sentences over long lists joined by semicolons.
- Avoid filler and marketing language ("sits at the intersection of", "substantial record", "made possible by"). Don't stack em dashes.
- Don't put notes to editors on public pages (such as "add more here" or "verify this"). Keep those in this file or the README.
- **Don't add facts that aren't confirmed.** Titles, dates, grant amounts, co-authors and journal details must come from David's CV, the publication itself or another source David has confirmed. If something is uncertain, ask rather than guess.
- When a working paper is published, change its `status` to `published`, add the journal details and link, and move it into the published block.
- Working papers listed on the site must also be on David's CV.
- When you replace the CV, replace `files/David-Blazar-CV.pdf`. The editable Word version is in David's local folder (Documents/Claude/Personal Website), not in this public repo.

## To-do
- [ ] **Custom domain** `davidblazar.com` (GoDaddy). Done: `site-url` set; domain verified at the org level (TXT record `_github-pages-challenge-david-blazar-website`, keep it); custom domain entered in repo Settings → Pages. Remaining, only when David approves launch: at GoDaddy delete the "WebsiteBuilder Site" A record, add A records for `@` → 185.199.108.153, .109.153, .110.153, .111.153, and point `www` (CNAME) to `david-blazar-website.github.io`; then turn on Enforce HTTPS. Don't touch other records. No `CNAME` file is needed with Actions deploys.
- [ ] Higher-resolution headshot (the current one is 260×260 px, from the UMD directory).
- [ ] Confirm the Bluesky handle (`davidblazar.bsky.social`) and the other social links; consider adding ORCID.
- [ ] Key-finding visuals: 11 papers have them; the rest use topic icons. Paper PDFs are in David's local folder (Documents/Claude/Personal Website/Papers).
- Free versions: eight accepted manuscripts are hosted in `files/papers/` (AJE 2017, EP 2017, ER 2015, ER 2020, EFP 2020, EEPA 2015, EER 2015, TCR 2020). IJEMST 2018, English Education 2011 and English Journal 2009 have no free version; David decided they show the journal link only (2026-11-12).
- [ ] Not yet copied to `files/papers/` (Chrome blocked the downloads): the RER 2018 and EEPA 2017 manuscripts on matthewakraft.com, and the three Harvard CEPR working papers (AERJ 2016, Educational Assessment 2017 and 2012).
- [ ] Figures missing from two manuscripts (the Word files have only placeholders or titles): EFP 2020 Figure 1; EEPA 2015 Figures 1–4.
