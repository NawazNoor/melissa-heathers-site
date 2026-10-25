"""Shared pieces for the Melissa Heathers static site generator.
Change BASE below (and rebuild with `python3 build.py`) if the domain changes."""
import json, datetime, html

# ------------------------------------------------------------------ settings
BASE = "https://www.soulsecrets.ca"          # canonical domain, no trailing slash
SITE = "Melissa Heathers"
TODAY = datetime.date.today().isoformat()
ASSET_V = "1"                                 # bump to bust caches after edits

BUY = "https://www.amazon.ca/dear-Ego-Heart-Poetic-Within/dp/1965016391"
AMAZON_AUTHOR = "https://www.amazon.ca/stores/author/B0DS46CXM5"
GG_AMAZON = "https://www.amazon.co.uk/Goddess-Gems-Mystical-Adventure-Court/dp/1067413103"
FACEBOOK = "https://www.facebook.com/melissa.penfoldheathers"
EZWAY = "https://ezwaywalloffame.com/members/MelHeathers/"
CDP = "https://podcasts.apple.com/us/podcast/live-with-cdp-talk-show-guest-melissa-heathers-author/id1564979524?i=1000700027376"
PRESS_RELEASE = "https://smallbiz.com/news/melissa-heathers-and-the-book-crawl-are-redefining-how-authors-turn-their-pages-into-influence/"
VIDEO = "https://video.wixstatic.com/video/a94b84_acf6c5da7946451ebbb30fe9fb05cd05/480p/mp4/file.mp4"

def isbn10_to_13(i10):
    d = "978" + i10[:9]
    s = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(d))
    return d + str((10 - s % 10) % 10)

ISBN_DEDH = isbn10_to_13("1965016391")        # derived from the Amazon ISBN-10: verify before relying on it
ISBN_ROSE = "9781067413101"                   # from the Amazon.co.uk listing

PERSON_ID = BASE + "/#melissa"
SITE_ID = BASE + "/#website"

NAV = [
    ("/dear-ego-dear-heart/", "The Book"),
    ("/the-book-crawl/", "The Book Crawl"),
    ("/goddess-gems/", "Goddess Gems"),
    ("/melissa-heathers/", "About"),
    ("/press/", "Press"),
    ("/contact/", "Contact"),
]

PERSON = {
    "@type": "Person",
    "@id": PERSON_ID,
    "name": "Melissa Heathers",
    "url": BASE + "/melissa-heathers/",
    "image": BASE + "/assets/img/melissa-heathers.png",
    "jobTitle": "Author, speaker, and Executive Producer & Host of The Book Crawl",
    "description": "Melissa Heathers is an author, speaker and creative visionary: author of the poetry collection Dear Ego, Dear Heart, creator of the children's series The Goddess Gems, and founder and host of The Book Crawl.",
    "homeLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "Kitchener", "addressRegion": "ON", "addressCountry": "CA"}},
    "sameAs": [FACEBOOK, AMAZON_AUTHOR, EZWAY],
    "knowsAbout": ["Poetry", "Children's books", "Emotional resilience", "Author media visibility", "Television and podcasting for authors"],
}

def T(s, **extra):
    """Replace [[TOKENS]] in page copy."""
    tokens = {"BUY": BUY, "AMAZON_AUTHOR": AMAZON_AUTHOR, "GG_AMAZON": GG_AMAZON, "FACEBOOK": FACEBOOK,
              "EZWAY": EZWAY, "CDP": CDP, "PR": PRESS_RELEASE, "VIDEO": VIDEO}
    tokens.update(extra)
    for k, v in tokens.items():
        s = s.replace("[[" + k + "]]", v)
    return s

def ld(*nodes):
    graph = {"@context": "https://schema.org", "@graph": list(nodes)}
    return '<script type="application/ld+json">' + json.dumps(graph, ensure_ascii=False, separators=(",", ":")) + "</script>"

def breadcrumbs(items):
    """items: list of (name, path). Returns schema node."""
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + p} for i, (n, p) in enumerate(items)]}

def crumbs_html(items):
    lis = []
    for i, (n, p) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{html.escape(n)}</li>')
        else:
            lis.append(f'<li><a href="{p}">{html.escape(n)}</a></li>')
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(lis) + "</ol></nav>"

