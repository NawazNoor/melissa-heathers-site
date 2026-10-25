from lib import *

ARR = '<span class="arr">→</span>'

def home():
    path = "/"
    title = "Melissa Heathers — Author, Speaker & Host of The Book Crawl"
    desc = "Melissa Heathers is the author of Dear Ego, Dear Heart, creator of The Goddess Gems, and host of The Book Crawl. Every story is worth savouring."
    body = T(f'''
<section class="hero" id="top">
  <span class="ink ink--a" aria-hidden="true"></span>
  <span class="ink ink--b" aria-hidden="true"></span>
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Author · Speaker · Host of The Book Crawl</p>
      <h1 data-split>Every story is worth <em>savouring.</em></h1>
      <p class="lede">Melissa Heathers writes about the quiet war between the mind and the heart, and hosts the television show that gives authors a seat at the table.</p>
      <div class="btn-row">
        <a class="btn" href="/dear-ego-dear-heart/">Read dear EGO dear HEART {ARR}</a>
        <a class="btn btn--ghost" href="/melissa-heathers/">Meet Melissa</a>
      </div>
    </div>
    <div class="hero-stage">
      <div class="ink-stage" aria-hidden="true"></div>
      <img class="portrait" src="/assets/img/melissa-heathers.webp" width="523" height="792" fetchpriority="high" alt="Melissa Heathers in a black blazer, smiling and holding her poetry book dear Ego, dear Heart">
      <span class="chip chip--1"><b>Poetry</b>dear EGO dear HEART</span>
      <span class="chip chip--2"><b>Television</b>The Book Crawl</span>
      <span class="chip chip--3"><b>Children’s stories</b>The Goddess Gems</span>
    </div>
  </div>
  <span class="scroll-cue" aria-hidden="true"></span>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker-track">
    <span>Think. Ink. Drink.</span><span>Every story is worth savouring.</span><span>dear EGO dear HEART</span><span>The Book Crawl</span><span>The Goddess Gems</span>
    <span>Think. Ink. Drink.</span><span>Every story is worth savouring.</span><span>dear EGO dear HEART</span><span>The Book Crawl</span><span>The Goddess Gems</span>
  </div>
</div>

<section class="section" id="begin">
  <div class="wrap">
    <div class="center reveal">
      <p class="eyebrow">Start here</p>
      <h2>Where would you like to <em>begin?</em></h2>
      <p class="lede">Five doors into one story world. Choose the one that feels like you.</p>
    </div>
    <div class="grid paths" style="margin-top:3rem">
      <a class="card path tilt reveal" style="--d:0" href="/dear-ego-dear-heart/">
        <span class="num">01</span>
        <h3>I’m here for the poetry</h3>
        <p>Letters between the ego and the heart. A gentle companion for seasons of change and the road home to yourself.</p>
        <span class="link-arrow">Explore the book {ARR}</span>
      </a>
      <a class="card path tilt reveal" style="--d:1" href="/the-book-crawl/">
        <span class="num">02</span>
        <h3>I’m an author</h3>
        <p>Step beyond the page into television, podcasting and a public-house table with your story on it.</p>
        <span class="link-arrow">Join the Crawl {ARR}</span>
      </a>
      <a class="card path tilt reveal" style="--d:2" href="/goddess-gems/">
        <span class="num">03</span>
        <h3>I’m reading with a child</h3>
        <p>A gem-powered story world for emotional strength and kindness. Meet Rose Court and her friend Luna.</p>
        <span class="link-arrow">Enter the story world {ARR}</span>
      </a>
      <a class="card path tilt reveal" style="--d:3" href="/press/">
        <span class="num">04</span>
        <h3>I’m planning an event or interview</h3>
        <p>Bios, headshot, speaking themes and the quickest way to get in touch.</p>
        <span class="link-arrow">Press &amp; booking {ARR}</span>
      </a>
      <a class="card path tilt reveal" style="--d:4" href="/meditations/">
        <span class="num">05</span>
        <h3>I need a quiet minute</h3>
        <p>Three complimentary meditations, offered from the soul.</p>
        <span class="link-arrow">Take a breath {ARR}</span>
      </a>
    </div>
  </div>
</section>

<section class="section section--blush" id="book">
  <span class="ink ink--a" aria-hidden="true" style="top:auto;bottom:-20%;right:auto;left:-30%;opacity:.6"></span>
  <div class="wrap split split--flip">
    <div class="reveal" style="padding:1rem 0">{COVER}</div>
    <div class="reveal" style="--d:1">
      <p class="eyebrow">The main book</p>
      <h2>dear <em>Ego,</em> dear <em>Heart</em></h2>
      <p class="serif-quote" style="margin-bottom:1.2rem">A poetic tale of the war within.</p>
      <p>Written as a series of letters between the ego and the heart, this poetry collection explores the inner war between the mind and the heart — a reflective journey through duality, identity and coming home to yourself.</p>
      <div class="btn-row">
        <a class="btn" href="[[BUY]]" rel="noopener">Buy on Amazon.ca {ARR}</a>
        <a class="btn btn--ghost" href="/dear-ego-dear-heart/">About the book</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="watch">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Watch</p>
      <h2>Melissa Heathers, <em>in her own words.</em></h2>
      <p class="lede">Press play to meet the author of dear EGO dear HEART.</p>
      <p><a class="link-arrow" href="/melissa-heathers/">Read her story {ARR}</a></p>
    </div>
    <div class="reveal" style="--d:1">
      {film("[[VIDEO]]", "/assets/img/video-poster.jpg", "Melissa Heathers, author of Dear Ego, Dear Heart")}
      <p class="film-cap">Melissa Heathers, author of dear EGO dear HEART.</p>
    </div>
  </div>
</section>

<section class="section section--tight" style="padding-top:0">
  <div class="wrap">
    <div class="split split--c">
      <div class="reveal">
        <img src="/assets/img/melissa-heathers-480.webp" width="480" height="727" loading="lazy" decoding="async" alt="Portrait of Melissa Heathers holding her book" style="width:min(340px,70%);margin-inline:auto">
      </div>
      <div class="reveal" style="--d:1">
        <p class="eyebrow">About Melissa</p>
        <h2>Storytelling, strategy <em>&amp; soul.</em></h2>
        <p>Melissa Heathers is an author, speaker and creative visionary, and the founder, executive producer and host of The Book Crawl. She is devoted to transforming books into platforms — and to positioning authors as thought leaders who shape culture, healing and conversation.</p>
        <div class="quote-block"><p class="serif-quote" style="margin:0">Every story is worth savouring.</p><cite>Melissa Heathers · Think. Ink. Drink.</cite></div>
        <p><a class="link-arrow" href="/melissa-heathers/">More about Melissa {ARR}</a></p>
      </div>
    </div>
  </div>
</section>

{wave("var(--cream)", "var(--plum)")}
<section class="section section--plum" id="crawl">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">The Book Crawl</p>
      <h2>Think. Ink. <em>Drink.</em></h2>
      <p class="lede">A televised literary experience where storytelling meets soul and conversation flows as smoothly as a well-crafted pint of ale.</p>
      <p>Streaming on EzWay TV under The Women’s Channel, The Book Crawl carries authors beyond the page into media visibility, broadcast exposure and meaningful public dialogue.</p>
      <div class="btn-row">
        <a class="btn btn--light" href="/the-book-crawl/">How it works {ARR}</a>
        <a class="btn btn--ghost-light" href="/contact/?topic=book-crawl">Be a guest</a>
      </div>
    </div>
    <div class="reveal" style="--d:1">
      <ul class="facts">
        <li><span>Host</span><span>Melissa Heathers</span></li>
        <li><span>Streams on</span><span>EzWay TV · The Women’s Channel</span></li>
        <li><span>Format</span><span>Television · podcast · social</span></li>
        <li><span>For</span><span>Authors with a story worth telling</span></li>
      </ul>
    </div>
  </div>
</section>
{wave("var(--plum)", "var(--cream)", flip=True)}

<section class="section" id="gems">
  <div class="wrap split split--flip">
    <div class="reveal">
      <div class="card" style="background:linear-gradient(150deg,#fff3cf,#ffd9c7 55%,#e7c4f0);text-align:center;padding:3rem 1.5rem">
        <p class="eyebrow" style="justify-content:center">Book 1</p>
        <h3 style="font-size:2.3rem">Rose Court</h3>
        <p class="serif-quote" style="font-size:1.5rem;margin:0">The Goddess Gem of Love</p>
      </div>
    </div>
    <div class="reveal" style="--d:1">
      <p class="eyebrow">For young readers</p>
      <h2>The Goddess <em>Gems</em></h2>
      <p>A heart-centred story world designed to help children strengthen emotional regulation and inner resilience through the symbolic power of gemstones and emotional strength.</p>
      <p><span class="pill">Next: Series 2 · Sunlite · coming soon</span></p>
      <div class="btn-row"><a class="btn" href="/goddess-gems/">Enter the story world {ARR}</a></div>
    </div>
  </div>
</section>

<section class="section section--blush center" style="padding:clamp(4rem,8vw,7rem) 0">
  <div class="wrap reveal">
    <h2>Every story is worth savouring.<br><em>Start with yours.</em></h2>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="/contact/">Say hello {ARR}</a>
      <a class="btn btn--ghost" href="[[BUY]]" rel="noopener">Get the book</a>
    </div>
  </div>
</section>
''')
    schema = [
        {"@type": "WebSite", "@id": SITE_ID, "url": BASE + "/", "name": "Melissa Heathers", "inLanguage": "en-CA", "publisher": {"@id": PERSON_ID}},
        PERSON,
        {"@type": "VideoObject", "name": "Melissa Heathers, author of Dear Ego, Dear Heart",
         "description": "A video featuring Melissa Heathers, author of Dear Ego, Dear Heart.",
         "thumbnailUrl": BASE + "/assets/img/video-poster.jpg", "contentUrl": VIDEO,
         "uploadDate": TODAY, "publisher": {"@id": PERSON_ID}},
    ]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active="/", preload_img="/assets/img/melissa-heathers.webp")


