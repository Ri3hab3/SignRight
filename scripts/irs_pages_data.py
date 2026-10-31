"""Content + facts for the IRS FIRE->IRIS and TY2026 information-return pages.

Facts live here, markup lives in generate_irs_pages.py. To update a fact, edit this
file and re-run `python3 scripts/generate_irs_pages.py`.

Every factual claim is traceable to an IRS document listed in SRC. Where a claim
could not be verified it is deliberately NOT written (see the build report).
"""

LAST_VERIFIED = "31 October 2026"
LAST_VERIFIED_ISO = "2026-10-31"

# ---------------------------------------------------------------- sources
SRC = {
    "ir99": ("IRS news release IR-2026-99: information return e-file system transitioning to a new platform",
             "https://www.irs.gov/newsroom/irs-reminder-information-return-e-file-system-transitioning-to-a-new-platform"),
    "iris": ("IRS: E-file information returns with IRIS", "https://www.irs.gov/filing/e-file-information-returns-with-iris"),
    "efile": ("IRS: E-file information returns", "https://www.irs.gov/filing/e-file-information-returns"),
    "tcc": ("IRS: IRIS Application for TCC", "https://www.irs.gov/tax-professionals/iris-application-for-tcc"),
    "p5903": ("IRS Publication 5903: IRIS App for TCC tutorial (PDF)", "https://www.irs.gov/pub/irs-pdf/p5903.pdf"),
    "faq": ("IRS: Information Returns Intake System (IRIS) FAQs (PDF)", "https://www.irs.gov/pub/irs-efile/info-returns-intake-system-faqs.pdf"),
    "p1220": ("IRS Publication 1220 (Rev. 5-2026): e-filing specifications (PDF)", "https://www.irs.gov/pub/irs-pdf/p1220.pdf"),
    "p5717": ("IRS Publication 5717: IRIS Taxpayer Portal user guide (PDF)", "https://www.irs.gov/pub/irs-pdf/p5717.pdf"),
    "p1099": ("IRS: Publication 1099, General Instructions for Certain Information Returns (2026)", "https://www.irs.gov/publications/p1099"),
    "p1099pdf": ("IRS Publication 1099 (2026), Guide to Information Returns (PDF)", "https://www.irs.gov/pub/irs-pdf/p1099.pdf"),
    "iw2w3": ("IRS: 2026 General Instructions for Forms W-2 and W-3 (PDF)", "https://www.irs.gov/pub/irs-pdf/iw2w3.pdf"),
    "i1099mec": ("IRS: Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026) (PDF)", "https://www.irs.gov/pub/irs-pdf/i1099mec.pdf"),
    "i1099k": ("IRS: Instructions for Form 1099-K (Rev. December 2026)", "https://www.irs.gov/instructions/i1099k"),
    "i1099r": ("IRS: 2026 Instructions for Forms 1099-R and 5498 (PDF)", "https://www.irs.gov/pub/irs-pdf/i1099r.pdf"),
    "f1099r": ("IRS: Form 1099-R (2026) (PDF)", "https://www.irs.gov/pub/irs-pdf/f1099r.pdf"),
    "i1098vli": ("IRS: Instructions for Form 1098-VLI (December 2026) (PDF)", "https://www.irs.gov/pub/irs-pdf/i1098vli.pdf"),
    "f1098vli": ("IRS: Form 1098-VLI (December 2026) early-release draft (PDF)", "https://www.irs.gov/pub/irs-dft/f1098vli--dft.pdf"),
    "s1a": ("IRS: 2026 Schedule 1-A (Form 1040), draft (PDF)", "https://www.irs.gov/pub/irs-dft/f1040s1a--dft.pdf"),
    "f1099nec_dft": ("IRS: Form 1099-NEC (Rev. December 2026) early-release draft (PDF)", "https://www.irs.gov/pub/irs-dft/f1099nec--dft.pdf"),
    "f1099k_dft": ("IRS: Form 1099-K (Rev. December 2026) early-release draft (PDF)", "https://www.irs.gov/pub/irs-dft/f1099k--dft.pdf"),
    "about_nec": ("IRS: About Form 1099-NEC", "https://www.irs.gov/forms-pubs/about-form-1099-nec"),
    "about_k": ("IRS: About Form 1099-K", "https://www.irs.gov/forms-pubs/about-form-1099-k"),
    "about_w2": ("IRS: About Form W-2", "https://www.irs.gov/forms-pubs/about-form-w-2"),
    "kfaq": ("IRS: FAQs on the Form 1099-K threshold under the One, Big, Beautiful Bill",
             "https://www.irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000"),
    "kfaq_general": ("IRS: Form 1099-K FAQs, general information", "https://www.irs.gov/newsroom/form-1099-k-faqs-general-information"),
    "ir03": ("IRS news release IR-2026-03: proposed backup withholding regulations for third-party payments",
             "https://www.irs.gov/newsroom/treasury-irs-issue-proposed-regulations-reflecting-changes-from-the-one-big-beautiful-bill-to-the-threshold-for-backup-withholding-on-certain-payments-made-through-third-parties"),
    "fs2026_13": ("IRS Fact Sheet FS-2026-13: qualified overtime compensation FAQs (PDF)", "https://www.irs.gov/pub/taxpros/fs-2026-13.pdf"),
    "ir49": ("IRS news release IR-2026-49: final regulations listing tipped occupations",
             "https://www.irs.gov/newsroom/treasury-irs-issue-final-regulations-listing-occupations-where-workers-customarily-and-regularly-receive-tips-under-the-one-big-beautiful-bill"),
    "p1179": ("IRS Publication 1179 (Rev. 7-2026): substitute forms rules (PDF)", "https://www.irs.gov/pub/irs-pdf/p1179.pdf"),
    "drafts": ("IRS: Draft tax forms", "https://www.irs.gov/draft-tax-forms"),
}

# ---------------------------------------------------------------- page order / labels
# (slug, short link label)
PAGES_ORDER = [
    ("irs-fire-system-shutdown-2026", "When does the IRS FIRE system shut down?"),
    ("iris-tcc-application-guide", "How to apply for an IRIS TCC"),
    ("fire-vs-iris-differences", "FIRE vs IRIS: what changes"),
    ("does-my-fire-tcc-work-with-iris", "Does my FIRE TCC work with IRIS?"),
    ("how-to-file-1099-through-iris", "How to file 1099s through IRIS"),
    ("1099-deadlines-2027-filing-season", "1099 deadlines for the 2027 filing season"),
    ("1099-threshold-600-to-2000", "1099 threshold: $600 to $2,000"),
    ("1099-nec-2026-changes", "Form 1099-NEC changes for 2026"),
    ("reporting-cash-tips-1099-w2-2026", "Reporting cash tips on W-2 and 1099 (2026)"),
    ("reporting-overtime-1099-2026", "Reporting qualified overtime (2026)"),
    ("treasury-tipped-occupation-code", "Treasury Tipped Occupation Code (TTOC)"),
    ("form-1098-vli-vehicle-loan-interest", "Form 1098-VLI: vehicle loan interest"),
    ("1099-r-box-7-changes-2026", "Form 1099-R box 7a-7d changes (2026)"),
    ("1099-k-2026-changes", "Form 1099-K changes for 2026"),
]
HUB = "irs-fire-system-shutdown-2026"
HUB_LABEL = "IRS FIRE to IRIS"
CLUSTER_A = [p[0] for p in PAGES_ORDER[:6]]

EXISTING_RELATED = [
    ("/w-8ben-form", "Form W-8BEN line by line (foreign payees) →"),
    ("/fill-w-8ben-online", "Fill W-8BEN online (free tool) →"),
]

DISCLAIMER = ("General information, not tax advice. Confirm with the IRS or a qualified tax professional "
              "before you act.")

STATUS_NEC = ("<b>Draft status:</b> the IRS has posted the December 2026 revision of Form 1099-NEC and its "
              "instructions, but its own notice says it is still &ldquo;developing&rdquo; that revision, and early-release "
              "copies are marked &ldquo;DRAFT &mdash; NOT FOR FILING&rdquo;. We could not confirm a final release, so box "
              "numbers, wording or e-file specifications could still change.")
STATUS_K = ("<b>Draft status:</b> the IRS has posted the December 2026 revision of Form 1099-K and its instructions, but "
            "says it is still &ldquo;developing&rdquo; that revision, and the early-release copy is marked "
            "&ldquo;DRAFT &mdash; NOT FOR FILING&rdquo;. We could not confirm a final release, so box wording or layout "
            "could still change.")
STATUS_W2 = ("<b>Status:</b> the IRS has posted the 2026 Form W-2 and the 2026 General Instructions for Forms W-2 and W-3 "
             "(issued 29 January 2026). The IRS listed further changes to the 2026 W-2 forms on 19 August 2026, so check "
             "the form you actually use.")

