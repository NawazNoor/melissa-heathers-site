from lib import *

ARR = '<span class="arr">→</span>'
TEASER = "/assets/video/sunlite-teaser.mp4"
TEASER_POSTER = "/assets/video/sunlite-poster.jpg"


def gems():
    path = "/goddess-gems/"
    title = "The Goddess Gems — A Mystical Adventure for Children"
    desc = "A heart-centred children's story world by Melissa Heathers. Meet Rose Court, the Goddess Gem of Love, and her friend Luna. Series 2: Sunlite is coming soon."
    crumbs = [("Home", "/"), ("The Goddess Gems", path)]
    body = T(f'''
<section class="page-hero">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split split--a">
    <div>
      {crumbs_html(crumbs)}
      <p class="eyebrow">Children’s series · by Melissa Heathers</p>
      <h1 data-split>The Goddess <em>Gems</em></h1>
      <p class="lede">A mystical adventure and a heart-centred story world, designed to help children strengthen emotional regulation and inner resilience through the symbolic power of gemstones and emotional strength.</p>
      <div class="btn-row">
        <a class="btn" href="[[GG_AMAZON]]" rel="noopener">Get Book 1: Rose Court {ARR}</a>
        <a class="btn btn--ghost" href="#sunlite">Series 2: Sunlite</a>
      </div>
    </div>
    <div class="reveal in">
      <div class="card" style="background:linear-gradient(150deg,#fff3cf,#ffd9c7 52%,#e7c4f0);text-align:center;padding:3.4rem 1.5rem">
        <p class="eyebrow" style="justify-content:center">Book 1</p>
        <h2 style="margin-bottom:.2em">Rose Court</h2>
        <p class="serif-quote" style="font-size:1.6rem;margin:0">The Goddess Gem of Love</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="book-1">
  <div class="wrap split split--top">
    <div class="reveal">
      <p class="eyebrow">Book 1</p>
      <h2>Rose Court, <em>the Goddess Gem of Love</em></h2>
      <p>When the warmth of the Valley of Heartland begins to fade, Rose Court sets out with her loyal companion Luna, the wise and loving dog, to bring love back to the places that need it most.</p>
      <p>Their journey reminds young readers that kindness shared freely can light even the darkest places, and that big feelings can be met with gentleness.</p>
      <div class="btn-row"><a class="btn" href="[[GG_AMAZON]]" rel="noopener">Find the book {ARR}</a></div>
      <p class="small muted" style="margin-top:1rem">Listed on Amazon.co.uk. Also see <a href="[[AMAZON_AUTHOR]]" rel="noopener">Melissa’s Amazon author page</a>.</p>
    </div>
    <div class="reveal" style="--d:1">
      <div class="grid cols-2" style="gap:1rem">
        <div class="card character tilt" style="--g1:#f5a5b8;--g2:#d4608f"><span class="glyph" aria-hidden="true">R</span><h3>Rose Court</h3><p class="small">The Goddess Gem of Love. A gentle gem keeper who brings comfort and affection.</p></div>
        <div class="card character tilt" style="--g1:#f4c16d;--g2:#d9893a"><span class="glyph" aria-hidden="true">L</span><h3>Luna</h3><p class="small">A wise, watchful golden retriever who senses troubled hearts before anyone else.</p></div>
        <div class="card character tilt" style="--g1:#8bb9d6;--g2:#4f78a8;grid-column:1 / -1"><span class="glyph" aria-hidden="true">J</span><h3>Johnny</h3><p class="small">A young boy who feels sad and fears he has lost his light, and who finds his way back to joy.</p></div>
      </div>
    </div>
  </div>
</section>

{wave("var(--cream)", "var(--plum)")}
<section class="section section--plum" id="sunlite">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Coming soon</p>
      <h2>Series 2: <em>Sunlite</em></h2>
      <p class="lede">A little girl named Honey has lost her joy. Luna feels it before anyone else, and light answers.</p>
      <p>In the next story, Luna calls on Sunlite, the crystal of sunlight who brings happiness and joy, to come down to Earth and help Honey work through her sadness and find her joy again, through the simple things in life.</p>
      <p><span class="pill">Still being written</span></p>
      <div class="btn-row">
        <a class="btn btn--light" href="/contact/?topic=goddess-gems">Be the first to hear {ARR}</a>
      </div>
    </div>
    <div class="reveal" style="--d:1">
      {film(TEASER, TEASER_POSTER, "Series 2 Sunlite teaser: Honey, Luna and Sunlite", tall=True)}
      <p class="film-cap center" style="color:rgba(255,248,242,.75)">A first look at Series 2: Sunlite.</p>
    </div>
  </div>
</section>
{wave("var(--plum)", "var(--cream)", flip=True)}

<section class="section">
  <div class="wrap">
    <div class="center reveal">
      <p class="eyebrow">Why gemstones?</p>
      <h2>Feelings, <em>given a face.</em></h2>
      <p class="lede">Each Goddess Gem carries an emotional strength. Children meet that strength as a character they can talk to, remember and take with them.</p>
    </div>
    <div class="grid cols-3" style="margin-top:3rem">
      <div class="card tilt reveal"><h3>Love</h3><p>Rose Court, the Goddess Gem of Love, models self-love, comfort and care.</p></div>
      <div class="card tilt reveal" style="--d:1"><h3>Joy</h3><p>Sunlite, in Series 2, brings happiness, confidence and the warmth of simple things.</p></div>
      <div class="card tilt reveal" style="--d:2"><h3>And more to come</h3><p>The story world is growing, one gem and one feeling at a time.</p></div>
    </div>
  </div>
</section>

<section class="section section--blush center" style="padding:clamp(4rem,8vw,7rem) 0">
  <div class="wrap reveal">
    <h2>Read with a child. <em>Feel with them.</em></h2>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="[[GG_AMAZON]]" rel="noopener">Get Book 1 {ARR}</a>
      <a class="btn btn--ghost" href="/contact/?topic=goddess-gems">Ask about Series 2</a>
    </div>
  </div>
</section>
''')
    schema = [
        PERSON, breadcrumbs(crumbs),
        {"@type": "CreativeWorkSeries", "@id": BASE + path + "#series", "name": "The Goddess Gems: A Mystical Adventure",
         "author": {"@id": PERSON_ID}, "url": BASE + path, "audience": {"@type": "PeopleAudience", "suggestedMinAge": 3, "suggestedMaxAge": 9},
         "description": "A heart-centred children's story world designed to help children strengthen emotional regulation and inner resilience through the symbolic power of gemstones."},
        {"@type": "Book", "name": "The Goddess Gems: A Mystical Gem Adventure: Rose Court, The Goddess Gem of Love", "isbn": ISBN_ROSE,
         "author": {"@id": PERSON_ID}, "isPartOf": {"@id": BASE + path + "#series"}, "inLanguage": "en", "sameAs": [GG_AMAZON], "url": BASE + path + "#book-1"},
        {"@type": "VideoObject", "name": "Series 2 Sunlite teaser: Honey, Luna and Sunlite",
         "description": "A short animated teaser for Series 2: Sunlite, the next story in The Goddess Gems by Melissa Heathers.",
         "thumbnailUrl": BASE + TEASER_POSTER, "contentUrl": BASE + TEASER, "uploadDate": TODAY, "duration": "PT1M42S"},
    ]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active=path)