def book():
    path = "/dear-ego-dear-heart/"
    title = "Dear Ego, Dear Heart by Melissa Heathers — A Poetic Tale"
    desc = "A poetic tale of the war within, written as letters between the ego and the heart. Meet Dear Ego, Dear Heart by Melissa Heathers and find where to buy."
    crumbs = [("Home", "/"), ("dear EGO dear HEART", path)]
    faq = [
        ("What is Dear Ego, Dear Heart about?",
         "It is a poetic exploration of the inner dialogue we all carry: the quiet war between who we think we must be and who we truly are. It is written as a series of letters between the ego and the heart."),
        ("Is it a poetry book?",
         "Yes. Dear Ego, Dear Heart is a poetry collection that explores duality, healing and personal growth through poetic prose and soulful inquiry."),
        ("Who is it for?",
         "Readers navigating change, healing, or the courage it takes to return home to themselves, and anyone who loves poetry that feels like an honest conversation."),
        ("Where can I buy it?",
         "Dear Ego, Dear Heart is available on Amazon.ca. A Kindle edition is also listed there."),
        ("Can I meet the author or get a signed copy?",
         "Melissa has held book signings at Indigo Kitchener. Follow her on Facebook, or use the contact page, to hear about future events."),
        ("Who is Melissa Heathers?",
         "Melissa Heathers is an author, speaker and creative visionary, and the founder, executive producer and host of The Book Crawl, which streams on EzWay TV under The Women’s Channel. She is also the creator of the children’s series The Goddess Gems."),
    ]
    faq_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faq)
    body = T(f'''
<section class="page-hero">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split split--a">
    <div>
      {crumbs_html(crumbs)}
      <p class="eyebrow">Poetry · by Melissa Heathers</p>
      <h1 class="wm"><span class="d">dear</span>Ego<span class="d">dear</span>Heart<span class="sr-only"> by Melissa Heathers: a poetic tale of the war within</span></h1>
      <p class="lede">A poetic tale of the war within, written as letters between the ego and the heart.</p>
      <div class="btn-row">
        <a class="btn" href="[[BUY]]" rel="noopener">Buy on Amazon.ca {ARR}</a>
        <a class="btn btn--ghost" href="#voices">Hear both voices</a>
      </div>
    </div>
    <div class="reveal in">{COVER}</div>
  </div>
</section>

<section class="section" id="about-the-book">
  <div class="wrap split split--top">
    <div class="reveal">
      <p class="eyebrow">About the book</p>
      <h2>A quiet war, <em>told gently.</em></h2>
      <p>Every one of us carries two voices. One insists on who we think we must be. The other remembers who we truly are. <strong>Dear Ego, Dear Heart</strong> gives them a page to speak to each other.</p>
      <p>Written as a series of letters between the ego and the heart, this poetry collection explores the inner war between the mind and the heart: a reflective journey through duality, identity and coming home to oneself.</p>
      <p>Through poetic prose and soulful inquiry, it invites you to witness your own duality with compassion instead of judgment.</p>
    </div>
    <div class="reveal" style="--d:1">
      <div class="card">
        <h3>At a glance</h3>
        <ul class="facts">
          <li><span>Author</span><span>Melissa Heathers</span></li>
          <li><span>Genre</span><span>Poetry</span></li>
          <li><span>Form</span><span>Letters between ego and heart</span></li>
          <li><span>Themes</span><span>Duality · identity · healing · coming home</span></li>
          <li><span>Available</span><span><a href="[[BUY]]" rel="noopener">Amazon.ca</a></span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--blush" id="voices">
  <div class="wrap">
    <div class="center reveal" style="margin-bottom:2.6rem">
      <p class="eyebrow">An invitation</p>
      <h2>Hear both <em>voices.</em></h2>
      <p class="lede">Ego and heart rarely agree. Choose a voice, then ask for another.</p>
    </div>
    <div class="voices reveal" id="voices-widget" data-voice="heart" style="--d:1">
      <div class="voice-toggle" role="group" aria-label="Choose a voice">
        <button type="button" data-voice="ego" aria-pressed="false">Ego</button>
        <button type="button" data-voice="heart" aria-pressed="true">Heart</button>
      </div>
      <p class="voice-line" id="voice-line" aria-live="polite">You’re allowed to be unfinished.</p>
      <div class="voice-foot">
        <button type="button" class="voice-next" id="voice-next">Another voice →</button>
        <span>Written for this page as an invitation. These lines are not excerpts from the book.</span>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Who it’s for</p>
      <h2>For the reader in the <em>middle of something.</em></h2>
      <ul class="ticks">
        <li>Readers navigating change, healing or a season of transition</li>
        <li>Anyone curious about the conversation between the mind and the heart</li>
        <li>Poetry lovers who want something honest and gentle</li>
        <li>Gift-givers looking for a thoughtful, reflective book</li>
      </ul>
      <div class="btn-row"><a class="btn" href="[[BUY]]" rel="noopener">Get your copy {ARR}</a></div>
    </div>
    <div class="reveal" style="--d:1">
      {film("[[VIDEO]]", "/assets/img/video-poster.jpg", "Melissa Heathers, author of Dear Ego, Dear Heart")}
      <p class="film-cap">Melissa Heathers, author of dear EGO dear HEART.</p>
    </div>
  </div>
</section>

{wave("var(--cream)", "var(--plum)")}
<section class="section section--plum" id="author">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split split--d">
    <div class="reveal"><img src="/assets/img/melissa-heathers-480.webp" width="480" height="727" loading="lazy" decoding="async" alt="Melissa Heathers holding dear Ego, dear Heart" style="width:min(330px,80%);margin-inline:auto"></div>
    <div class="reveal" style="--d:1">
      <p class="eyebrow">About the author</p>
      <h2>Melissa <em>Heathers</em></h2>
      <p class="lede">Author, speaker and creative visionary. Founder, executive producer and host of The Book Crawl.</p>
      <p>She leads from lived experience as an author herself, blending storytelling, strategy and soul to create refined, elevated spaces where words are honoured and wisdom is poured.</p>
      <div class="btn-row">
        <a class="btn btn--light" href="/melissa-heathers/">Meet Melissa {ARR}</a>
        <a class="btn btn--ghost-light" href="/contact/?topic=speaking">Invite her to speak</a>
      </div>
    </div>
  </div>
</section>
{wave("var(--plum)", "var(--cream)", flip=True)}

<section class="section section--tight">
  <div class="wrap split split--top">
    <div class="reveal">
      <p class="eyebrow">In person</p>
      <h2>Meet her at a <em>signing.</em></h2>
      <p>Melissa has signed copies of dear EGO dear HEART at Indigo Kitchener, on Fairway Road South, Kitchener.</p>
      <ul class="timeline">
        <li><time datetime="2026-02-22">February 22, 2026</time><h3>Book signing at Indigo Kitchener</h3></li>
        <li><time datetime="2026-07-18">July 18, 2026</time><h3>Second signing at Indigo Kitchener</h3></li>
      </ul>
      <p class="small muted" style="margin-top:1.5rem">Want to know about the next one? <a href="[[FACEBOOK]]" rel="me noopener">Follow Melissa on Facebook</a> or <a href="/contact/">get in touch</a>.</p>
    </div>
    <div class="reveal" style="--d:1">
      <h2>Questions, <em>answered.</em></h2>
      <div class="faq" style="max-width:none">{faq_html}</div>
    </div>
  </div>
</section>

<section class="section section--blush center" style="padding:clamp(4rem,8vw,7rem) 0">
  <div class="wrap reveal">
    <h2>Ready to listen to <em>both voices?</em></h2>
    <p class="lede" style="margin-inline:auto">dear EGO dear HEART, by Melissa Heathers.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="[[BUY]]" rel="noopener">Buy on Amazon.ca {ARR}</a>
      <a class="btn btn--ghost" href="/goddess-gems/">Explore The Goddess Gems</a>
    </div>
  </div>
</section>
''')
    schema = [
        PERSON,
        {"@type": "Book", "@id": BASE + path + "#book", "name": "dear Ego, dear Heart", "alternativeHeadline": "A Poetic Tale of The War Within",
         "author": {"@id": PERSON_ID}, "genre": "Poetry", "inLanguage": "en", "isbn": ISBN_DEDH, "url": BASE + path,
         "image": BASE + "/assets/img/og-image.jpg",
         "description": "A poetic tale of the war within, written as a series of letters between the ego and the heart: a reflective journey through duality, identity and coming home to oneself.",
         "sameAs": [BUY]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
        {"@type": "VideoObject", "name": "Melissa Heathers, author of Dear Ego, Dear Heart",
         "description": "A video featuring Melissa Heathers, author of Dear Ego, Dear Heart.",
         "thumbnailUrl": BASE + "/assets/img/video-poster.jpg", "contentUrl": VIDEO, "uploadDate": TODAY},
        breadcrumbs(crumbs),
    ]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active=path)


