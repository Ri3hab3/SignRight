import glob

MEGA_MENU_FIX = """
/* ---- mobile nav fix: mega-menu ---- */
@media(max-width:900px){
  .nav-links,.nav-cta{display:none}
  .nav-mobile-btn{display:block}
  .nav-drawer{display:block;position:fixed;inset:0;background:rgba(20,22,43,.5);z-index:200;
              opacity:0;pointer-events:none;transition:opacity .2s}
  .nav-drawer.open{opacity:1;pointer-events:all}
  .nav-drawer-panel{position:absolute;top:0;right:0;width:min(320px,86vw);height:100%;
                    background:#fff;padding:1.2rem;overflow-y:auto}
  .nav-drawer-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:1.2rem}
  .drawer-close{background:none;border:none;padding:.3rem}
  .drawer-section{margin-bottom:1.2rem;display:flex;flex-direction:column;gap:.3rem}
  .drawer-section-label{font-size:.7rem;font-weight:700;text-transform:uppercase;
                        letter-spacing:.06em;color:#5C5F75;margin-bottom:.25rem}
  .drawer-section a{font-size:.9rem;padding:.32rem 0}
}
"""

SIMPLE_NAV_FIX = """
/* ---- mobile nav fix: simple forms nav ---- */
@media(max-width:640px){
  .nav-inner{padding:0 1rem}
  .nav-links{gap:.9rem}
  .nav-links a{font-size:.8rem}
  .btn-ghost,.btn-dark{padding:.45rem .7rem;font-size:.82rem}
}
@media(max-width:420px){
  .nav-links a:nth-child(1),.nav-links a:nth-child(2){display:none}
}
"""

patched, skipped, errors = [], [], []

for fname in sorted(glob.glob("*.html")):
    with open(fname, encoding="utf-8") as f:
        html = f.read()
    has_drawer = "nav-drawer" in html
    has_simple = 'href="/#services"' in html
    if has_drawer and "mobile nav fix: mega-menu" not in html:
        block, label = MEGA_MENU_FIX, "mega-menu"
    elif has_simple and "mobile nav fix: simple forms" not in html:
        block, label = SIMPLE_NAV_FIX, "simple forms nav"
    else:
        skipped.append(f"{fname} (no matching nav pattern, or already patched)")
        continue
    idx = html.find("</style>")
    if idx != -1:
        html = html[:idx] + block + html[idx:]
    elif "</head>" in html:
        html = html.replace("</head>", "<style>" + block + "</style>\n</head>", 1)
    else:
        errors.append(f"{fname} (no </style> or </head> — patch manually)"); continue
    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    patched.append(f"{fname} [{label}]")

try:
    with open("styles.css", encoding="utf-8") as f:
        shared = f.read()
    if "mobile nav fix: mega-menu" not in shared:
        with open("styles.css", "a", encoding="utf-8") as f:
            f.write("\n" + MEGA_MENU_FIX)
        patched.append("styles.css [mega-menu, shared]")
    else:
        skipped.append("styles.css (already patched)")
except FileNotFoundError:
    errors.append("styles.css not found in this directory")

print("PATCHED:")
for p in patched: print(" ", p)
print("\nSKIPPED:")
for s in skipped: print(" ", s)
if errors:
    print("\nNEEDS MANUAL LOOK:")
    for e in errors: print(" ", e)
