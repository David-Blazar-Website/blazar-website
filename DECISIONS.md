# Website decision log

Standing decisions for davidblazar.com. Check this before changing the site, and add to it when David makes a new call. Newest decisions are marked with their date. `CLAUDE.md` covers the mechanics (files, workflow, writing rules); this file covers *what David has decided*.

## Launch and hosting
- **Not live until David says so** (2026-11-11). Don't change GoDaddy DNS or merge to `main` in a way that would publish at davidblazar.com before he approves launch.
- Hosting: GitHub Pages, published by GitHub Actions on every push to `main`. Domain verified at the **organization** level (not personal), because the repo belongs to the `David-Blazar-Website` org.
- Automated updates (scheduled tasks) only open pull requests for review. They never merge, and never touch DNS or Pages settings.

## Site structure
- **Three pages: Home, Research, Media** (2026-11-11). The CV is a navbar link to the PDF, not a page. No Teaching page; grants, service and teaching live in the CV.
- **Home** (2026-11-12), top to bottom:
  1. Headshot, name, title, a single affiliation line linking only the **Maryland Equity Project** (no MLDS link in the header), and large social buttons (Email, Google Scholar, LinkedIn, Bluesky, EdWorkingPapers, CV). LinkedIn comes before Bluesky everywhere (header buttons, navbar, footer). The email button shows the address itself. No ORCID (2026-11-12).
  2. **About and the Latest carousel side by side** on desktop, so the About text sits high on the page and the carousel is visible without scrolling. On phones the carousel comes right after the header, then About. The carousel column is narrower than About, and the two end at the same height. "About" and "Latest" use the same heading style (2026-11-12). On wide screens each slide's image is a tall portrait card the full height of the slide (2026-11-12).
- **About text is David's wording** (2026-11-12). Don't rewrite it; only change it when he sends edits.
- **Carousel** rotates three tags: *New research*, *Opinion*, *In the news* (podcasts are tagged *In the news*). It shows items marked `featured: true` in the data files, newest first, up to 8.
- **Research page** (2026-11-11): note at the top pointing to the shorter versions on the Maryland Equity Project and MLDS Center sites; then Working Papers; then Published Articles, newest first. Full-length papers only. The intro says "a strong and racially diverse teaching workforce" (2026-11-12). Entries are compact and run in two columns on wide screens, to cut scrolling (2026-11-12). The intro and the "Short on time?" box span the full content width, as does the press box on Media (2026-11-12).
- **Research topics** (2026-11-12): Working Papers stay at the top. Published articles are grouped under four topics, newest first within each, plus earlier work, with a row of jump links under the intro: *Teacher labor markets and educator diversity*; *Coaching, evaluation, and teacher development*; *Effective teaching and its effects on students*; *Policy, resources, and student opportunity* (renamed 2026-11-12, when Hill, Blazar & Lynch 2015 moved to Effective teaching and Blazar & Kraft 2019 moved to Coaching; it will also hold the student-absences and CS-for-all papers once published); *Earlier work: Teaching English*. Each paper's `area:` field sets its topic.
- **Media page** (2026-11-12): press-inquiries line (dblazar@umd.edu), then **Opinion & Commentary**, **Podcasts & Interviews** and **In the News** (its own section). Same compact two-column layout as Research.
- **Keep every news item on the site, but show the newest 6** (2026-11-12). The rest open in place with a "Show all N news stories" button; a link to a hidden story opens the list automatically.
- **Policy briefs are off the Media page for now** (2026-11-12). David will revisit them after fixing the Maryland Equity Project site. The brief entries stay in `data/media.yml` (type `brief`) but aren't shown.
- **Commentary lives on the Media page once and is cross-linked from Research** (2026-11-12). A paper's entry shows "Related" links to the op-eds, podcasts and news coverage about it (news added 2026-11-12), so readers see them in both places. Each paper's `related:` list in `data/research.yml` holds a label and link for each piece. Only link a piece to a paper when the piece is clearly about that study.
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
- Lagos & Blazar (2026, ER) uses David's September 2025 manuscript, hosted in `files/papers/` and labeled "Author manuscript, earlier version" (2026-11-12). It replaces the 2021 ERIC working paper, whose findings differ.

## Content sourcing
- Facts (titles, dates, co-authors, journal details) come from David's CV, the publication itself, or a source David confirms. If something is uncertain, ask.
- Link the **original outlet** first. For a republished op-ed, mention a major republication (e.g., *The Washington Post*) as a second link; don't list minor republications.
- Working papers on the site must also be on the CV. David asked (2026-11-12) to add three EdWorkingPapers not yet on the CV: student absences post pandemic (Yaow, Gershenson, Blazar & Hutt), When demand outpaces supply (Yoo, Blazar & Liu) and Computer science for all? (Liu, Conrad & Blazar); he'll add them to the CV.
- **Unposted working papers are held back** (2026-11-12): David isn't ready to share working papers with no public version (teaching tradeoffs, expanding educational opportunity, service scholarships, aide-to-teacher pathways, Troyer paper). Their entries are in `data/research-pending.yml`; the monthly task moves each back into `data/research.yml` once it is publicly posted.
- The CV PDF on the site is the current version (October 2026). The editable Word file and the paper PDFs are in David's local folder `Documents/Claude/Personal Website` (papers in `Papers/`, unposted working papers in `Papers/Working Papers/`), not in the public repo.
- Working papers use the title on EdWorkingPapers (or the latest draft) when it differs from the CV; David updates the CV (2026-11-12). Current author orders come from David (e.g., the aide-to-teacher paper: Morris, Montana, Dominguez-Mel, Blazar).
- Titles, pages and DOIs follow the published article when the CV differs (e.g., EFP 2020 "Can video technology improve teacher evaluations?").

## Visuals
- **Research thumbnails** (2026-11-12): every paper has a key-finding card drawn from the paper itself (a chart or headline number using the paper's own numbers, a short list of findings, or, for the two early English-teaching essays, a key-idea card). On the Research page the thumbnail shows only the big visual, with no small text; the words are in a readable "Key finding:" sentence under the citation (`key_finding:` in research.yml); clicking the thumbnail opens the full card enlarged, not the paper.
- **Carousel images don't repeat the slide's tag** (2026-11-12): the tag (*Opinion*, *In the news*…) appears once, above the title, so the carousel copies of media cards leave the type label off.
- **Media thumbnails:** typographic cards naming the outlet, colored by type (2026-11-12, David approved). No photos taken from news articles (they're licensed to the publisher).
- Palette and fonts: cream `#FAF6EF`, terracotta `#B5502D`, near-black `#232323`; Fraunces headings, Inter body.

## Upkeep
- Weekly scheduled task (Mondays, 7:40 am ET): finds new op-eds, podcasts and press; rotates `featured` to keep the carousel fresh; opens a pull request. Searches go beyond David's name to paper titles and topics, co-authors and a list of outlets, since coverage often names only the study (2026-11-12).
- Monthly scheduled task (1st, 8:17 am ET): checks EdWorkingPapers, CALDER and journals for new or newly published papers, and whether any held-back working paper is now posted; asks David whether he has new papers; opens a pull request.