def wave(bg, fill, flip=False):
    path = "M0,40 C240,90 480,0 720,36 C960,72 1200,10 1440,44 L1440,90 L0,90 Z"
    t = ' style="transform:scaleY(-1)"' if flip else ""
    return f'<div class="wave" style="background:{bg}" aria-hidden="true"><svg viewBox="0 0 1440 90" preserveAspectRatio="none" style="fill:{fill}"{t}><path d="{path}"/></svg></div>'

def header(active):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    links.append(f'<a class="btn" href="{BUY}" rel="noopener">Get the book <span class="arr">→</span></a>')
    return f'''<header class="site-header">
  <div class="wrap header-in">
    <a class="brand" href="/" aria-label="Melissa Heathers, home">melissa <b>heathers</b></a>
    <nav id="site-nav" class="nav" aria-label="Primary">{"".join(links)}</nav>
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span></button>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="/">melissa <b style="color:var(--peach)">heathers</b></a>
        <p class="foot-quote">Every story is worth savouring.</p>
        <p class="small" style="margin-top:1rem">Author · Speaker · Visionary Executive Producer<br>Kitchener, Ontario, Canada</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/dear-ego-dear-heart/">dear EGO dear HEART</a></li>
          <li><a href="/the-book-crawl/">The Book Crawl</a></li>
          <li><a href="/goddess-gems/">The Goddess Gems</a></li>
          <li><a href="/meditations/">Mel’s Meditations</a></li>
        </ul>
      </div>
      <div>
        <h4>Work together</h4>
        <ul>
          <li><a href="/melissa-heathers/">About Melissa</a></li>
          <li><a href="/press/">Press &amp; media kit</a></li>
          <li><a href="/contact/?topic=speaking">Speaking &amp; interviews</a></li>
          <li><a href="/contact/?topic=book-crawl">Be a Book Crawl guest</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <ul>
          <li><a href="{FACEBOOK}" rel="me noopener">Facebook</a></li>
          <li><a href="{AMAZON_AUTHOR}" rel="me noopener">Amazon author page</a></li>
          <li><a href="{EZWAY}" rel="me noopener">eZWay profile</a></li>
          <li><a href="{BUY}" rel="noopener">Buy on Amazon.ca</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-base">
      <span>© <span data-year>2026</span> Melissa Heathers. All rights reserved.</span>
      <span>Think. Ink. Drink.</span>
    </div>
  </div>
</footer>'''

FONTS = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500"
         "&family=Jost:wght@300;400;500&display=swap")

def shell(path, title, desc, body, schema=(), active=None, dark_top=False, og_image="/assets/img/og-image.jpg", noindex=False, preload_img=None):
    url = BASE + path
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    t = html.escape(title, quote=True); d = html.escape(desc, quote=True)
    pre = f'<link rel="preload" as="image" href="{preload_img}" fetchpriority="high">' if preload_img else ""
    graph = ld(*schema) if schema else ""
    body_class = "dark-top" if dark_top else ""
    canon = "" if noindex else f'<link rel="canonical" href="{url}">'
    return f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="{robots}">
{canon}
<meta name="theme-color" content="#fff8f2">
<meta property="og:site_name" content="{SITE}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_CA">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{BASE}{og_image}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/icon-192.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/assets/css/style.css?v={ASSET_V}">
{pre}
<script>document.documentElement.classList.add("js")</script>
{graph}
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/js/site.js?v={ASSET_V}" defer></script>
</body>
</html>
'''

def film(src, poster, label, tall=False, w=None, h=None):
    cls = "film film--tall" if tall else "film"
    return f'''<div class="{cls}">
  <video controls preload="none" playsinline poster="{poster}" aria-label="{html.escape(label, quote=True)}"><source src="{src}" type="video/mp4"></video>
  <button class="play" type="button" aria-label="Play video: {html.escape(label, quote=True)}"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span></button>
</div>'''

COVER = '''<div class="cover" role="img" aria-label="Book cover of dear Ego, dear Heart by Melissa Heathers">
  <div class="cover-art"></div>
  <div class="cover-title" aria-hidden="true"><span class="d">dear</span><span class="b">Ego</span><span class="d">dear</span><span class="b">Hea</span><span class="b">rt</span></div>
  <svg class="cover-line" viewBox="0 0 100 40" preserveAspectRatio="none" aria-hidden="true"><path d="M0,38 C30,37 62,33 80,25" /><path d="M84,23 C74,16 76,6 81,7 C83,7.5 84,9 84,10 C84,9 85,7.5 87,7 C92,6 94,16 84,23 Z" /></svg>
  <span class="cover-author" aria-hidden="true">melissa heathers</span>
</div>'''