# ---------------------------------------------------------------- helpers
def table(headers, rows, cls="tbl ba"):
    h = "".join(f"<th scope=\"col\">{c}</th>" for c in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tblwrap"><table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'

def steps(items):
    return "<ol class=\"steps\">" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def box(kind, html):
    return f'<div class="box {kind}">{html}</div>'


# ---------------------------------------------------------------- pages
PAGES = {}

PAGES["irs-fire-system-shutdown-2026"] = dict(
    title="IRS FIRE System Shutdown 2026: Last Day Is 19 November",
    h1="When Does the IRS FIRE System Shut Down?",
    desc="The IRS FIRE system closes at 3 p.m. ET on 19 Nov 2026. See the key dates, who is affected, a live countdown and what to do before filing through IRIS.",
    og_title="IRS FIRE Shutdown: Last Day Is 19 November 2026",
    answer=("<b>The IRS FIRE system stops accepting information returns at 3 p.m. Eastern on 19 November 2026.</b> "
            "For tax year 2026 returns filed in 2027, you must use the IRS Information Returns Intake System (IRIS) instead."),
    applies=[
        "You e-file Forms 1099, 1098, 5498, W-2G or 1042-S by uploading files to FIRE (or through software that does).",
        "You hold a FIRE Transmitter Control Code (TCC) &mdash; FIRE TCCs start with a number.",
        "You file 10 or more information returns in total, so e-filing is required.",
        "You are a small business that has never e-filed 1099s and wants the free IRIS portal instead of paper.",
    ],
    tool="fire_countdown",
    sections=[
        ("dates", "Key FIRE dates", (
            "<p>These are the dates in IRS news release IR-2026-99 (24 August 2026). Today&rsquo;s status is calculated in your browser.</p>"
            + table(["Date", "What happens", "Status today"], [
                ["1 Nov 2026", "Last day to file test returns through the FIRE Trading Partner Test System", '<span data-status="2026-11-01T23:59:00-05:00">&hellip;</span>'],
                ["9 Nov 2026", "Last day to make changes to Information Returns (IR) Applications for TCC", '<span data-status="2026-11-09T23:59:00-05:00">&hellip;</span>'],
                ["19 Nov 2026, 3 p.m. ET", "Last day to file information returns through FIRE", '<span data-status="2026-11-19T15:00:00-05:00">&hellip;</span>'],
            ]))),
        ("change", "What changed, before and after", (
            table(["", "Before", "Now"], [
                ["Where you e-file", "FIRE, or IRIS (available for tax year 2022 and later)", "IRIS only, for tax year 2026 returns filed in the 2027 filing season"],
                ["New FIRE TCC applications", "Accepted", "Not accepted from 21 July 2026 (IRS Pub. 1220, Rev. 5-2026)"],
                ["Changes to existing FIRE applications", "Allowed", "Last day 9 Nov 2026 per IR-2026-99; Pub. 1220 says updates continue through December 2026, then read-only"],
                ["Last day to file through FIRE", "&mdash;", "19 Nov 2026, 3 p.m. ET"],
            ])
            + box("warn", "<b>Sources differ slightly.</b> Publication 1220 (Rev. 5-2026) says IRIS is the only e-file system, including corrections, after 1 January 2027. The later IRS release IR-2026-99 sets 19 November 2026 as the last day to submit through FIRE. Plan around the earlier date."))),
        ("tax-year", "Does this affect tax year 2025 returns?", (
            "<p>Publication 1220 (Rev. 5-2026) says IRIS will be the only information returns e-file system, &ldquo;including current year, prior year, or corrections&rdquo;, after 1 January 2027. "
            "If you still have tax year 2025 returns or corrections to send through FIRE, do it before the 19 November cutoff. We could not find an IRS statement on how corrections to returns originally filed in FIRE will be handled after it closes, so check IRS.gov/IRIS.</p>")),
    ],
    next=[
        'Decide this week: will you file in the free IRIS Taxpayer Portal, through software, or through a service provider?',
        'If you file yourself, complete the <a href="https://www.irs.gov/tax-professionals/iris-application-for-tcc" target="_blank" rel="noopener">IRIS Application for TCC</a>. <a href="/iris-tcc-application-guide">See the timing calculator</a>.',
        'Finish any tax year 2025 FIRE filings and corrections before 3 p.m. ET on 19 November 2026.',
        'Subscribe to IRIS QuickAlerts, which the IRS recommends for system changes and maintenance notices.',
    ],
    faq=[
        ("Is the FIRE shutdown date confirmed?", "Yes. IRS news release IR-2026-99 (24 August 2026) lists 19 November 2026, 3 p.m. ET as the last day to file information returns through FIRE. Older IRS documents point to the end of December 2026, so always use the earlier date."),
        ("What happens if I miss the 19 November cutoff?", "FIRE will no longer accept your submissions after that time. You would file the return through IRIS instead. The IRS release states filers will no longer be able to submit through FIRE after the November maintenance window."),
        ("Do I need to do anything if my accountant files my 1099s?", "Probably not directly, but ask them whether they have moved to IRIS. The IRS release says IRIS has an Application to Application channel for filers using third-party or self-developed software."),
        ("Is IRIS free?", "The IRIS Taxpayer Portal is free and lets you e-file up to 100 returns at a time by manual entry or CSV upload, according to the IRS. Third-party software is a separate product from the free Portal."),
        ("Which forms were filed through FIRE?", "The IRS e-file page lists Forms 1097, 1098, 1099, 3921, 3922, 5498, 8027, 8596, 8955-SSA, 1042-S and W-2G as FIRE-eligible. It also says IRIS will accept Forms 8027 and 8955-SSA beginning with filing year 2027."),
    ],
    sources=["ir99", "p1220", "efile", "iris", "tcc"],
    cta=("Open the official IRIS page on IRS.gov", "https://www.irs.gov/filing/e-file-information-returns-with-iris"),
)

PAGES["iris-tcc-application-guide"] = dict(
    title="How to Apply for an IRIS TCC (Transmitter Control Code)",
    h1="How to Apply for an IRIS TCC (Transmitter Control Code)",
    desc="Apply for an IRIS TCC online. What you need, how long the IRS says it takes (up to 45 days) and a calculator for the last safe date to apply.",
    og_title="How to Apply for an IRIS TCC: Steps and Timing",
    answer=("<b>Apply online through the IRS IRIS Application for TCC.</b> The IRS says processing is usually quick but can take up to 45 days "
            "(Publication 5903 says the typical application is processed within 45 business days), so apply as early as you can."),
    applies=[
        "You want to e-file 1099-series forms yourself in the IRIS Taxpayer Portal or through your own software.",
        "You only have a FIRE TCC (numeric). IRIS needs its own TCC, which starts with the letter D.",
        "You are a business, transmitter or software developer. Foreign filers who cannot get a TCC in IRIS use a separate Foreign Filer TCC Registration.",
        "You do <b>not</b> need your own TCC if a payroll provider or tax preparer submits your returns for you.",
    ],
    tool="tcc_calc",
    sections=[
        ("change", "FIRE TCC vs IRIS TCC", (
            table(["", "FIRE TCC", "IRIS TCC"], [
                ["Application", "Information Returns (IR) Application for TCC", "IRIS Application for TCC"],
                ["Looks like", "Starts with a number", "Starts with &ldquo;D&rdquo;; five digits"],
                ["Works for", "FIRE", "IRIS only"],
                ["New applications", "Closed from 21 July 2026", "Open"],
            ])
            + "<p>Source: IRS &ldquo;E-file information returns&rdquo; and &ldquo;E-file information returns with IRIS&rdquo; pages, and Publication 1220 (Rev. 5-2026).</p>")),
        ("need", "What to have ready", (
            ul([
                "Your organization&rsquo;s EIN, legal name, business type, addresses and phone numbers.",
                "Responsible Officials (RO): at least two. Sole proprietors, S-corporations and single-member LLCs need at least one RO and one contact.",
                "Contacts the IRS can reach about the application (at least two, or one for the single-owner structures above).",
                "For every authorized user: SSN or ITIN, date of birth, citizenship status and contact details.",
                "The forms you will file and the transmission method: Portal (web) or A2A (software).",
                "Your role: Issuer (only your own returns), Transmitter (returns for others) or Software Developer. You cannot choose both Issuer and Transmitter.",
            ]) + "<p>Source: IRS Publication 5903 (Rev. 12-2024).</p>")),
        ("process", "How the process works", (
            steps([
                "Every RO and AD signs in with an IRS online account. They create one if they don&rsquo;t have it.",
                "Fill in every page of the IRIS Application for TCC.",
                "Every RO signs the Application Submission page with a 5-digit PIN. Status then shows &ldquo;Submitted Pending Review&rdquo;.",
                "The IRS runs checks and assigns TCCs. When status is &ldquo;Completed&rdquo;, the TCC appears on the Application Summary page. You can use the TCC before the acceptance letter arrives by post.",
            ]))),
        ("timing", "How long does it take?", (
            "<p>The IRS gives three figures, so here they are side by side:</p>"
            + table(["IRS source", "What it says"], [
                ["IRIS FAQs", "Usually completed within 24 hours, but could take up to 45 days"],
                ["Publication 5903", "The typical application is processed within 45 business days"],
                ["Publication 1220", "Allow 45 business days; submit by 1 November of the year before the filing deadline (that guidance is written for FIRE applications)"],
            ])
            + "<p>The calculator above uses 45 business days by default because it is the most cautious reading. We count weekdays and skip US federal holidays; the IRS does not define &ldquo;business days&rdquo; on these pages.</p>")),
    ],
    next=[
        'Check you need a TCC: if a provider submits for you, ask them first.',
        'Gather the items above, and make sure each Responsible Official can sign in to their IRS online account.',
        'Start the <a href="https://www.irs.gov/tax-professionals/iris-application-for-tcc" target="_blank" rel="noopener">IRIS Application for TCC</a> and follow the <a href="https://www.irs.gov/pub/irs-pdf/p5903.pdf" target="_blank" rel="noopener">Publication 5903 tutorial</a>.',
        'Use the calculator above to check your target filing date against the 45-day window.',
    ],
    faq=[
        ("How long does it take to get an IRIS TCC?", "The IRS IRIS FAQs say the process is usually completed within 24 hours but could take up to 45 days. Publication 5903 says the typical application is processed within 45 business days. Plan for the longer figure."),
        ("What does an IRIS TCC look like?", "It is a five-digit code that starts with the letter D and works only with IRIS, per the IRS e-file pages."),
        ("Do I need an IRIS TCC to use the free Taxpayer Portal?", "Yes. The IRS says you need an IRIS TCC to use the IRIS Taxpayer Portal."),
        ("What is the difference between Issuer and Transmitter?", "An Issuer only transmits returns for the company on the application. A Transmitter is a third party that transmits for its own company and other businesses. Software Developers build software that sends returns by A2A."),
        ("Can a government agency apply?", "Yes. The IRS says agencies sharing one EIN can have only one IRIS Application for TCC, so coordinate inside the agency."),
        ("I only have a FIRE TCC. Is that enough?", "No. The IRS tells current FIRE users to complete an IRIS Application for TCC. See our page on whether a FIRE TCC works with IRIS."),
    ],
    sources=["tcc", "p5903", "faq", "p1220", "iris", "efile"],
    cta=("Start the IRIS Application for TCC", "https://www.irs.gov/tax-professionals/iris-application-for-tcc"),
)

PAGES["fire-vs-iris-differences"] = dict(
    title="FIRE vs IRIS: What Replaces FIRE and What Changes",
    h1="FIRE vs IRIS: What Replaces the IRS FIRE System?",
    desc="IRIS replaces the IRS FIRE system for 1099 e-filing. Compare FIRE and IRIS side by side: TCCs, filing methods, Form 1096, corrections and deadlines.",
    og_title="FIRE vs IRIS: What Replaces the IRS FIRE System",
    answer=("<b>IRIS (the Information Returns Intake System) replaces FIRE.</b> FIRE closes after 3 p.m. ET on 19 November 2026, and IRIS is the only IRS system for e-filing information returns in the 2027 filing season."),
    applies=[
        "You e-file 1099s or related forms and want to know what is different in IRIS.",
        "You have used FIRE file uploads and are wondering about the free web option.",
        "You issue corrections to previously filed returns.",
        "You need to explain the change to a client or colleague.",
    ],
    sections=[
        ("compare", "FIRE vs IRIS side by side", (
            table(["", "FIRE", "IRIS"], [
                ["Status", "Last day to file: 19 Nov 2026, 3 p.m. ET", "Only e-file system for tax year 2026 returns (filing season 2027)"],
                ["TCC", "Numeric TCC from the IR Application", "TCC starting with &ldquo;D&rdquo; from the IRIS Application for TCC; works only in IRIS"],
                ["Ways to file", "Upload a formatted file; the IRS says software is required", "Free Taxpayer Portal (type forms in or upload CSV) or Application to Application (A2A) using XML software"],
                ["Volume", "File-based", "Portal: CSV files hold up to 100 records each, unlimited files; A2A: 100MB per file"],
                ["Form 1096 transmittal", "&mdash;", "Not needed: the Form 1096 data is in the IRIS submission header (Form 1096 is for paper filing only)"],
                ["Recipient copies", "&mdash;", "Download and print from the Portal&rsquo;s Submitted Forms tile (Taxpayer Portal)"],
                ["Combined Federal/State", "Supported", "Uses the same CF/SF process as FIRE"],
                ["Form 1099-DA", "Not supported for e-file", "Use IRIS if you must e-file it"],
                ["Corrections", "Until FIRE closes", "IRIS only after 1 January 2027, including prior-year corrections (Pub. 1220)"],
            ])
            + "<p>Sources: IRS IRIS FAQs, Publication 1220 (Rev. 5-2026), IR-2026-99 and the IRS IRIS pages. Some points above, such as Form 1096, are from the IRS FAQs written during the IRIS rollout.</p>")),
        ("same", "What does not change", (
            ul([
                "If you file 10 or more information returns in total, you must e-file (rule effective from 1 January 2024). The count combines all form types across IRIS, FIRE, AIR and Form W-2 submissions.",
                "You still furnish statements to recipients by the usual dates. See the <a href=\"/1099-deadlines-2027-filing-season\">2027 deadlines</a>.",
                "You can still get a 30-day extension to file most 1099s with Form 8809 (not for Forms W-2 and 1099-NEC).",
            ]))),
    ],
    next=[
        'Pick your channel: Taxpayer Portal for small volumes, or A2A through software.',
        'Apply for an <a href="/iris-tcc-application-guide">IRIS TCC</a> if you will file yourself.',
        'Read <a href="/how-to-file-1099-through-iris">how to file 1099s through IRIS</a>.',
        'Use the official <a href="https://www.irs.gov/filing/e-file-information-returns-with-iris" target="_blank" rel="noopener">IRS IRIS page</a> for forms available by tax year.',
    ],
    faq=[
        ("What replaces the IRS FIRE system?", "The Information Returns Intake System (IRIS). The IRS says current FIRE users must use IRIS to file tax year 2026 information returns in the 2027 filing season."),
        ("Is IRIS only for 1099s?", "The IRS e-file page lists the forms IRIS accepts by processing year. Forms 8027 and 8955-SSA are added beginning with filing year 2027, per the IRIS TCC page."),
        ("Do I need new software?", "Not if you use the free Taxpayer Portal. If you use software that sends files to FIRE, ask the vendor whether it supports IRIS A2A."),
        ("Is there still a Form 1096 for IRIS?", "No. The IRS FAQ says you do not file a separate transmittal such as Form 1096 through IRIS. Form 1096 is only for paper filing."),
        ("What happens to corrections?", "Publication 1220 says IRIS will be the only e-file system, including corrections, after 1 January 2027. The IRS had not published full correction details for FIRE-filed returns in the documents we read."),
    ],
    sources=["ir99", "p1220", "faq", "iris", "tcc", "p1099"],
    cta=("Open the official IRIS page on IRS.gov", "https://www.irs.gov/filing/e-file-information-returns-with-iris"),
)

PAGES["does-my-fire-tcc-work-with-iris"] = dict(
    title="Does My FIRE TCC Work With IRIS? Do I Need a New One?",
    h1="Does My FIRE TCC Work With IRIS?",
    desc="Short answer: no. IRIS needs its own TCC. Answer 3 quick questions to find out whether you need a new IRIS TCC and what to do next.",
    og_title="Does My FIRE TCC Work With IRIS?",
    answer=("<b>No.</b> The IRS tells current FIRE users to complete a separate IRIS Application for TCC. "
            "An IRIS TCC starts with the letter D and works only in IRIS, while FIRE TCCs start with a number."),
    applies=[
        "You hold a FIRE TCC and upload your own files to FIRE.",
        "You are not sure whether your software vendor or accountant holds the TCC.",
        "You plan to e-file Forms 1099 in early 2027.",
        "You are an agency, transmitter or software developer.",
    ],
    tool="tcc_tree",
    sections=[
        ("why", "What the IRS says", (
            ul([
                "Publication 1220 (Rev. 5-2026): &ldquo;Current FIRE users must complete an Information Returns Intake System (IRIS) Application for TCC and transition to IRIS for electronic filing beginning with the 2027 filing season.&rdquo;",
                "IRS e-file pages: FIRE TCCs start with a numeric character; IRIS TCCs start with &ldquo;D&rdquo;; and an IRIS TCC &ldquo;can only be used for IRIS&rdquo;.",
                "IR-2026-99 asks filers to &ldquo;complete an IRIS Application for TCC&rdquo;.",
            ])
            + "<p>We found no IRS statement that FIRE TCCs are converted automatically, so treat a new IRIS application as required.</p>")),
        ("change", "Quick comparison", (
            table(["", "FIRE TCC", "IRIS TCC"], [
                ["Format", "Starts with a number", "Starts with D, five digits"],
                ["Works in", "FIRE (closes 19 Nov 2026)", "IRIS only"],
                ["How to get one", "Closed to new applications from 21 July 2026", "IRIS Application for TCC"],
            ]))),
    ],
    next=[
        'Run the decision tree above for your exact next step.',
        'If you need a TCC, start the <a href="https://www.irs.gov/tax-professionals/iris-application-for-tcc" target="_blank" rel="noopener">IRIS Application for TCC</a>.',
        'Check the <a href="/iris-tcc-application-guide">timing calculator</a> so you apply early enough.',
    ],
    faq=[
        ("Do I need a new TCC for IRIS?", "If you file your own returns, yes. The IRS requires current FIRE users to complete an IRIS Application for TCC."),
        ("Can I keep using my FIRE TCC after 19 November 2026?", "FIRE stops accepting submissions after 3 p.m. ET on that date, so there is nothing left to use it for. Pub. 1220 also says existing FIRE applications become read-only after December 2026."),
        ("My payroll provider files my 1099s. Do I need a TCC?", "Usually the provider needs one, not you. Ask them whether they will submit through IRIS in 2027."),
        ("How do I know if a TCC is an IRIS TCC?", "IRIS TCCs start with the letter D, and FIRE TCCs start with a number, according to the IRS e-file page."),
        ("Where can I check my application?", "Sign in through the IRS IRIS Application for TCC page. The Application Summary page shows your TCC once status is Completed."),
    ],
    sources=["p1220", "efile", "iris", "ir99", "tcc", "p5903"],
    cta=("Start the IRIS Application for TCC", "https://www.irs.gov/tax-professionals/iris-application-for-tcc"),
)

PAGES["how-to-file-1099-through-iris"] = dict(
    title="How to File 1099 Through IRIS: Step-by-Step Guide",
    h1="How to File a 1099 Through IRIS",
    desc="Step-by-step: get an IRIS TCC, enter forms in the free Taxpayer Portal or upload CSV, download recipient copies. Plus the 10-return e-file rule.",
    og_title="How to File 1099s Through the IRS IRIS Portal",
    answer=("<b>Get an IRIS TCC, sign in to the IRIS Taxpayer Portal, then type each form in or upload a CSV.</b> The Portal is free and the IRS says it lets you e-file up to 100 returns at a time."),
    applies=[
        "You paid contractors, landlords or others and must file Forms 1099.",
        "You file only a few returns and prefer a free web tool over paid software.",
        "You used FIRE before and need to switch.",
        "You file 10 or more returns in total, so you must e-file.",
    ],
    sections=[
        ("steps", "Filing in the IRIS Taxpayer Portal", (
            steps([
                "<b>Get an IRIS TCC.</b> You need one to use the Portal. See the <a href=\"/iris-tcc-application-guide\">TCC guide</a>.",
                "<b>Choose entry or upload.</b> Enter each form by hand, or upload a CSV using the template for that form (found on the IRIS Dashboard under &ldquo;Upload CSV with Form Data&rdquo;).",
                "<b>Respect CSV rules.</b> Each CSV holds up to 100 records (not counting the header), one form type and one tax year per file. Multiple payers are allowed. You can submit unlimited files.",
                "<b>Submit.</b> You do not file a Form 1096 with IRIS; its data is in the submission header.",
                "<b>Furnish recipient copies.</b> Download and print them from the Portal&rsquo;s Submitted Forms tile, then send by the recipient deadline.",
            ]) + "<p>Sources: IRS IRIS FAQs and Publication 5717 (Taxpayer Portal user guide).</p>")),
        ("a2a", "Using software instead (A2A)", (
            "<p>The Application to Application (A2A) channel is for third-party or self-developed software and larger volumes. A2A uses XML, with a limit of 100MB per file. The IRS runs an Assurance Testing System (ATS) for A2A testing; as of 7 October 2026, ATS transmissions use SchemaVersionNum 5.0.7 for tax years 2022 through 2026.</p>")),
        ("rules", "Rules that still apply", (
            table(["Rule", "Detail"], [
                ["E-file requirement", "10 or more information returns in total (all form types combined) must be e-filed"],
                ["Recipient copies", "Furnish by the form&rsquo;s deadline. See the <a href=\"/1099-deadlines-2027-filing-season\">2027 deadlines</a>"],
                ["Which forms", "The IRS lists IRIS forms by processing year on its IRIS page"],
            ]))),
    ],
    next=[
        'Apply for your <a href="https://www.irs.gov/tax-professionals/iris-application-for-tcc" target="_blank" rel="noopener">IRIS TCC</a> now.',
        'Download the CSV template for your form inside the Portal, and follow the <a href="https://www.irs.gov/pub/irs-pdf/p5717.pdf" target="_blank" rel="noopener">Publication 5717 guide</a>.',
        'Check your <a href="/1099-deadlines-2027-filing-season">deadlines</a> and calendar them.',
        'Collect payee names and TINs early. Contractors can give you Form W-9.',
    ],
    faq=[
        ("How do I file a 1099 through IRIS?", "Apply for an IRIS TCC, sign in to the Taxpayer Portal, then enter forms manually or upload CSV files. The Portal is free."),
        ("Is the IRIS portal free?", "Yes. The IRS describes the IRIS Taxpayer Portal as a free platform."),
        ("How many 1099s can I file at once?", "Each CSV file holds up to 100 records, and the IRS says the Portal lets you e-file up to 100 returns at a time. You can submit more than one file."),
        ("Do I send Form 1096?", "No. The IRS says no separate transmittal such as Form 1096 is needed through IRIS."),
        ("Can I mix 1099-NEC and 1099-MISC in one CSV?", "No. Each form type uses its own template, and all rows in a file must be the same form type and tax year."),
        ("Do I still send payees a copy?", "Yes. You must furnish statements to recipients. The Portal lets you download recipient copies."),
    ],
    sources=["faq", "p5717", "iris", "ir99", "tcc", "p1099"],
    cta=("Open the official IRIS page on IRS.gov", "https://www.irs.gov/filing/e-file-information-returns-with-iris"),
)

PAGES["1099-deadlines-2027-filing-season"] = dict(
    title="1099 Deadlines 2027: When Are 1099s and W-2s Due?",
    h1="When Are 1099s Due in 2027? Deadlines for Tax Year 2026",
    desc="1099-NEC and W-2 are due 1 Feb 2027. Other 1099s: 1 Mar on paper, 31 Mar e-filed. Live next-deadline highlight and calendar (.ics) downloads.",
    og_title="1099 Deadlines for 2027: Dates and Calendar Downloads",
    answer=("<b>Forms 1099-NEC and W-2 are due 1 February 2027</b> (31 January falls on a Sunday). "
            "Most other 1099s are due to recipients by 1 February, and to the IRS by 1 March on paper or 31 March if filed electronically."),
    applies=[
        "You paid a contractor $2,000 or more in 2026 (1099-NEC).",
        "You issue 1099-MISC, 1099-K, 1099-R or 1098-VLI.",
        "You employ people and file W-2s.",
        "You use FIRE today and must switch to IRIS before the 19 November 2026 cutoff.",
    ],
    tool="deadlines",
    sections=[
        ("rules", "How the dates work", (
            ul([
                "The statutory dates are 31 January (NEC, W-2, statements to recipients for most 1099s), 28 February (paper filing of most others) and 31 March (e-filing of most others).",
                "When a due date falls on a Saturday, Sunday or DC legal holiday, the next business day applies. 31 January 2027 and 28 February 2027 are both Sundays. 15 February 2027 is Monday, the federal Washington&rsquo;s Birthday holiday, so the 15 February date for certain forms moves to 16 February.",
                "A leap year does not move 28 February.",
            ]))),
        ("table", "Before and after: what the IRS dates look like", (
            table(["Form", "Statutory date", "2027 date"], [
                ["W-2 (to SSA and employees)", "31 Jan", "1 Feb 2027 (IRS says SSA due date is 1 Feb 2027)"],
                ["1099-NEC (to IRS and recipient)", "31 Jan", "1 Feb 2027"],
                ["1099-MISC, 1099-K, 1099-R, 1098-VLI: recipient copy", "31 Jan", "1 Feb 2027"],
                ["1099-MISC with boxes 8 or 10: recipient copy", "15 Feb", "16 Feb 2027"],
                ["1099-MISC, 1099-K, 1099-R, 1098-VLI: file with IRS on paper", "28 Feb", "1 Mar 2027"],
                ["Same forms: file with IRS electronically", "31 Mar", "31 Mar 2027"],
            ])
            + "<p>The &ldquo;2027 date&rdquo; column applies the IRS rule above to the statutory dates in Publication 1099 (2026). Forms 1099-NEC and W-2 have no automatic extension; for most others Form 8809 gives an automatic 30 days if filed by the due date.</p>")),
        ("gotchas", "Easy-to-miss points", (
            ul([
                "Form 1099-NEC goes to the IRS by the same date it goes to the contractor.",
                "You must e-file if you file 10 or more information returns of any type in total.",
                "IRIS is the only IRS e-file system for these returns. FIRE closes on 19 November 2026.",
            ]))),
    ],
    next=[
        'Download the calendar entries for the dates that apply to you.',
        'Apply for an <a href="/iris-tcc-application-guide">IRIS TCC</a> early if you file yourself.',
        'Collect W-9s from contractors before the year ends.',
        'Confirm dates against IRS.gov/TaxCalendar, which Publication 1099 points to. Our table follows Publication 1099 (2026).',
    ],
    faq=[
        ("When are 1099-NEC forms due in 2027?", "1 February 2027. The statutory date is 31 January, which is a Sunday, so the next business day applies. The same date applies to the IRS and the recipient."),
        ("When is the W-2 deadline for 2027?", "The IRS general instructions say the due date for filing 2026 Forms W-2 and W-3 with the SSA is 1 February 2027, on paper or electronically."),
        ("When are other 1099s due to the IRS?", "28 February (1 March 2027) on paper, or 31 March 2027 if filed electronically. Recipient copies are generally due 31 January (1 February 2027)."),
        ("Can I get an extension?", "For most 1099s, an automatic 30-day extension is available with Form 8809 if filed by the due date. Forms W-2 and 1099-NEC have no automatic extension."),
        ("Does the calendar file send my data anywhere?", "No. The .ics file is created in your browser and downloaded to your device."),
    ],
    sources=["p1099pdf", "p1099", "iw2w3", "i1099mec", "ir99"],
    cta=("Read Publication 1099 on IRS.gov", "https://www.irs.gov/publications/p1099"),
)

PAGES["1099-threshold-600-to-2000"] = dict(
    title="1099 Threshold 2026: Is the $600 Rule Gone? ($2,000 Now)",
    h1="1099 Threshold 2026: Is the $600 Rule Gone?",
    desc="For tax year 2026, 1099-NEC and most 1099-MISC thresholds rise from $600 to $2,000. Check your payment amount against 2025 and 2026 rules.",
    og_title="1099 Threshold for 2026: $600 Becomes $2,000",
    answer=("<b>For most payments made in tax year 2026, the 1099 threshold is $2,000, not $600.</b> The IRS says the change applies to tax years beginning after 2025 and will be adjusted for inflation beginning in 2027."),
    applies=[
        "You pay contractors, freelancers or attorneys and file Form 1099-NEC.",
        "You pay rent, prizes or other amounts reported on Form 1099-MISC.",
        "You backup withhold on a payee (that triggers reporting at any amount).",
        "You wonder whether your 2025 filing used a different rule. It did: $600.",
    ],
    tool="threshold",
    sections=[
        ("table", "Before and after", (
            table(["Form / payment", "Tax year 2025", "Tax year 2026"], [
                ["1099-NEC: services, attorney payments", "$600 or more", "$2,000 or more"],
                ["1099-MISC: rents, prizes, medical payments", "$600 or more", "$2,000 or more"],
                ["1099-MISC: royalties", "$10 or more", "$10 or more (unchanged)"],
                ["W-2 wage reporting (no tax withheld)", "$600", "$2,000"],
                ["1099-K: payment cards", "All amounts", "All amounts (unchanged)"],
                ["1099-K: third party network", "See our <a href=\"/1099-k-2026-changes\">1099-K page</a>", "More than $20,000 and more than 200 transactions"],
                ["1098-VLI (new form)", "n/a", "$600 interest per vehicle loan (its own threshold)"],
                ["1099-S real estate", "Generally $600", "Generally $600 (unchanged)"],
            ])
            + "<p>Sources: Publication 1099 (2026) Guide to Information Returns, Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026), Instructions for Forms W-2 and W-3 (2026). The 2025 NEC figure comes from the prior-year instructions.</p>")),
        ("notes", "Things the threshold does not change", (
            ul([
                "<b>Income is still taxable.</b> The threshold only decides whether a form is required, not whether the payee owes tax.",
                "<b>Backup withholding:</b> you must file a 1099-NEC for any person you backup withheld from, regardless of the amount.",
                "<b>Inflation:</b> the IRS says the $2,000 amount may be adjusted for inflation beginning in calendar year 2027.",
                "<b>State rules</b> may differ; check your state.",
            ]))),
    ],
    next=[
        'Type your payment amount in the tool above for both years.',
        'If you cross $2,000, collect a W-9 and prepare a <a href="/1099-nec-2026-changes">1099-NEC</a>.',
        'Calendar the <a href="/1099-deadlines-2027-filing-season">1 February 2027 deadline</a>.',
        'Read the official <a href="https://www.irs.gov/pub/irs-pdf/i1099mec.pdf" target="_blank" rel="noopener">Form 1099-MISC/NEC instructions</a>.',
    ],
    faq=[
        ("Is the $600 1099 rule gone?", "For Forms 1099-NEC and most 1099-MISC payments in tax year 2026, yes: the minimum is now $2,000. $600 still appears for some forms, such as 1099-S and the new 1098-VLI."),
        ("Does the new $2,000 threshold apply to 2025?", "No. Tax year 2025 returns, filed in early 2026, used $600. The IRS says the increase applies to tax years beginning after 2025."),
        ("What if I paid a contractor $1,500 in 2026?", "You generally need no 1099-NEC, unless you backup withheld on that person. Keep the records anyway."),
        ("Do I still need a W-9?", "The IRS general instructions (Publication 1099) cover TINs and backup withholding. Collecting a W-9 is a common way to get the payee&rsquo;s TIN, so it is sensible to ask before you pay."),
        ("Does the payee still report the income?", "Yes. Receiving no form does not make the income tax-free."),
        ("Does this change Form 1099-K?", "Not for card payments. For third party networks the rule is more than $20,000 and more than 200 transactions."),
    ],
    sources=["p1099pdf", "p1099", "i1099mec", "iw2w3", "i1098vli"],
    cta=("Read the 1099-MISC / 1099-NEC instructions", "https://www.irs.gov/pub/irs-pdf/i1099mec.pdf"),
)

PAGES["1099-nec-2026-changes"] = dict(
    title="1099-NEC 2026 Changes: New Boxes 1a-1d Explained",
    h1="Form 1099-NEC 2026 Changes: New Boxes Explained",
    desc="Form 1099-NEC (Rev. Dec 2026) adds boxes 1b cash tips, 1c TTOC and 1d overtime, and a $2,000 threshold. Before and after box table. Draft status noted.",
    og_title="1099-NEC 2026 Changes: New Boxes 1b, 1c, 1d",
    answer=("<b>The December 2026 Form 1099-NEC adds three boxes under 1a: 1b cash tips, 1c Treasury Tipped Occupation Code (TTOC) and 1d overtime compensation,</b> and the filing threshold rises to $2,000. Use it for payments made in 2026, filed in early 2027."),
    applies=[
        "You pay independent contractors and file Form 1099-NEC.",
        "Your contractors receive tips or paid overtime-style premiums that the law treats as reportable.",
        "You use payroll or accounting software that prints 1099-NEC.",
        "You received a 1099-NEC and want to know what the new boxes mean.",
    ],
    notice=STATUS_NEC,
    sections=[
        ("table", "Box by box: 2025 vs 2026", (
            table(["Box", "2025 form (Rev. April 2025)", "2026 form (Rev. December 2026)"], [
                ["1", "Nonemployee compensation", "<b>1a</b> Nonemployee compensation"],
                ["&mdash;", "(none)", "<b>1b</b> Cash tips <i>(new)</i>"],
                ["&mdash;", "(none)", "<b>1c</b> TTOC <i>(new)</i>"],
                ["&mdash;", "(none)", "<b>1d</b> Overtime compensation <i>(new)</i>"],
                ["2", "Payer made direct sales totaling $5,000 or more", "Same"],
                ["3", "Excess golden parachute payments", "Same"],
                ["4&ndash;7", "Federal and state tax withheld, state number, state income", "Same"],
                ["Threshold", "$600", "$2,000"],
                ["Address fields", "Combined", "Separate entry boxes"],
            ]))),
        ("what", "What goes in the new boxes", (
            ul([
                "<b>1b Cash tips:</b> the total designated as cash tips included in box 1a. This includes tips paid in cash or charged by customers.",
                "<b>1c TTOC:</b> up to two Treasury Tipped Occupation Codes. If any tips came from a non-qualifying occupation, one code must be 000. See <a href=\"/treasury-tipped-occupation-code\">what TTOC is</a>.",
                "<b>1d Overtime compensation:</b> the qualified overtime included in box 1a, which is the part above the regular rate, such as the &ldquo;half&rdquo; of time-and-a-half. See <a href=\"/reporting-overtime-1099-2026\">overtime reporting</a>.",
            ]) + "<p>The amounts in 1b and 1d are already included in the amount in 1a; they are not added on top of it.</p>")),
        ("rules", "Other points from the instructions", (
            ul([
                "Form 1099-NEC is due to the IRS by 31 January (1 February 2027) on paper or electronically, with no automatic extension.",
                "File for any person you backup withheld from, at any amount.",
                "Excess golden parachute payments are no longer reported on Form 1099-MISC; report them on Form 1099-NEC box 3.",
                "The IRS has a continuous-use revision: the December 2026 form is meant for 2026 and later years until replaced.",
            ]))),
    ],
    next=[
        'Check with your payroll or 1099 software that it supports the new boxes.',
        'Gather W-9s and identify contractors who earn tips or overtime.',
        'File by <a href="/1099-deadlines-2027-filing-season">1 February 2027</a>, via <a href="/how-to-file-1099-through-iris">IRIS</a>.',
        'Watch the <a href="https://www.irs.gov/forms-pubs/about-form-1099-nec" target="_blank" rel="noopener">IRS About Form 1099-NEC</a> page for the final release.',
    ],
    faq=[
        ("Is Form 1099-NEC changing for 2026?", "Yes. The December 2026 revision adds boxes 1b, 1c and 1d, renames box 1 as 1a, separates the address fields and applies a $2,000 threshold."),
        ("What is box 1c on Form 1099-NEC?", "The Treasury Tipped Occupation Code (TTOC) for the payee&rsquo;s tipped occupation, up to two codes."),
        ("Do I have to fill boxes 1b to 1d for every contractor?", "Only where the payee had cash tips or qualified overtime. If there are none, they stay blank."),
        ("Is the form final?", "Not confirmed. The IRS describes it as being developed, and early-release copies are marked draft. Confirm on IRS.gov before filing."),
        ("When do I file it?", "1 February 2027 (31 January is a Sunday) for both the IRS and the recipient."),
    ],
    sources=["i1099mec", "f1099nec_dft", "about_nec", "p1099pdf", "drafts"],
    cta=("IRS: About Form 1099-NEC", "https://www.irs.gov/forms-pubs/about-form-1099-nec"),
)

PAGES["reporting-cash-tips-1099-w2-2026"] = dict(
    title="Reporting Cash Tips on W-2 and 1099 in 2026 (Box 12 Code TP)",
    h1="How to Report Cash Tips on W-2 and 1099 in 2026",
    desc="Employers report cash tips in W-2 box 12 code TP with TTOC in box 14b. 1099-NEC box 1b/1c and 1099-K box 1c/1d. Before and after table.",
    og_title="Reporting Cash Tips in 2026: W-2 Box 12 Code TP",
    answer=("<b>On Form W-2, report total cash tips in box 12 with code TP and list the Treasury Tipped Occupation Code in new box 14b.</b> Contractors&rsquo; tips go in Form 1099-NEC boxes 1b and 1c; payment-platform tips go in Form 1099-K boxes 1c and 1d."),
    applies=[
        "You are an employer with tipped employees (restaurants, salons, delivery and similar).",
        "You pay tipped contractors and file Form 1099-NEC or 1099-MISC.",
        "You are a payment processor or platform that files Form 1099-K.",
        "You are a worker who wants to claim the qualified tips deduction and need to know where your tips will show up.",
    ],
    notice=STATUS_W2 + " " + STATUS_NEC.replace("<b>Draft status:</b>", "<b>For 1099 forms:</b>"),
    sections=[
        ("table", "Where cash tips are reported, before and after", (
            table(["Form", "Before (2025)", "2026"], [
                ["W-2", "No box 12 tip code and no occupation-code box", "Box 12 code <b>TP</b> (total cash tips reported to employer); box <b>14b</b> TTOC (up to two codes)"],
                ["1099-NEC", "No tip box", "Box <b>1b</b> cash tips; box <b>1c</b> TTOC"],
                ["1099-MISC", "No tip box", "Box <b>13a</b> cash tips; box <b>13b</b> TTOC"],
                ["1099-K", "No tip box", "Box <b>1c</b> cash tips; box <b>1d</b> TTOC"],
            ])
            + "<p>W-2 box 14 is split: what used to go in box 14 &ldquo;Other&rdquo; now goes in box 14a.</p>")),
        ("rules", "The rules in the IRS instructions", (
            ul([
                "Cash tips include voluntary cash or charged tips from customers and tips through tip-sharing arrangements. Mandatory service charges added to the bill are <b>not</b> qualified tips.",
                "Enter up to two occupation codes. If tips came from more than two occupations, give any two. If any tips came from a non-qualifying occupation, one code must be <b>000</b>.",
                "Tips are still generally subject to federal income tax withholding, social security and Medicare tax if received tips are $20 or more per month.",
                "The employee deduction for qualified tips is up to $25,000 for tax years beginning after 2024 and ending before 2029, for occupations the IRS lists as customarily and regularly receiving tips.",
                "Workers can deduct only qualified tips that appear on Form W-2, 1099-NEC, 1099-MISC or 1099-K, or that they report on Form 4137.",
            ]))),
    ],
    next=[
        'Employers: update payroll so box 12 code TP and box 14b populate for tipped employees.',
        'Look up the <a href="/treasury-tipped-occupation-code">TTOC</a> for each job title you employ.',
        'Contractor payers: use <a href="/1099-nec-2026-changes">1099-NEC boxes 1b and 1c</a>.',
        'Read the <a href="https://www.irs.gov/pub/irs-pdf/iw2w3.pdf" target="_blank" rel="noopener">2026 W-2 instructions</a> on box 12 code TP and box 14b.',
    ],
    faq=[
        ("What is box 12 code TP on the W-2?", "The total amount of cash tips reported to the employer. A box 14b occupation code must also be listed."),
        ("What is box 14b?", "A new box that reports the Treasury Tipped Occupation Code(s), up to two. Box 14 was split into 14a (Other) and 14b."),
        ("Do service charges count?", "No. Mandatory service charges added to the bill are not qualified tips."),
        ("What does the code 000 mean?", "It marks tips from a non-qualifying occupation. If 000 is the only code, the tips are not qualified tips for the deduction."),
        ("Are tips still taxed?", "Yes for payroll taxes. The deduction affects federal income tax only, up to the limit, for qualifying occupations."),
        ("What if my employer didn&rsquo;t report tips correctly?", "Ask for a corrected form (Form W-2c). The IRS 2026 instructions explain how to correct box 14b."),
    ],
    sources=["iw2w3", "i1099mec", "i1099k", "ir49", "about_w2"],
    cta=("Read the 2026 W-2 instructions", "https://www.irs.gov/pub/irs-pdf/iw2w3.pdf"),
)

PAGES["reporting-overtime-1099-2026"] = dict(
    title="Reporting Qualified Overtime in 2026 (W-2 Box 12 Code TT)",
    h1="How to Report Qualified Overtime in 2026 (Box 12 Code TT)",
    desc="Employers report qualified overtime in W-2 box 12 code TT; contractors in 1099-NEC box 1d. Only the premium half counts. Deduction limit $12,500.",
    og_title="Reporting Qualified Overtime in 2026: W-2 Code TT",
    answer=("<b>Employers report qualified overtime in W-2 box 12 with code TT, and payers report it for contractors in Form 1099-NEC box 1d.</b> Only the premium part counts, for example the &ldquo;half&rdquo; of time-and-a-half."),
    applies=[
        "You are an employer who pays FLSA overtime and issues Forms W-2.",
        "You pay contractors and file Form 1099-NEC or 1099-MISC.",
        "You are a worker who wants the qualified overtime deduction.",
        "You are unsure whether your overtime is FLSA overtime at all.",
    ],
    notice=STATUS_W2 + " " + STATUS_NEC.replace("<b>Draft status:</b>", "<b>For 1099 forms:</b>"),
    sections=[
        ("table", "Where overtime is reported, before and after", (
            table(["Form", "Before (2025)", "2026"], [
                ["W-2", "No qualified overtime box", "Box 12 code <b>TT</b>: total qualified overtime compensation"],
                ["1099-NEC", "No overtime box", "Box <b>1d</b> overtime compensation (included in box 1a)"],
                ["1099-MISC", "No overtime box", "Box <b>14</b> overtime compensation"],
            ]))),
        ("what", "What counts as qualified overtime", (
            ul([
                "Compensation required under section 7 of the Fair Labor Standards Act (FLSA) that is more than the regular rate at which the individual is paid.",
                "Only the premium portion is reported. In time-and-a-half, report only the &ldquo;half&rdquo;.",
                "Overtime is still generally subject to income tax withholding and social security and Medicare taxes.",
            ]))),
        ("ded", "The worker&rsquo;s deduction", (
            ul([
                "For tax years beginning after 2024 and ending before 2029, individuals can deduct up to $12,500 ($25,000 on a joint return) of qualified overtime compensation.",
                "The IRS says qualified overtime must be separately reported on Form W-2 to claim the deduction (FS-2026-13).",
                "The amount in box 12 code TT is the total reported, which can be higher than the deduction because of the limit. Other limits can apply; see the IRS FAQs.",
            ]))),
    ],
    next=[
        'Employers: map FLSA premium pay to box 12 code TT in payroll.',
        'Payers of contractors: see the new <a href="/1099-nec-2026-changes">1099-NEC box 1d</a>.',
        'Workers: keep pay stubs and check your W-2 when it arrives in early 2027.',
        'Read the IRS <a href="https://www.irs.gov/pub/taxpros/fs-2026-13.pdf" target="_blank" rel="noopener">overtime FAQs (FS-2026-13)</a>.',
    ],
    faq=[
        ("What is box 12 code TT?", "The total amount of qualified overtime compensation on Form W-2."),
        ("Is all overtime pay reported in TT?", "No. Only the part above the regular rate that the FLSA requires. For time-and-a-half, only the extra half."),
        ("How much overtime can I deduct?", "Up to $12,500, or $25,000 on a joint return, for tax years beginning after 2024 and ending before 2029, subject to other limits in the IRS rules."),
        ("What if my W-2 has no code TT?", "The IRS says qualified overtime must be separately reported on Form W-2 to claim the deduction. Ask your employer about a corrected W-2c."),
        ("Does overtime for contractors count?", "Contractors can be covered: Form 1099-NEC has a box 1d for it. Whether pay is FLSA overtime depends on the facts."),
    ],
    sources=["iw2w3", "fs2026_13", "i1099mec", "about_w2"],
    cta=("Read the IRS overtime FAQs (FS-2026-13)", "https://www.irs.gov/pub/taxpros/fs-2026-13.pdf"),
)

PAGES["treasury-tipped-occupation-code"] = dict(
    title="Treasury Tipped Occupation Code (TTOC): What It Is",
    h1="What Is the Treasury Tipped Occupation Code (TTOC)?",
    desc="TTOC is the three-digit IRS code for a tipped job, reported on 2026 W-2, 1099-NEC and 1099-K forms. How it works, the 000 code and where to find the list.",
    og_title="What Is a Treasury Tipped Occupation Code (TTOC)?",
    answer=("<b>A TTOC is the three-digit code the IRS assigns to each occupation that customarily and regularly receives tips.</b> Payers report it next to cash tips on 2026 Forms W-2, 1099-NEC, 1099-MISC and 1099-K."),
    applies=[
        "You are an employer or payer that reports cash tips.",
        "You are a tipped worker who wants the qualified tips deduction.",
        "You see a code in box 14b (W-2), 1c (1099-NEC) or 1d (1099-K) and wonder what it means.",
        "You work two jobs, only one of them tipped.",
    ],
    sections=[
        ("what", "How TTOC works", (
            ul([
                "The IRS list of occupations is classified by the Treasury Tipped Occupation Code system. Each occupation has a three-digit code and description.",
                "The final regulations (IR-2026-49, 10 April 2026) list more than 70 tipped occupations in eight categories, from the 100s (beverage and food service) to the 800s (transportation and delivery).",
                "Only occupations that customarily and regularly received tips on or before 31 December 2024 are included.",
                "Tips from an occupation not on the list are not eligible for the deduction.",
            ]))),
        ("table", "Where the TTOC goes", (
            table(["Form", "Box"], [
                ["W-2", "Box 14b (up to two codes), alongside box 12 code TP"],
                ["1099-NEC", "Box 1c"],
                ["1099-MISC", "Box 13b"],
                ["1099-K", "Box 1d"],
            ])
            + "<p>Enter up to two codes. If tips came from more than two occupations, enter any two. If any tips came from a non-qualifying occupation, one code must be <b>000</b>. If 000 is the only code, the tips are not qualified tips.</p>")),
        ("find", "Where to find your code", (
            "<p>The IRS instructions point to IRS.gov/TippedOccupations and IRS.gov/TTOC for the list of codes. The list itself is in the final regulations (<a href=\"https://www.federalregister.gov/public-inspection/2026-07104/occupations-that-customarily-and-regularly-received-tips-definition-of-qualified-tips\" target=\"_blank\" rel=\"noopener\">Federal Register</a>). "
            "We do not reproduce individual codes here because we could not verify the final numbers on a page we fetched, and wrong codes cause wrong forms.</p>")),
    ],
    next=[
        'Employers: find each tipped job title on the IRS list and store its code in payroll.',
        'Workers: check your W-2 box 14b matches your real job.',
        'Read <a href="/reporting-cash-tips-1099-w2-2026">how to report cash tips</a>.',
        'Read the <a href="https://www.irs.gov/newsroom/treasury-irs-issue-final-regulations-listing-occupations-where-workers-customarily-and-regularly-receive-tips-under-the-one-big-beautiful-bill" target="_blank" rel="noopener">IRS release on the final list</a>.',
    ],
    faq=[
        ("What does TTOC stand for?", "Treasury Tipped Occupation Code."),
        ("How many digits is a TTOC?", "Three. Each occupation has a three-digit code and a description."),
        ("What does 000 mean?", "It marks tips from a non-qualifying occupation. If it is the only code, the tips are not qualified tips for the deduction."),
        ("Can I have more than one TTOC?", "Yes, up to two on the form. If you had tips in more than two occupations, the payer lists any two."),
        ("Are gig workers covered?", "The IRS says gig workers and other self-employed people can qualify if their occupation is on the list. The deduction for self-employed people is limited to net income."),
        ("Which occupations are on the list?", "More than 70, in eight categories. See the IRS-linked final regulations for the exact list."),
    ],
    sources=["ir49", "iw2w3", "i1099mec", "i1099k"],
    cta=("IRS release: final tipped occupations list", "https://www.irs.gov/newsroom/treasury-irs-issue-final-regulations-listing-occupations-where-workers-customarily-and-regularly-receive-tips-under-the-one-big-beautiful-bill"),
)

PAGES["form-1098-vli-vehicle-loan-interest"] = dict(
    title="Form 1098-VLI: Vehicle Loan Interest Statement Explained",
    h1="Form 1098-VLI: Vehicle Loan Interest Statement",
    desc="Form 1098-VLI reports $600+ of vehicle loan interest per loan. Who files it, boxes 1-7, loan rules, due dates and the car loan interest deduction.",
    og_title="Form 1098-VLI: Vehicle Loan Interest Statement Explained",
    answer=("<b>Form 1098-VLI is the new IRS form lenders use to report $600 or more of interest received on a vehicle loan in a calendar year.</b> One form per loan. It supports the new &ldquo;No Tax on Car Loan Interest&rdquo; deduction."),
    applies=[
        "You are a lender, dealer or servicer that received $600 or more of interest on one loan in the course of a trade or business.",
        "You took out a loan after 2024 for a new personal-use vehicle assembled in the US and secured by a first lien.",
        "You are a borrower expecting the form in early 2027.",
        "You are not the lender: an individual who lends privately outside any business does not file.",
    ],
    notice=("<b>Draft status:</b> the IRS has posted Form 1098-VLI (December 2026) and its instructions, and the form still carries a draft marking. IRS Publication 1179 (Rev. 7-2026) said "
            "Form 1098-VLI had &ldquo;not yet been released to the public for filing/furnishing&rdquo; and that a notice would be posted on release. We did not find that release notice, so treat the form as not final."),
    sections=[
        ("table", "What the form reports", (
            table(["Box", "Content"], [
                ["1", "Vehicle loan interest received by lender"],
                ["2a&ndash;2d", "Vehicle year, make, model and VIN"],
                ["3a / 3b", "Loan origination date / loan acquisition date"],
                ["4", "Outstanding principal"],
                ["5", "Refund of overpaid interest"],
                ["6", "Original use of the vehicle began with the payer of record"],
                ["7", "Final assembly of the vehicle occurred within the United States"],
            ])
            + "<p>Box layout from the early-release draft dated 8/20/26. It could change.</p>")),
        ("rules", "Who and what qualifies", (
            ul([
                "<b>Threshold:</b> $600 or more of interest per loan. Each loan is separate, even if one borrower paid more than $600 in total across loans.",
                "<b>Loan:</b> a specified passenger vehicle loan is indebtedness incurred after 2024 to buy an applicable passenger vehicle for personal use, secured by a first lien.",
                "<b>Vehicle:</b> car, minivan, van, SUV, pickup truck or motorcycle; at least 2 wheels; gross vehicle weight rating under 14,000 lb; final assembly in the US; original use begins with the payer of record.",
                "<b>Payer of record:</b> must be an individual, decedent&rsquo;s estate or nongrantor trust. Do not file if the payer is a nonresident alien.",
                "<b>Related lenders:</b> loans owed to a related person are not specified passenger vehicle loans.",
            ]))),
        ("dates", "Deadlines and the borrower side", (
            table(["Item", "Date"], [
                ["Statement to borrower", "31 Jan (1 Feb 2027, since 31 Jan is a Sunday)"],
                ["File with IRS, paper", "28 Feb (1 Mar 2027)"],
                ["File with IRS, electronic", "31 Mar 2027"],
            ])
            + "<p>Borrowers: the draft 2026 Schedule 1-A has a Part IV, &ldquo;No Tax on Car Loan Interest&rdquo;, and notes that certain vehicle loan interest paid in 2026 should be reported on Form 1098-VLI box 1. We do not state the deduction amount or income limits here because we did not verify them.</p>")),
    ],
    next=[
        'Lenders: confirm your loan servicing system can flag first-lien vehicle loans originated after 2024 and capture VIN and final-assembly data.',
        'Check the IRS page for the final release before filing.',
        'Borrowers: keep your lender statements and VIN, and wait for the form in early 2027.',
        'Read the <a href="https://www.irs.gov/pub/irs-pdf/i1098vli.pdf" target="_blank" rel="noopener">Form 1098-VLI instructions</a>.',
    ],
    faq=[
        ("What is Form 1098-VLI?", "A Vehicle Loan Interest Statement that a business lender files to report $600 or more of specified passenger vehicle loan interest received from an individual, estate or nongrantor trust."),
        ("Do I get a form for each loan?", "Yes. The $600 threshold applies loan by loan."),
        ("Does a lender file for a used car loan?", "The instructions require that original use of the vehicle begin with the payer of record, so a used vehicle generally does not qualify."),
        ("Is the form final?", "Not confirmed. Publication 1179 (Rev. 7-2026) listed it among forms not yet released for filing and furnishing."),
        ("Does a loan before 2025 qualify?", "No. A specified passenger vehicle loan is debt incurred after 2024."),
        ("When will borrowers get it?", "Statements are due to borrowers on 31 January, which becomes 1 February 2027."),
    ],
    sources=["i1098vli", "f1098vli", "p1179", "s1a", "p1099pdf"],
    cta=("Read the Form 1098-VLI instructions", "https://www.irs.gov/pub/irs-pdf/i1098vli.pdf"),
)

PAGES["1099-r-box-7-changes-2026"] = dict(
    title="1099-R Box 7a, 7b, 7c, 7d Changes for 2026 Explained",
    h1="Form 1099-R Box 7a, 7b, 7c and 7d: 2026 Changes",
    desc="2026 Form 1099-R splits box 7 into 7a-7d, adds a Trump account checkbox and box 8a/8b. Before and after table with code Y for QCDs.",
    og_title="1099-R Box 7a-7d Changes for 2026",
    answer=("<b>On the 2026 Form 1099-R, box 7 is split into 7a (distribution code) and 7b (IRA/SEP/SIMPLE), with two new boxes: 7c (Trump account) and 7d (earnings on excess contributions).</b> Box 8 also becomes 8a and 8b."),
    applies=[
        "You issue Form 1099-R for retirement plans, IRAs or annuities.",
        "You received a 2026 Form 1099-R and see unfamiliar boxes.",
        "You handle qualified charitable distributions (QCDs) from IRAs.",
        "You administer Trump accounts, the new type of IRA for children under 18.",
    ],
    notice=("<b>Status:</b> the IRS has posted a 2026 Form 1099-R (created 4/2/26) and 2026 Instructions for Forms 1099-R and 5498. A separate early-release draft labelled 2027 also exists, dated 9/22/26, with the same box layout. This page covers 2026."),
    sections=[
        ("table", "Before and after", (
            table(["Box", "2025 form", "2026 form"], [
                ["7", "Distribution code(s) plus an IRA/SEP/SIMPLE checkbox", "<b>7a</b> Distribution code(s); <b>7b</b> IRA/SEP/SIMPLE checkbox"],
                ["&mdash;", "(none)", "<b>7c</b> Trump account checkbox <i>(new)</i>"],
                ["&mdash;", "(none)", "<b>7d</b> Earnings on excess contributions <i>(new)</i>"],
                ["8", "Other, and percentage", "<b>8a</b> Other; <b>8b</b> percentage of annuity contract"],
                ["Addresses", "Combined", "Separate entry boxes for payer and recipient"],
            ]))),
        ("new", "What is new in the instructions", (
            ul([
                "<b>Box 7c:</b> enter an &ldquo;X&rdquo; if the distribution is from a Trump account.",
                "<b>Box 7d:</b> the earnings on excess contributions distributed from a Trump account that are included in box 1. Enter 0 if there are losses.",
                "<b>Code Y in box 7a:</b> new code for a qualified charitable distribution (QCD). For tax year 2026 using code Y is optional.",
                "<b>Box 8a:</b> for 2026, issuers of annuitized commercial annuity contracts are not required to enter the year-end value in 8a.",
                "<b>Later years:</b> for tax years after 2026, qualified long-term care distributions will be reported on Form 1099-R. Form 5498 gets a new code HP in box 14b.",
            ]))),
        ("dates", "Due dates", (
            "<p>Recipient copies are due 31 January (1 February 2027). The IRS copy is due 28 February (1 March 2027) on paper or 31 March 2027 electronically. See the <a href=\"/1099-deadlines-2027-filing-season\">deadline table</a>.</p>")),
    ],
    next=[
        'Issuers: update your 1099-R software for boxes 7a to 7d and 8a/8b.',
        'Recipients: if you see an X in box 7c, the distribution came from a Trump account.',
        'File through <a href="/how-to-file-1099-through-iris">IRIS</a>; FIRE closes 19 November 2026.',
        'Read the <a href="https://www.irs.gov/pub/irs-pdf/i1099r.pdf" target="_blank" rel="noopener">2026 instructions for Forms 1099-R and 5498</a>.',
    ],
    faq=[
        ("What are boxes 7a, 7b, 7c and 7d?", "7a is the distribution code, 7b the IRA/SEP/SIMPLE checkbox, 7c the Trump account checkbox and 7d earnings on excess contributions from a Trump account."),
        ("Is box 7c about every account?", "No. It is only for distributions from a Trump account."),
        ("Is code Y required for QCDs in 2026?", "No. The IRS says using code Y to report a QCD is optional for tax year 2026."),
        ("Why did box 8 change?", "Box 8 and the percentage box were renumbered 8a and 8b. Reporting the actuarial value in 8a is optional for 2026 annuitized contracts."),
        ("Does this change my tax?", "No. These are reporting changes. Your tax depends on the distribution. Check the instructions or a tax professional."),
    ],
    sources=["i1099r", "f1099r", "p1099pdf", "iw2w3"],
    cta=("Read the 1099-R / 5498 instructions", "https://www.irs.gov/pub/irs-pdf/i1099r.pdf"),
)

PAGES["1099-k-2026-changes"] = dict(
    title="1099-K 2026 Changes: $20,000 Threshold and Cash Tips Box",
    h1="Form 1099-K 2026 Changes: Threshold and New Tips Boxes",
    desc="For 2026 the 1099-K third-party threshold is more than $20,000 and 200 transactions. The form adds box 1c cash tips and 1d TTOC. Before/after table.",
    og_title="1099-K 2026: $20,000 Threshold, Cash Tips Box 1c",
    answer=("<b>For 2026, a payment app or marketplace issues Form 1099-K only if you have more than $20,000 and more than 200 transactions.</b> Payment card payments have no minimum. The form also adds box 1c (cash tips) and 1d (TTOC)."),
    applies=[
        "You sell goods or services through payment apps, marketplaces or online platforms.",
        "You accept payment cards for a business.",
        "You are a payment settlement entity that files Form 1099-K.",
        "You received a 1099-K for under $20,000 and are wondering why.",
    ],
    notice=STATUS_K,
    sections=[
        ("table", "Before and after", (
            table(["", "Before", "Now"], [
                ["Third party network threshold", "The ARPA-era (American Rescue Plan Act of 2021) threshold, which the IRS says was retroactively replaced", "More than $20,000 and more than 200 transactions"],
                ["Payment card transactions", "No minimum", "No minimum (unchanged)"],
                ["Cash tips", "No box", "<b>Box 1c</b> cash tips <i>(new)</i>"],
                ["TTOC", "No box", "<b>Box 1d</b> TTOC <i>(new)</i>"],
                ["Addresses", "Combined", "Separate entry boxes"],
            ])
            + "<p>The IRS says the One, Big, Beautiful Bill restored the earlier $20,000 and 200-transaction rule (IRS FAQ announced 17 November 2025). Box 2 (merchant category code) is unchanged.</p>")),
        ("notes", "Points people get wrong", (
            ul([
                "<b>Income is taxable at any amount.</b> The IRS says that no matter the amount of reported payments, you report all income on your return.",
                "<b>You can still get a form below the threshold.</b> A third party settlement organization may send a 1099-K for lower amounts, and your state may have a lower threshold.",
                "<b>Card payments:</b> the IRS FAQ says that if you received $0.01 of payments from a payment card transaction, you should receive a Form 1099-K.",
                "<b>Backup withholding:</b> in IR-2026-03 (8 January 2026) Treasury and the IRS proposed regulations under which certain third-party settlement organizations generally do not have to backup withhold unless the payee exceeds $20,000 and 200 transactions. They are proposals, not final.",
            ]))),
    ],
    next=[
        'Sellers: track all platform income yourself and report it, whether or not you receive a 1099-K.',
        'Filers: update systems for boxes 1c and 1d and check the final IRS release.',
        'Compare against the <a href="/1099-threshold-600-to-2000">1099-NEC/MISC threshold</a> change, which is separate.',
        'Read the <a href="https://www.irs.gov/instructions/i1099k" target="_blank" rel="noopener">Form 1099-K instructions</a>.',
    ],
    faq=[
        ("What is the 1099-K threshold for 2026?", "For third party network transactions, more than $20,000 in aggregate payments and more than 200 transactions. For payment cards there is no threshold."),
        ("Did the lower ARPA-era 1099-K threshold take effect?", "The IRS says the One, Big, Beautiful Bill retroactively reinstated the threshold in effect before the American Rescue Plan Act of 2021: more than $20,000 and more than 200 transactions."),
        ("What is box 1c on Form 1099-K?", "The total cash tips included in box 1a."),
        ("What is box 1d?", "The Treasury Tipped Occupation Code (TTOC), up to two codes. Use 000 if any tips were in a non-qualifying occupation."),
        ("I sold less than $20,000. Do I owe tax?", "The threshold only affects whether a form is issued. You must report taxable income regardless."),
        ("Is the form final?", "Not confirmed. The IRS describes the December 2026 revision as under development, and an early-release draft is posted."),
    ],
    sources=["i1099k", "kfaq", "kfaq_general", "ir03", "about_k", "f1099k_dft", "p1099pdf"],
    cta=("IRS: Form 1099-K instructions", "https://www.irs.gov/instructions/i1099k"),
)