def about():
    path = "/melissa-heathers/"
    title = "About Melissa Heathers — Author, Speaker, Executive Producer"
    desc = "Meet Melissa Heathers: author of Dear Ego, Dear Heart, creator of The Goddess Gems, and founder and host of The Book Crawl. Her story, philosophy and milestones."
    crumbs = [("Home", "/"), ("About Melissa", path)]
    body = T(f'''
<section class="page-hero">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split split--b">
    <div>
      {crumbs_html(crumbs)}
      <p class="eyebrow">Author · Speaker · Creative visionary</p>
      <h1 data-split>Melissa <em>Heathers</em></h1>
      <p class="lede">Author, speaker, and founder, executive producer and host of The Book Crawl. She believes a book is only the beginning of the conversation.</p>
      <div class="btn-row">
        <a class="btn" href="/contact/?topic=speaking">Invite Melissa {ARR}</a>
        <a class="btn btn--ghost" href="/press/">Press &amp; media kit</a>
      </div>
    </div>
    <div class="reveal in" style="position:relative">
      <img src="/assets/img/melissa-heathers.webp" width="523" height="792" fetchpriority="high" alt="Melissa Heathers in a black blazer, smiling and holding her book dear Ego, dear Heart" style="width:min(380px,90%);margin-inline:auto">
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split split--c split--top">
    <div class="reveal">
      <p class="eyebrow">Her story</p>
      <h2>Words, honoured. <em>Wisdom, poured.</em></h2>
      <div class="quote-block"><p class="serif-quote" style="margin:0">Every story is worth savouring.</p><cite>Her philosophy</cite></div>
    </div>
    <div class="reveal" style="--d:1">
      <p>Melissa Heathers is an author, speaker and creative visionary, and the founder, executive producer and host of <a href="/the-book-crawl/">The Book Crawl</a>. She is devoted to transforming books into platforms and to positioning authors as thought leaders who shape culture, healing and conversation.</p>
      <p>Her poetry collection, <a href="/dear-ego-dear-heart/">Dear Ego, Dear Heart</a>, explores the inner war between the mind and the heart as a series of letters: a reflective journey through duality, identity and coming home to oneself.</p>
      <p>For younger readers she created <a href="/goddess-gems/">The Goddess Gems: A Mystical Adventure</a>, a heart-centred story world that uses the symbolic power of gemstones to help children strengthen emotional regulation and inner resilience.</p>
      <p>As the visionary behind The Book Crawl, streaming on EzWay TV under The Women’s Channel, she is building a movement that supports authors in stepping beyond the page into media visibility, broadcast exposure and meaningful public dialogue. She is also a co-founder of the Authors and Book Lovers Visibility Summit.</p>
      <p>Leading from lived experience as an author herself, Melissa blends storytelling, strategy and soul, creating refined, elevated spaces where words are honoured and wisdom is poured.</p>
    </div>
  </div>
</section>

<section class="section section--blush">
  <div class="wrap">
    <div class="center reveal">
      <p class="eyebrow">What she does</p>
      <h2>Four ways she <em>shares stories.</em></h2>
    </div>
    <div class="grid cols-2" style="margin-top:3rem">
      <div class="card tilt reveal"><h3>Author</h3><p>Dear Ego, Dear Heart: a poetic tale of the war within, written as letters between the ego and the heart.</p><a class="link-arrow" href="/dear-ego-dear-heart/">The book {ARR}</a></div>
      <div class="card tilt reveal" style="--d:1"><h3>Executive Producer &amp; Host</h3><p>The Book Crawl, a televised literary experience streaming on EzWay TV under The Women’s Channel.</p><a class="link-arrow" href="/the-book-crawl/">The show {ARR}</a></div>
      <div class="card tilt reveal" style="--d:2"><h3>Children’s storyteller</h3><p>The Goddess Gems: A Mystical Adventure, a story world for emotional strength and inner resilience.</p><a class="link-arrow" href="/goddess-gems/">The series {ARR}</a></div>
      <div class="card tilt reveal" style="--d:3"><h3>Speaker</h3><p>Conversations about the ego and the heart, turning books into platforms, and story as a tool for resilience.</p><a class="link-arrow" href="/contact/?topic=speaking">Invite Melissa {ARR}</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split split--top">
    <div class="reveal">
      <p class="eyebrow">Think. Ink. Drink.</p>
      <h2>Three words, <em>one table.</em></h2>
      <p class="lede">Melissa’s signature sums up her world: think, put it in ink, and pour the conversation.</p>
      <ol class="numbered" style="margin-top:2rem">
        <li><h3>Think</h3><p>The idea worth sitting with.</p></li>
        <li><h3>Ink</h3><p>The words that make it real.</p></li>
        <li><h3>Drink</h3><p>The conversation that turns a story into a community.</p></li>
      </ol>
    </div>
    <div class="reveal" style="--d:1">
      <p class="eyebrow">Milestones</p>
      <ul class="timeline">
        <li><time datetime="2025-03">March 2025</time><h3>Guest on the Live With CDP Talk Show</h3><p>Season 10, Episode 17, speaking about Dear Ego, Dear Heart.</p></li>
        <li><time datetime="2026-02">February 2026</time><h3>First book signing at Indigo Kitchener</h3></li>
        <li><time datetime="2026-05">May 2026</time><h3>The Book Crawl announced as a media visibility platform</h3><p>On The Women’s Channel, distributed on Roku, Apple TV and Amazon Fire TV.</p></li>
        <li><time datetime="2026-07">July 2026</time><h3>Second book signing at Indigo Kitchener</h3></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--blush center" style="padding:clamp(4rem,8vw,7rem) 0">
  <div class="wrap reveal">
    <h2>Let’s make a story <em>worth savouring.</em></h2>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="/contact/">Get in touch {ARR}</a>
      <a class="btn btn--ghost" href="/press/">Press &amp; media kit</a>
    </div>
  </div>
</section>
''')
    schema = [PERSON, breadcrumbs(crumbs),
              {"@type": "ProfilePage", "url": BASE + path, "name": "About Melissa Heathers", "mainEntity": {"@id": PERSON_ID}}]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active=path)


