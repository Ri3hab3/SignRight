#!/usr/bin/env python3
"""Generate the 14 IRS FIRE->IRIS / TY2026 information-return pages.

    python3 scripts/generate_irs_pages.py            # write pages, patch vercel.json/sitemap/index
    python3 scripts/generate_irs_pages.py --check    # validate only, write nothing

Content/facts: scripts/irs_pages_data.py     Tools (HTML+JS): scripts/irs_tools.py
Patching is additive and idempotent: existing vercel.json / sitemap entries are never edited.
"""
import html as H
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import irs_pages_data as D  # noqa: E402
from irs_tools import TOOLS  # noqa: E402

SITE = "https://signright.io"
MAX_BYTES = 100 * 1024

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%235B6CFF'/%3E"
           "%3Cpath d='M8 20 Q12 12 16 20 T24 16' stroke='white' stroke-width='2.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E")

GTM_HEAD = ("<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
            "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
            "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KGBKN6DP');</script>\n"
            "<!-- GA4 -->\n<script async src=\"https://www.googletagmanager.com/gtag/js?id=G-ZFGB4KGK2V\"></script>\n"
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-ZFGB4KGK2V');</script>")
GTM_BODY = '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KGBKN6DP" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'
CLARITY = ('<!-- Microsoft Clarity -->\n<script>(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;'
           't.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","wf378dn1ai");</script>')
ADSENSE = ('<!-- Google AdSense -->\n<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8173139997421073"\n'
           '     crossorigin="anonymous"></script>')

CSS = """
:root{color-scheme:light;--bg:#fff;--text:#1a1a1a;--muted:#5b6470;--line:#e4e7eb;--brand:#0b5fff;--brand-dark:#0846c2;--ok:#0a7d3e;--ok-bg:#e8f6ee;--warn-bg:#fff6e5;--warn:#8a5a00;--card:#f7f9fc;--danger-bg:#fdecec;--danger:#a11a1a;--red:#d32f2f;--red-dark:#b71c1c}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans",Arial,sans-serif;padding-bottom:84px}
.wrap{max-width:760px;margin:0 auto;padding:16px}
nav.crumbs{font-size:13px;color:var(--muted)} nav.crumbs a{color:var(--muted)}
h1{font-size:30px;line-height:1.22;margin:10px 0 8px}
h2{font-size:22px;margin:36px 0 10px;padding-top:8px;border-top:1px solid var(--line)}
h3{font-size:18px;margin:20px 0 6px}
a{color:var(--brand)} p{margin:8px 0}
a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible,select:focus-visible{outline:3px solid var(--brand);outline-offset:2px}
.meta{font-size:13px;color:var(--muted);margin:4px 0 12px}
.meta b{color:var(--text)}
.answer{background:var(--card);border-left:4px solid var(--brand);border-radius:0 10px 10px 0;padding:14px 16px;margin:12px 0;font-size:18px;line-height:1.5}
.applies{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:6px 16px 10px;margin:16px 0}
.applies h2{border:0;margin:10px 0 4px;padding:0;font-size:19px}
.applies ul{margin:6px 0;padding-left:22px} .applies li{margin:4px 0}
.box{border-radius:10px;padding:12px 14px;margin:14px 0;font-size:15px}
.warn{background:var(--warn-bg);color:var(--warn)}
.tblwrap{overflow-x:auto;margin:10px 0;-webkit-overflow-scrolling:touch}
.tbl{width:100%;border-collapse:collapse;font-size:15px}
.tbl th,.tbl td{border-bottom:1px solid var(--line);padding:9px 8px;text-align:left;vertical-align:top}
.tbl th{font-size:13px;color:var(--muted);font-weight:600;background:var(--card)}
.tbl td:first-child{font-weight:600}
.tbl.ba td:nth-child(3){background:#f1f7ff}
tr.next td{background:#fff6e5!important;font-weight:600}
ol.steps{padding-left:22px} ol.steps li{margin:8px 0}
details{border-bottom:1px solid var(--line);padding:2px 0} summary{font-weight:600;cursor:pointer;padding:12px 0;min-height:44px}
details p{margin:0 0 12px}
.related a{display:block;padding:12px 0;min-height:44px;border-bottom:1px solid var(--line);text-decoration:none;font-weight:600}
.sources li{margin:6px 0;font-size:15px}
.tool{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:12px 0}
.privacy{font-size:13px;color:var(--ok);background:var(--ok-bg);border-radius:8px;padding:7px 10px;margin:0 0 12px}
label.f{display:block;font-weight:600;font-size:14px;margin:10px 0 4px}
.tool input[type=number],.tool input[type=date]{width:100%;min-height:44px;padding:10px;border:1px solid #8a94a3;border-radius:9px;font-size:16px;background:#fff;color:var(--text)}
fieldset{border:0;padding:0;margin:0 0 14px} legend{font-weight:700;margin-bottom:6px;padding:0}
.opt{display:flex;gap:10px;align-items:flex-start;min-height:44px;padding:9px 10px;margin:6px 0;border:1px solid var(--line);border-radius:9px;background:#fff;cursor:pointer;font-size:15px}
.opt input{margin-top:4px;width:18px;height:18px;flex:0 0 auto}
.cb{display:flex;gap:10px;align-items:center;min-height:44px;margin-top:10px;font-size:15px} .cb input{width:20px;height:20px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;border:0;border-radius:10px;padding:10px 16px;font-weight:700;font-size:16px;cursor:pointer;background:var(--brand);color:#fff;text-decoration:none;margin:6px 6px 0 0}
.btn.sec{background:#fff;color:var(--brand);border:1px solid var(--brand)}
.btn.sm{font-size:14px;padding:8px 12px}
.quick{margin:4px 0 12px}
.verdict{border-radius:10px;padding:14px;margin:12px 0;background:#fff;border:1px solid var(--line);font-size:16px}
.verdict.yes{background:var(--ok-bg);color:#075c2d;border-color:#9bd3b3}
.verdict.no{background:var(--danger-bg);color:var(--danger);border-color:#e9a8a8}
.verdict.mid{background:var(--warn-bg);color:var(--warn);border-color:#e6c27a}
.verdict .actions{margin-top:8px}
.count{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;text-align:center;margin:8px 0}
.count div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 4px}
.count b{display:block;font-size:28px;line-height:1.1;font-variant-numeric:tabular-nums} .count span{font-size:12px;color:var(--muted)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px} .row2{display:grid;grid-template-columns:1fr 1fr;gap:10px;align-items:end}
.hint{font-size:13px;color:var(--muted);margin:6px 0 0}
.sticky{position:fixed;left:0;right:0;bottom:0;background:var(--bg);border-top:1px solid var(--line);padding:10px 16px;z-index:10}
.sticky a{display:block;max-width:760px;margin:0 auto;text-align:center;background:var(--red);color:#fff;text-decoration:none;font-weight:700;padding:13px;border-radius:10px;min-height:44px}
.sticky a:hover{background:var(--red-dark)}
footer{font-size:13px;color:var(--muted);margin-top:40px;border-top:1px solid var(--line);padding-top:14px}
footer a{display:inline-block;padding:10px 4px}
@media (max-width:560px){h1{font-size:25px}.two,.row2{grid-template-columns:1fr}.count b{font-size:22px}}
@media print{.sticky,.tool,nav,footer{display:none!important}}
"""


def esc(s):
    return H.escape(s, quote=True)


def plain(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def label(slug):
    return dict(D.PAGES_ORDER)[slug]


def url(slug):
    return f"{SITE}/{slug}"


def breadcrumb(slug, title):
    items = [("Home", "/")]
    if slug in D.CLUSTER_A and slug != D.HUB:
        items.append((D.HUB_LABEL, f"/{D.HUB}"))
    items.append((title, f"/{slug}"))
    return items


def jsonld(slug, p):
    crumbs = breadcrumb(slug, p["h1"])
    graph = [
        {
            "@type": "Article", "headline": p["h1"], "description": p["desc"],
            "datePublished": D.LAST_VERIFIED_ISO, "dateModified": D.LAST_VERIFIED_ISO,
            "inLanguage": "en-US", "mainEntityOfPage": url(slug),
            "author": {"@type": "Organization", "name": "SignRight", "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": "SignRight", "url": SITE + "/"},
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": (SITE + h) if h != "/" else SITE + "/"}
                for i, (n, h) in enumerate(crumbs)
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                for q, a in p["faq"]
            ],
        },
    ]
    if p.get("tool"):
        t = TOOLS[p["tool"]]
        graph.append({
            "@type": "WebApplication", "name": t["name"], "url": url(slug),
            "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
            "browserRequirements": "Requires JavaScript",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            "description": t["desc"], "inLanguage": "en-US", "dateModified": D.LAST_VERIFIED_ISO,
            "publisher": {"@type": "Organization", "name": "SignRight", "url": SITE + "/"},
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


def render(slug):
    p = D.PAGES[slug]
    u = url(slug)
    crumbs = breadcrumb(slug, p["h1"])
    crumb_html = " › ".join(
        f'<a href="{h}">{esc(n)}</a>' if i < len(crumbs) - 1 else esc(plain(n)) for i, (n, h) in enumerate(crumbs)
    )
    out = []
    a = out.append
    a('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">')
    a(f"<title>{esc(p['title'])}</title>")
    a(f'<meta name="description" content="{esc(p["desc"])}">')
    a(f'<link rel="canonical" href="{u}">')
    a('<meta name="robots" content="index, follow, max-image-preview:large">')
    a(f'<link rel="icon" type="image/svg+xml" href="{FAVICON}">')
    a(f'<meta property="og:type" content="article">\n<meta property="og:title" content="{esc(p["og_title"])}">\n'
      f'<meta property="og:description" content="{esc(p["desc"])}">\n<meta property="og:url" content="{u}">\n'
      '<meta property="og:site_name" content="SignRight">\n<meta property="og:locale" content="en_US">\n'
      f'<meta property="article:modified_time" content="{D.LAST_VERIFIED_ISO}">\n'
      f'<meta name="twitter:card" content="summary">\n<meta name="twitter:title" content="{esc(p["og_title"])}">\n'
      f'<meta name="twitter:description" content="{esc(p["desc"])}">')
    a('<script type="application/ld+json">\n' + jsonld(slug, p) + "\n</script>")
    a(GTM_HEAD)
    a("<style>" + CSS + "</style>")
    a(CLARITY)
    a(ADSENSE)
    a("</head>\n<body>")
    a(GTM_BODY)
    a('<main class="wrap">')
    a(f'<nav class="crumbs" aria-label="Breadcrumb">{crumb_html}</nav>')
    a(f"<h1>{esc(p['h1'])}</h1>")
    a(f'<p class="meta"><b>Last verified:</b> {D.LAST_VERIFIED} against IRS.gov sources listed below · {D.DISCLAIMER}</p>')
    a(f'<p class="answer">{p["answer"]}</p>')
    if p.get("notice"):
        a(f'<div class="box warn">{p["notice"]}</div>')
    a('<section class="applies" aria-labelledby="applies-h"><h2 id="applies-h">Does this apply to me?</h2><ul>'
      + "".join(f"<li>{x}</li>" for x in p["applies"]) + "</ul></section>")
    if p.get("tool"):
        t = TOOLS[p["tool"]]
        a(f'<section aria-labelledby="tool-h"><h2 id="tool-h">{t["title"]}</h2><p>{t["intro"]}</p>'
          f'<div class="tool sr-tool" data-ad-exclude="true">{t["html"]}</div></section>')
    for sid, h2, body in p["sections"]:
        a(f'<section id="{sid}"><h2>{h2}</h2>{body}</section>')
    a('<section id="next"><h2>What to do next</h2><ol class="steps">' + "".join(f"<li>{x}</li>" for x in p["next"]) + "</ol></section>")
    a('<section id="faq"><h2>Frequently asked questions</h2>'
      + "".join(f"<details><summary>{q}</summary><p>{ans}</p></details>" for q, ans in p["faq"]) + "</section>")
    a('<section id="sources"><h2>Official sources</h2><ul class="sources">'
      + "".join(f'<li><a href="{D.SRC[k][1]}" target="_blank" rel="noopener">{esc(D.SRC[k][0])}</a></li>' for k in p["sources"]) + "</ul></section>")
    rel = [f'<a href="/{s}">{esc(l)} →</a>' for s, l in D.PAGES_ORDER if s != slug]
    rel += [f'<a href="{h}">{esc(l)}</a>' for h, l in D.EXISTING_RELATED]
    a('<section id="related"><h2>Related guides</h2><div class="related">' + "".join(rel) + "</div></section>")
    a(f'<footer>\n<p><strong>Last verified:</strong> {D.LAST_VERIFIED}.</p>\n'
      "<p>SignRight is an independent guide, not affiliated with the IRS. This is general information, not tax or legal advice. "
      "Confirm with the IRS or a qualified tax professional. Rules and draft forms can change.</p>\n"
      '<p><a href="/">Home</a> · <a href="/about">About</a> · <a href="/contact">Contact</a> · <a href="/privacy">Privacy</a> · <a href="/terms">Terms</a></p>\n</footer>')
    a("</main>")
    label_, link = p["cta"]
    a(f'<div class="sticky no-print"><a href="{link}" target="_blank" rel="noopener">{esc(label_)} →</a></div>')
    a("</body>\n</html>\n")
    return "\n".join(out)


# ------------------------------------------------------------------ validation
def validate(pages):
    errs = []
    titles, descs = set(), set()
    known = {s for s in D.PAGES} | {f[:-5] for f in os.listdir(ROOT) if f.endswith(".html")} | {""}
    for slug, html in pages.items():
        p = D.PAGES[slug]
        if len(html.encode()) > MAX_BYTES:
            errs.append(f"{slug}: {len(html.encode())} bytes > 100KB")
        if len(p["desc"]) > 160:
            errs.append(f"{slug}: description {len(p['desc'])} chars")
        if p["title"] in titles or p["desc"] in descs:
            errs.append(f"{slug}: duplicate title/description")
        titles.add(p["title"]); descs.add(p["desc"])
        if html.count("adsbygoogle.js?client=ca-pub-8173139997421073") != 1:
            errs.append(f"{slug}: AdSense count != 1")
        for needle in ("GTM-KGBKN6DP", 'rel="canonical"', 'property="og:title"', 'name="twitter:card"', '"FAQPage"', '"Article"', '"BreadcrumbList"'):
            if needle not in html:
                errs.append(f"{slug}: missing {needle}")
        if bool(p.get("tool")) != ('"WebApplication"' in html):
            errs.append(f"{slug}: WebApplication mismatch")
        if html.count("GTM-KGBKN6DP") != 2 or "<noscript><iframe" not in html:
            errs.append(f"{slug}: GTM must appear once in <head> script and once in <body> noscript")
        for m in re.finditer(r'href="(/[^"#?]*)"', html):
            path = m.group(1).strip("/")
            if path not in known:
                errs.append(f"{slug}: broken internal link {m.group(1)}")
        if len(re.findall(r'href="/(?:' + "|".join(re.escape(s) for s in D.PAGES if s != slug) + r')"', html)) < 3:
            errs.append(f"{slug}: fewer than 3 internal links to the set")
        # ld+json must parse
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            json.loads(blob)
    return errs


# ------------------------------------------------------------------ patchers (additive, idempotent)
def patch_vercel():
    path = os.path.join(ROOT, "vercel.json")
    raw = open(path).read()
    before = json.loads(raw)
    slugs = [s for s, _ in D.PAGES_ORDER]
    red_new = [s for s in slugs if f'"/{s}.html"' not in raw]
    rew_new = [s for s in slugs if not re.search(r'"source":\s*"/' + re.escape(s) + r'"', raw)]
    if not red_new and not rew_new:
        return "vercel.json: already patched"
    red = "".join(f'    {{\n      "source": "/{s}.html",\n      "destination": "/{s}",\n      "permanent": true\n    }},\n' for s in red_new)
    rew = "".join(f'    {{\n      "source": "/{s}",\n      "destination": "/{s}.html"\n    }},\n' for s in rew_new)
    i_rew_key = raw.index('"rewrites": [')
    # redirects array closes just before the rewrites key
    i_red_close = raw.rindex("]", 0, i_rew_key)
    last_red_obj_end = raw.rindex("}", 0, i_red_close)
    new = raw[: last_red_obj_end + 1] + ",\n" + red.rstrip(",\n") + "\n  " + raw[i_red_close:]
    i_rew_key = new.index('"rewrites": [')
    i_hdr_key = new.index('"headers": [')
    i_rew_close = new.rindex("]", 0, i_hdr_key)
    last_rew_obj_end = new.rindex("}", 0, i_rew_close)
    new = new[: last_rew_obj_end + 1] + ",\n" + rew.rstrip(",\n") + "\n  " + new[i_rew_close:]
    after = json.loads(new)
    assert after["redirects"][: len(before["redirects"])] == before["redirects"], "existing redirects changed"
    assert after["rewrites"][: len(before["rewrites"])] == before["rewrites"], "existing rewrites changed"
    assert after["headers"] == before["headers"] and after.get("trailingSlash") == before.get("trailingSlash")
    open(path, "w").write(new)
    return f"vercel.json: +{len(red_new)} redirects, +{len(rew_new)} rewrites"


def patch_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    raw = open(path).read()
    new_lines = []
    for s, _ in D.PAGES_ORDER:
        if f"<loc>{SITE}/{s}</loc>" in raw:
            continue
        pr = "0.9" if s == D.HUB else "0.8"
        new_lines.append(f"  <url><loc>{SITE}/{s}</loc><lastmod>{D.LAST_VERIFIED_ISO}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    if not new_lines:
        return "sitemap.xml: already patched"
    block = "\n  <!-- IRS FIRE to IRIS and tax year 2026 information return guides -->\n" + "\n".join(new_lines) + "\n"
    i = raw.rindex("</urlset>")
    open(path, "w").write(raw[:i].rstrip("\n") + "\n" + block + "\n" + raw[i:])
    return f"sitemap.xml: +{len(new_lines)} urls"


def patch_index():
    path = os.path.join(ROOT, "index.html")
    raw = open(path).read()
    if f'href="/{D.HUB}"' in raw:
        return "index.html: already linked"
    card = (f'      <a class="tool-card" href="/{D.HUB}">\n'
            '        <div class="tool-card-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>\n'
            '        <span class="tool-card-name">IRS FIRE shutdown: 19 November 2026</span>\n'
            '        <span class="tool-card-desc">Countdown, IRIS TCC guide and 1099 changes for 2026</span>\n'
            '      </a>\n')
    anchor = '      <a class="tool-card" href="/travel">'
    assert raw.count(anchor) == 1
    open(path, "w").write(raw.replace(anchor, card + anchor))
    return "index.html: hub card added"


def main():
    check = "--check" in sys.argv
    pages = {s: render(s) for s, _ in D.PAGES_ORDER}
    errs = validate(pages)
    for s, h in pages.items():
        print(f"{len(h.encode())/1024:6.1f} KB  {s}")
    if errs:
        print("\nVALIDATION ERRORS:\n  " + "\n  ".join(errs))
        sys.exit(1)
    print("\nvalidation: OK")
    if check:
        return
    for s, h in pages.items():
        with open(os.path.join(ROOT, f"{s}.html"), "w") as f:
            f.write(h)
    print(patch_vercel()); print(patch_sitemap()); print(patch_index())


if __name__ == "__main__":
    main()
