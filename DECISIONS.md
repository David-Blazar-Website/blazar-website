# Website decision log

Standing decisions for davidblazar.com. Check this before changing the site, and add to it when David makes a new call. Newest decisions are marked with their date. `CLAUDE.md` covers the mechanics (files, workflow, writing rules); this file covers *what David has decided*.

## Launch and hosting
- **Not live until David says so** (2026-11-11). Don't change GoDaddy DNS or merge to `main` in a way that would publish at davidblazar.com before he approves launch.
- Hosting: GitHub Pages, published by GitHub Actions on every push to `main`. Domain verified at the **organization** level (not personal), because the repo belongs to the `David-Blazar-Website` org.
- Automated updates (scheduled tasks) only open pull requests for review. They never merge, and never touch DNS or Pages settings.

## Site structure
- **Three pages: Home, Research, Media** (2026-11-11). The CV is a navbar link to the PDF, not a page. No Teaching page; grants, service and teaching live in the CV.
- **Home** (2026-11-12), top to bottom:
  1. Headshot, name, title, a single affiliation line linking only the **Maryland Equity Project** (no MLDS link in the header), and large social buttons (Email, Google Scholar, Bluesky, LinkedIn, EdWorkingPapers, CV).
  2. **About and the Latest carousel side by side** on desktop, so the About text sits high on the page and the carousel is visible without scrolling. On phones the carousel comes right after the header, then About.
- **About text is David's wording** (2026-11-12). Don't rewrite it; only change it when he sends edits.
- **Carousel** rotates three tags: *New research*, *Opinion*, *In the news* (podcasts are tagged *In the news*). It shows items marked `featured: true` in the data files, newest first, up to 8.
- **Research page** (2026-11-11): note at the top pointing to the shorter versions on the Maryland Equity Project and MLDS Center sites; then Working Papers; then Published Articles, newest first. Full-length papers only.
- **Media page** (2026-11-12): press-inquiries line (dblazar@umd.edu), then **Opinion & Commentary**, **Podcasts & Interviews**, **In the News** (its own section), and **Policy Briefs** (Maryland Equity Project and MLDS Center).
- **Commentary lives on the Media page once and is cross-linked from Research** (2026-11-12). A paper's entry shows "Related" links to the op-eds, briefs and podcasts about it, so readers see them in both places. Each paper's `related:` list in `data/research.yml` holds a label and link for each piece. Only link a piece to a paper when the piece is clearly about that study.
- **Maryland Equity Project briefs are listed without links for now** (2026-11-12): David is refreshing the MEP website and brief formatting; add links after that.
- External briefs and commentary (Brookings, Education Next, IZA World of Labor, Urban Institute, Albert Shanker Institute, The Conversation, The Hill) go under **Opinion & Commentary**. Only Maryland Equity Project and MLDS Center briefs go under **Policy Briefs**.

## Links to papers (hierarchy, 2026-11-12)
1. **Open-access journal article:** one link to the journal version, marked *Open access*.
2. **Paywalled article with a free version elsewhere** (EdWorkingPapers, NBER, IZA, SSRN, university repository): two clearly labeled links, *Journal version* (may require a subscription) and *Free version* (naming where it's posted).
3. **Paywalled article with no free version:** *Journal version*, plus a free manuscript hosted on the site (`files/papers/`). Use David's **accepted manuscript** (the version after peer review, before the publisher's copyediting and typesetting), with a cover line giving the citation and DOI. Don't post the publisher's PDF, and don't rebuild a "clean" copy from the publisher's typeset text. If no accepted manuscript is in David's folder, list the paper for David to find one.
- Acceptable free versions (rule b): working papers and author manuscripts on EdWorkingPapers, NBER/IZA/SSRN, Harvard CEPR, co-authors' sites, NSF PAR, Harvard DASH, or UMD when the file is a manuscript. Don't use publisher PDFs hosted elsewhere (including UMD's copies) as the "free version" (2026-11-12).
- Working papers: link the public version (EdWorkingPapers, etc.) when one exists; otherwise no link.
- **Keep a copy of free versions on the site** (2026-11-12): free versions posted on sites David can't fix if they move (co-authors' sites, UMD, NSF PAR, CEPR reports) are hosted in `files/papers/` and linked there. EdWorkingPapers versions are linked directly, with no copy. A copy of each hosted file is in David's folder `Papers/Free Versions/`.
- **File names** for free versions: `Authors_Year_Short-Title_Journal_Version.pdf`. Version is one of Accepted-Manuscript, Author-Manuscript, Earlier-Version, Working-Paper or CEPR-Report. Year and journal are those of the published article. Manuscripts made from David's Word files have a cover page with the version label, citation and DOI, and a title page with authors and affiliations as published. The cleaned Word files are in `Papers/Final Manuscripts/Cleaned/`.
- Papers with no free version David can find (IJEMST 2018, English Education 2011, English Journal 2009) show only the journal link (2026-11-12).
- Lagos & Blazar (2026, ER) links the 2021 EdWorkingPaper on ERIC (ED616814) as the free version, labeled as an earlier version (2026-11-12).

## Content sourcing
- Facts (titles, dates, co-authors, journal details) come from David's CV, the publication itself, or a source David confirms. If something is uncertain, ask.
- Link the **original outlet** first. For a republished op-ed, mention a major republication (e.g., *The Washington Post*) as a second link; don't list minor republications.
- Working papers on the site must also be on the CV.
- The CV PDF on the site is the current version (October 2026). The editable Word file and the paper PDFs are in David's local folder `Documents/Claude/Personal Website` (papers in `Papers/`, unposted working papers in `Papers/Working Papers/`), not in the public repo.
- Working papers use the title on EdWorkingPapers (or the latest draft) when it differs from the CV; David updates the CV (2026-11-12). Current author orders come from David (e.g., the aide-to-teacher paper: Morris, Montana, Dominguez-Mel, Blazar).
- Titles, pages and DOIs follow the published article when the CV differs (e.g., EFP 2020 "Can video technology improve teacher evaluations?").

## Visuals
- **Research thumbnails:** a key-finding chart redrawn in the site's style from numbers in the paper itself; a topic icon until the paper's figure is made.
- **Media thumbnails:** typographic cards naming the outlet, colored by type (2026-11-12, David approved). No photos taken from news articles (they're licensed to the publisher).
- Palette and fonts: cream `#FAF6EF`, terracotta `#B5502D`, near-black `#232323`; Fraunces headings, Inter body.

## Upkeep
- Weekly scheduled task (Mondays, 7:40 am ET): finds new op-eds, podcasts and press; rotates `featured` to keep the carousel fresh; opens a pull request.
- Monthly scheduled task (1st, 8:17 am ET): checks EdWorkingPapers and journals for new or newly published papers; asks David whether he has new papers; opens a pull request.