def crawl():
    path = "/the-book-crawl/"
    title = "The Book Crawl — Where Authors Become Thought Leaders"
    desc = "The Book Crawl is a televised literary experience hosted by Melissa Heathers, streaming on EzWay TV under The Women’s Channel. Think. Ink. Drink. Be a guest."
    crumbs = [("Home", "/"), ("The Book Crawl", path)]
    body = T(f'''
<section class="page-hero section--plum">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap split split--b">
    <div>
      {crumbs_html(crumbs)}
      <p class="eyebrow">A televised literary experience</p>
      <h1 data-split>The Book <em>Crawl</em></h1>
      <p class="lede">Think. Ink. Drink. Where storytelling meets soul and conversation flows as smoothly as a well-crafted pint of ale.</p>
      <div class="btn-row">
        <a class="btn btn--light" href="/contact/?topic=book-crawl">Apply to be a guest {ARR}</a>
        <a class="btn btn--ghost-light" href="[[EZWAY]]" rel="noopener">Watch &amp; listen on eZWay</a>
      </div>
    </div>
    <div class="reveal in">
      <ul class="facts">
        <li><span>Host</span><span>Melissa Heathers</span></li>
        <li><span>Streams on</span><span>EzWay TV</span></li>
        <li><span>Channel</span><span>The Women’s Channel</span></li>
        <li><span>Also on</span><span>Roku · Apple TV · Amazon Fire TV</span></li>
      </ul>
    </div>
  </div>
</section>
{wave("var(--plum)", "var(--cream)", flip=True)}

<section class="section" id="what">
  <div class="wrap split split--top">
    <div class="reveal">
      <p class="eyebrow">What it is</p>
      <h2>Beyond the page, <em>into the room.</em></h2>
      <p>The Book Crawl is a modern media visibility platform that helps authors build authority and expand their reach through television, podcasting, social media and strategic brand positioning.</p>
      <p>It is part show, part movement: a public house for words, where every author’s story is honoured, and where wisdom is poured.</p>
      <div class="quote-block">
        <p class="serif-quote" style="margin:0">Every story is worth savouring, and every author deserves a platform that reflects the depth of what they have created.</p>
        <cite>Melissa Heathers, founder &amp; host</cite>
      </div>
    </div>
    <div class="reveal" style="--d:1">
      <div class="card">
        <h3>What authors receive</h3>
        <ul class="ticks">
          <li>A televised interview on The Book Crawl</li>
          <li>Podcast appearances</li>
          <li>Multi-platform social media promotion</li>
          <li>Brand positioning assets</li>
          <li>Access to speaking and summit opportunities</li>
        </ul>
        <a class="link-arrow" href="/contact/?topic=book-crawl">Tell us about your book {ARR}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--blush">
  <div class="wrap">
    <div class="center reveal">
      <p class="eyebrow">How to begin</p>
      <h2>Three steps to the <em>table.</em></h2>
    </div>
    <ol class="numbered grid cols-3" style="margin-top:3rem">
      <li class="reveal"><h3>Introduce yourself</h3><p>Tell us about you and your book through the contact form.</p></li>
      <li class="reveal" style="--d:1"><h3>Hear back</h3><p>You’ll hear about fit and next steps.</p></li>
      <li class="reveal" style="--d:2"><h3>Step into the public house</h3><p>Share your story on camera and carry it further.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap split split--top">
    <div class="reveal">
      <p class="eyebrow">On the road &amp; on the air</p>
      <h2>Conversations that <em>keep going.</em></h2>
      <p>The Book Crawl has gone live from New York and Mystic, Connecticut, and continues the conversation through its podcast, <em>On the Air with The Book Crawl</em>.</p>
      <p>Melissa is also a co-founder of the Authors and Book Lovers Visibility Summit.</p>
      <p><a class="link-arrow" href="[[EZWAY]]" rel="noopener">Episodes &amp; news on eZWay {ARR}</a></p>
    </div>
    <div class="reveal" style="--d:1">
      <h3>Recent conversations</h3>
      <ul class="press-list">
        <li class="card press-item press-item--sm"><span class="kind">Featured author</span><div><h3>Grace C.W. Liu</h3><p>Author of Pearl of Grace®</p></div></li>
        <li class="card press-item press-item--sm"><span class="kind">Podcast</span><div><h3>Carroll Patrizi</h3><p>On Surrender the Movement</p></div></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--plum center" style="padding:clamp(4rem,8vw,7rem) 0">
  <span class="ink ink--a" aria-hidden="true"></span>
  <div class="wrap reveal">
    <h2>Your story belongs <em>at the table.</em></h2>
    <p class="lede" style="margin-inline:auto">Pull up a chair. The Book Crawl is waiting.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--light" href="/contact/?topic=book-crawl">Apply to be a guest {ARR}</a>
    </div>
  </div>
</section>
''')
    schema = [PERSON, breadcrumbs(crumbs),
              {"@type": "TVSeries", "name": "The Book Crawl", "url": BASE + path, "creator": {"@id": PERSON_ID},
               "genre": "Author interviews and literary talk",
               "description": "A televised literary experience hosted by Melissa Heathers, streaming on EzWay TV under The Women's Channel, helping authors build authority and expand reach through television, podcasting, social media and brand positioning."}]
    return dict(path=path, title=title, desc=desc, body=body, schema=schema, active=path, dark_top=True)
