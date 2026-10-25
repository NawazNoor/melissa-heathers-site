# Melissa Heathers — website

A fast, crawlable, multi-page static site. No framework, no database, no build step required to host it:
upload the folder and it works. All page content is real HTML, so search engines (and visitors with
JavaScript off) see everything.

## Pages

| URL | Purpose |
|---|---|
| `/` | Brand hub: hero, "Where would you like to begin?" path chooser, book feature, video, Book Crawl, Goddess Gems |
| `/dear-ego-dear-heart/` | **Main book landing page**: cover, story, "Hear both voices" interactive, FAQ, buy buttons |
| `/melissa-heathers/` | Author page: bio, philosophy, milestones, speaking |
| `/the-book-crawl/` | Show page + guest application path |
| `/goddess-gems/` | Children's series, Rose Court, Series 2: Sunlite teaser video |
| `/press/` | Media kit: copyable bios, headshot, quick facts, press and interviews |
| `/meditations/` | Mel's Meditations (three audio players) |
| `/contact/` | Topic-based contact form |
| `/404.html` | Friendly not-found page |

Also included: `sitemap.xml` (with video entries), `robots.txt`, `llms.txt`, `site.webmanifest`, favicons,
`_redirects` (old Wix URLs → new pages) and `_headers` (caching and security).

## Preview in your browser (two easy ways)

**Fastest, nothing to install:** unzip, then drag the `melissa-heathers-site` folder (or the zip) onto
https://app.netlify.com/drop or https://www.cloudflare.com/drop. You get a live link you can open on your phone and
send to Melissa. Unclaimed previews expire quickly (about an hour), so claim it with a free account to keep it.
Drop the folder that contains `index.html`, not `_source`.

**On your own computer:** double-click `preview.bat` (Windows) or `preview.command` (Mac). Your browser opens at
http://localhost:8000. This needs Python (free, python.org). Don't open `index.html` directly: the pages use
root paths (`/assets/...`) and will look unstyled.

## Before launch: three settings

1. **Contact form** — open `assets/js/site.js` and fill in `CONFIG.email` (opens the visitor's email app) or
   `CONFIG.formEndpoint` (a Formspree / Netlify Forms / Basin URL). Until you do, the form shows a "not connected yet" note.
2. **Domain** — the canonical domain is `https://www.soulsecrets.ca` (set in `_source/lib.py` as `BASE`).
   If it changes: edit `BASE`, then `cd _source && python3 build.py` to regenerate every page, canonical link,
   social tag, structured-data entry and the sitemap.
3. **Hosting** — soulsecrets.ca currently runs on Wix. Move the domain's DNS to the new host (Cloudflare Pages,
   Netlify, etc.). Keep `_redirects` so old links (`/bookcrawl`, `/interviews`, `/mels-meditations`) still work.
   Hosts that ignore `_redirects` need the same 301 rules entered in their dashboard.

After launch: add the site to Google Search Console, submit `https://www.soulsecrets.ca/sitemap.xml`, and test
pages in Google's Rich Results Test and the Facebook Sharing Debugger.

## Replace or confirm (nothing here was invented, but some items were not verifiable)

- **Book cover**: the cover on the site is a CSS illustration built from her watercolor, not the official file.
  Put the real cover at `assets/img/dear-ego-dear-heart-cover.jpg` and swap `COVER` in `_source/lib.py` for an `<img>`.
- **The Wix video** is linked directly from Wix's CDN. Download it and self-host it (`assets/video/`) so it keeps working.
  The poster frame is a designed composite, not a frame from the video; its upload date is not set in the structured data.
- **Meditation audio**: add `meditation-1.mp3`, `-2.mp3`, `-3.mp3` to `assets/audio/` (cards show "being added" until then).
- **Sunlite vs Sunstone**: the site says "Sunlite" (series title, per Melissa's latest message). Confirm the spelling,
  and that she wants the Series 2 teaser public. To hide it, delete the `#sunlite` section in `_source/pages_b.py` and rebuild.
- **Signing dates** (Feb 22 and Jul 18, 2026, Indigo Kitchener) come from event signage and her posts: confirm the year.
- **Goddess Gems link** points to the Amazon.co.uk listing; add Amazon.ca when available. Johnny is described from the project notes.
- **ISBN** in the book's structured data is derived from the Amazon ISBN-10 (9781965016398): verify before relying on it.
- **Book Crawl recent conversations** (Grace C.W. Liu, Carroll Patrizi) and the **speaking themes** are drawn from her public posts
  and bios: approve them as written.
- **"Hear both voices"** lines are original site copy, labelled as not excerpts from the book.
- **Facebook** is the only social link found. Add Instagram/YouTube in `lib.py` (`PERSON.sameAs` and footer).

## Edit and rebuild

Copy lives in `_source/pages_a.py` and `_source/pages_b.py`, shared header/footer and SEO in `_source/lib.py`,
design in `assets/css/style.css`. After editing, run `python3 build.py` inside `_source/` (Python 3, no extra packages).
Bump `ASSET_V` in `lib.py` after changing CSS or JS so browsers fetch the new files.

## Tested

Every page: one H1, unique title and description, valid structured data, no broken internal links or anchors,
alt text on all images. Behaviour tested in a headless browser: mobile menu, ego/heart widget, FAQ, video play button,
copy buttons, contact form states, header hide/show on scroll, no horizontal scrolling at 390px and 1440px.
Not tested here: web-font loading (the preview had no internet), real phones, Lighthouse scores, and playback of the Wix-hosted video.