def press():
    path = "/press/"
    title = "Press, Interviews & Media Kit — Melissa Heathers"
    desc = "Bios, headshot, quick facts and speaking themes for Melissa Heathers, plus interviews and press for Dear Ego, Dear Heart and The Book Crawl."
    crumbs = [("Home", "/"), ("Press & media kit", path)]
    short = "Melissa Heathers is an author, speaker and creative visionary. She wrote the poetry collection Dear Ego, Dear Heart, created the children’s series The Goddess Gems, and is the founder, executive producer and host of The Book Crawl, streaming on EzWay TV under The Women’s Channel."
    medium = short + " Leading from lived experience as an author herself, she blends storytelling, strategy and soul to create refined, elevated spaces where words are honoured and wisdom is poured. Her philosophy is simple: every story is worth savouring."
    longb = ("Melissa Heathers is an author, speaker and creative visionary, and the founder, executive producer and host of The Book Crawl. She is devoted to transforming books into platforms and to positioning authors as thought leaders who shape culture, healing and conversation. "
             "She is the author of Dear Ego, Dear Heart, a poetic exploration of the inner war between the mind and the heart, written as letters between the ego and the heart: a reflective journey through duality, identity and coming home to oneself. "
             "Melissa is also the creator of the children’s series The Goddess Gems: A Mystical Adventure, a heart-centred story world designed to help children strengthen emotional regulation and inner resilience through the symbolic power of gemstones. "
             "As the visionary behind The Book Crawl, streaming on EzWay TV under The Women’s Channel, she is building a movement that supports authors in stepping beyond the page into media visibility, broadcast exposure and meaningful public dialogue. She is a co-founder of the Authors and Book Lovers Visibility Summit. "
             "Her philosophy is simple and powerful: every story is worth savouring.")
    body = T(f'''
<section class="page-hero">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap">
    {crumbs_html(crumbs)}
    <p class="eyebrow">For hosts, producers &amp; journalists</p>
    <h1 data-split>Press &amp; <em>media kit</em></h1>
    <p class="lede">Everything you need to introduce Melissa Heathers: approved bios, a headshot, quick facts and the best way to book her.</p>
    <div class="btn-row">
      <a class="btn" href="/contact/?topic=press">Request an interview {ARR}</a>
      <a class="btn btn--ghost" href="/assets/img/melissa-heathers.png" download>Download headshot</a>
    </div>
  </div>
</section>

<section class="section" id="kit">
  <div class="wrap split split--c split--top">
    <div class="reveal">
      <h2>Quick <em>facts</em></h2>
      <ul class="facts">
        <li><span>Name</span><span>Melissa Heathers</span></li>
        <li><span>Based in</span><span>Kitchener, Ontario, Canada</span></li>
        <li><span>Roles</span><span>Author · Speaker · Executive Producer &amp; Host</span></li>
        <li><span>Book</span><span>dear Ego, dear Heart (poetry)</span></li>
        <li><span>Children’s series</span><span>The Goddess Gems</span></li>
        <li><span>Show</span><span>The Book Crawl · EzWay TV</span></li>
        <li><span>Signature</span><span>Think. Ink. Drink.</span></li>
      </ul>
      <img src="/assets/img/melissa-heathers-480.webp" width="480" height="727" loading="lazy" decoding="async" alt="Melissa Heathers, press headshot holding her book" style="width:min(260px,70%);margin:2rem auto 0">
    </div>
    <div class="reveal" style="--d:1">
      <h2>Approved <em>bios</em></h2>
      <div class="grid" style="gap:1.2rem">
        <div class="card bio-block"><h3>Short · 50 words</h3><button class="copy" type="button" data-copy="bio-short">Copy</button><p id="bio-short">{short}</p></div>
        <div class="card bio-block"><h3>Medium</h3><button class="copy" type="button" data-copy="bio-medium">Copy</button><p id="bio-medium">{medium}</p></div>
        <div class="card bio-block"><h3>Long</h3><button class="copy" type="button" data-copy="bio-long">Copy</button><p id="bio-long">{longb}</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--blush">
  <div class="wrap split split--top">
    <div class="reveal">
      <p class="eyebrow">Speaking themes</p>
      <h2>What Melissa <em>talks about.</em></h2>
      <ul class="ticks">
        <li>The ego and the heart: living with your inner dialogue</li>
        <li>From page to platform: turning a book into media visibility</li>
        <li>Story as a tool for children’s emotional resilience</li>
      </ul>
      <div class="btn-row"><a class="btn" href="/contact/?topic=speaking">Invite Melissa to speak {ARR}</a></div>
    </div>
    <div class="reveal" style="--d:1">
      <p class="eyebrow">In conversation &amp; in the news</p>
      <ul class="press-list">
        <li><a class="card press-item" href="[[PR]]" rel="noopener"><span class="kind">Press release</span><div><h3>Melissa Heathers and The Book Crawl Are Redefining How Authors Turn Their Pages Into Influence</h3><p>SmallBiz.com · May 2026</p></div><span class="arr">→</span></a></li>
        <li><a class="card press-item" href="[[CDP]]" rel="noopener"><span class="kind">Interview</span><div><h3>Live With CDP Talk Show: Melissa Heathers, author of Dear Ego, Dear Heart</h3><p>Season 10, Episode 17 · March 19, 2025</p></div><span class="arr">→</span></a></li>
        <li><a class="card press-item" href="[[EZWAY]]" rel="noopener"><span class="kind">Profile</span><div><h3>eZWay Wall of Fame: Melissa Heathers</h3><p>The Book Crawl episodes and news</p></div><span class="arr">→</span></a></li>
        <li><a class="card press-item" href="[[AMAZON_AUTHOR]]" rel="noopener"><span class="kind">Author page</span><div><h3>Melissa Heathers on Amazon.ca</h3><p>Books and author biography</p></div><span class="arr">→</span></a></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--plum center" style="padding:clamp(4rem,8vw,7rem) 0">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap reveal">
    <h2>Let’s <em>talk.</em></h2>
    <p class="lede" style="margin-inline:auto">Interviews, podcasts, panels and features. Tell us what you have in mind.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn btn--light" href="/contact/?topic=press">Get in touch {ARR}</a></div>
  </div>
</section>
''')
    items = [
        ("Melissa Heathers and The Book Crawl Are Redefining How Authors Turn Their Pages Into Influence", PRESS_RELEASE),
        ("Live With CDP Talk Show: Melissa Heathers, author of Dear Ego, Dear Heart", CDP),
        ("eZWay Wall of Fame: Melissa Heathers", EZWAY),
        ("Melissa Heathers on Amazon.ca", AMAZON_AUTHOR),
    ]
    schema = [PERSON, breadcrumbs(crumbs),
              {"@type": "CollectionPage", "name": "Press, Interviews & Media Kit", "url": BASE + path, "about": {"@id": PERSON_ID},
               "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": u} for i, (n, u) in enumerate(items)]}}]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active=path)


