#!/usr/bin/env python3
"""Builds the static site into ../ (the folder above _source).
Usage:  cd _source && python3 build.py
Edit copy in pages_a.py / pages_b.py, settings in lib.py, then rebuild."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
import pages_a, pages_b

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PAGES = [pages_a.home(), pages_a.book(), pages_a.about(), pages_a.crawl(),
         pages_b.gems(), pages_b.press(), pages_b.meditations(), pages_b.contact(), pages_b.notfound()]

def write(rel, text):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)

for pg in PAGES:
    html_text = shell(pg["path"], pg["title"], pg["desc"], pg["body"], schema=pg.get("schema", ()),
                      active=pg.get("active"), dark_top=pg.get("dark_top", False), noindex=pg.get("noindex", False),
                      preload_img=pg.get("preload_img"))
    if pg["path"] == "/":
        rel = "index.html"
    elif pg["path"].endswith(".html"):
        rel = pg["path"].lstrip("/")
    else:
        rel = pg["path"].strip("/") + "/index.html"
    write(rel, html_text)

# ---------------------------------------------------------------- sitemap
priority = {"/": "1.0", "/dear-ego-dear-heart/": "0.9", "/the-book-crawl/": "0.8", "/melissa-heathers/": "0.8",
            "/goddess-gems/": "0.8", "/press/": "0.6", "/contact/": "0.6", "/meditations/": "0.5"}
vids = {
    "/": [("Melissa Heathers, author of Dear Ego, Dear Heart", "A video featuring Melissa Heathers, author of Dear Ego, Dear Heart.", "/assets/img/video-poster.jpg", VIDEO)],
    "/dear-ego-dear-heart/": [("Melissa Heathers, author of Dear Ego, Dear Heart", "A video featuring Melissa Heathers, author of Dear Ego, Dear Heart.", "/assets/img/video-poster.jpg", VIDEO)],
    "/goddess-gems/": [("Series 2 Sunlite teaser", "A short animated teaser for Series 2: Sunlite, the next story in The Goddess Gems by Melissa Heathers.", "/assets/video/sunlite-poster.jpg", "/assets/video/sunlite-teaser.mp4")],
}
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
urls = []
for pg in PAGES:
    if pg.get("noindex"):
        continue
    p = pg["path"]
    x = f"  <url>\n    <loc>{BASE}{p}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{priority.get(p, '0.5')}</priority>\n"
    for (name, d, thumb, src) in vids.get(p, []):
        loc = src if src.startswith("http") else BASE + src
        x += (f"    <video:video>\n      <video:thumbnail_loc>{BASE}{thumb}</video:thumbnail_loc>\n      <video:title>{esc(name)}</video:title>\n"
              f"      <video:description>{esc(d)}</video:description>\n      <video:content_loc>{esc(loc)}</video:content_loc>\n    </video:video>\n")
    x += "  </url>"
    urls.append(x)
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n'
           + "\n".join(urls) + "\n</urlset>\n")
write("sitemap.xml", sitemap)

write("robots.txt", f"""User-agent: *
Allow: /

Sitemap: {BASE}/sitemap.xml
""")

write("llms.txt", f"""# Melissa Heathers

> Melissa Heathers is an author, speaker and creative visionary based in Kitchener, Ontario, Canada. She wrote the poetry collection "dear Ego, dear Heart", created the children's series "The Goddess Gems: A Mystical Adventure", and is founder, executive producer and host of "The Book Crawl", which streams on EzWay TV under The Women's Channel. Her philosophy: every story is worth savouring.

## Key pages
- [Home]({BASE}/): overview and where to begin
- [dear Ego, dear Heart]({BASE}/dear-ego-dear-heart/): a poetic tale of the war within, written as letters between the ego and the heart
- [The Book Crawl]({BASE}/the-book-crawl/): a televised literary experience for authors
- [The Goddess Gems]({BASE}/goddess-gems/): a children's story world; Book 1 is Rose Court, the Goddess Gem of Love
- [About Melissa Heathers]({BASE}/melissa-heathers/): biography and milestones
- [Press & media kit]({BASE}/press/): approved bios, headshot, quick facts, interviews
- [Mel's Meditations]({BASE}/meditations/): three complimentary meditations
- [Contact]({BASE}/contact/): speaking, Book Crawl guest applications, press

## Buy
- [dear Ego, dear Heart on Amazon.ca]({BUY})
""")

write("site.webmanifest", json.dumps({
    "name": "Melissa Heathers", "short_name": "Melissa Heathers", "start_url": "/", "display": "standalone",
    "background_color": "#fff8f2", "theme_color": "#fff8f2",
    "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))

# Netlify / Cloudflare Pages style files (ignored by hosts that don't use them)
write("_redirects", """# Old Wix URLs -> new pages (301)
/bookcrawl            /the-book-crawl/   301
/bookcrawl/           /the-book-crawl/   301
/interviews           /press/            301
/interviews/          /press/            301
/mels-meditations     /meditations/      301
/mels-meditations/    /meditations/      301
/photopassion         /                  301
/blog                 /                  301
""")
write("_headers", """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*.html
  Cache-Control: public, max-age=0, must-revalidate
""")

print("built", len(PAGES), "pages ->", OUT)
