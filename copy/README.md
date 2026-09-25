# Copy

One folder per page, named after the page in agent/site-plan.yaml.

    copy/
    └── page-slug/
        ├── notes.md               raw material, who the page is for
        ├── outline.md             sections in order, from section-library.md
        ├── draft-version-one.md
        └── review.md              optional feedback

Only create the files a page needs. Number versions: version one, two, three.
Never call a file final.

Two ways we work, set in agent/research-brief.md:
- We write the copy: Claude drafts with Compound Writing (cw-scribe), using
  agent/VOICE.md and agent/STYLE.md.
- The client writes the copy: Claude makes a Google Doc for every page (copy-brief skill),
  linked from each page's wireframe in sitemap/index.html.