def meditations():
    path = "/meditations/"
    title = "Mel’s Meditations — Three Complimentary Meditations"
    desc = "Three complimentary meditations from the soul, offered by author Melissa Heathers. Find a quiet place, press play and breathe."
    crumbs = [("Home", "/"), ("Mel’s Meditations", path)]
    cards = ""
    orbs = [("#ffe3c9", "#ee6f57"), ("#f2d0f5", "#9a5db4"), ("#d9f0ea", "#4aa597")]
    names = ["One", "Two", "Three"]
    for i in range(3):
        o1, o2 = orbs[i]
        cards += f'''<div class="card audio-card tilt reveal" style="--d:{i}">
  <div class="orb" style="--o1:{o1};--o2:{o2}" aria-hidden="true"></div>
  <h3>Meditation {names[i]}</h3>
  <audio controls preload="none"><source src="/assets/audio/meditation-{i+1}.mp3" type="audio/mpeg"></audio>
  <p class="soon">The audio for this meditation is being added. Please check back soon.</p>
</div>'''
    body = f'''
<section class="page-hero">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap">
    {crumbs_html(crumbs)}
    <p class="eyebrow">From the soul</p>
    <h1 data-split>Mel’s <em>Meditations</em></h1>
    <p class="lede">Three complimentary meditations, offered with care. Find a quiet place, press play and breathe.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap"><h2 class="sr-only">The three meditations</h2><div class="grid cols-3">{cards}</div>
  <p class="center muted small" style="margin-top:2.5rem">Liked these? Explore <a href="/dear-ego-dear-heart/">dear EGO dear HEART</a>, Melissa’s poetic tale of the war within.</p></div>
</section>
'''
    schema = [PERSON, breadcrumbs(crumbs)]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active=None)


def contact():
    path = "/contact/"
    title = "Contact Melissa Heathers — Book, Speaking, Book Crawl & Press"
    desc = "Get in touch with Melissa Heathers about Dear Ego, Dear Heart, speaking and interviews, being a guest on The Book Crawl, The Goddess Gems, or press."
    crumbs = [("Home", "/"), ("Contact", path)]
    body = T(f'''
<section class="page-hero">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split split--b split--top">
    <div>
      {crumbs_html(crumbs)}
      <p class="eyebrow">Say hello</p>
      <h1 data-split>Let’s <em>talk.</em></h1>
      <p class="lede">Reader questions, speaking invitations, Book Crawl applications and press requests are all welcome. Choose a topic and tell Melissa a little about what you have in mind.</p>
      <ul class="facts" style="margin-top:2rem">
        <li><span>Based in</span><span>Kitchener, Ontario</span></li>
        <li><span>Also find her</span><span><a href="[[FACEBOOK]]" rel="me noopener">Facebook</a></span></li>
        <li><span>The book</span><span><a href="[[BUY]]" rel="noopener">Amazon.ca</a></span></li>
      </ul>
    </div>
    <div class="card reveal in">
      <form id="contact-form" class="form" novalidate>
        <div class="two">
          <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="f-email">Your email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="f-topic">I’m reaching out about</label>
          <select id="f-topic" name="topic">
            <option value="book">dear EGO dear HEART: a question or event</option>
            <option value="book-crawl">Being a guest on The Book Crawl</option>
            <option value="speaking">Speaking or an interview</option>
            <option value="goddess-gems">The Goddess Gems</option>
            <option value="press">Press &amp; media</option>
            <option value="other">Something else</option>
          </select>
        </div>
        <div class="field"><label for="f-msg">Your message</label><textarea id="f-msg" name="message" required></textarea></div>
        <input class="hp" type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div><button class="btn" type="submit">Send message {ARR}</button></div>
        <p id="form-note" class="form-note" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
''')
    schema = [PERSON, breadcrumbs(crumbs), {"@type": "ContactPage", "name": "Contact Melissa Heathers", "url": BASE + path, "about": {"@id": PERSON_ID}}]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active="/contact/")


def notfound():
    body = f'''
<section class="page-hero" style="min-height:80vh;display:grid;align-items:center">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap center">
    <p class="eyebrow" style="justify-content:center">404</p>
    <h1>This page wandered <em>off the page.</em></h1>
    <p class="lede" style="margin-inline:auto">Let’s find your way back to the story.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="/">Back home {ARR}</a>
      <a class="btn btn--ghost" href="/dear-ego-dear-heart/">dear EGO dear HEART</a>
    </div>
  </div>
</section>'''
    return dict(path="/404.html", title="Page not found — Melissa Heathers", desc="This page could not be found.", body=body, schema=[], active=None, noindex=True)
