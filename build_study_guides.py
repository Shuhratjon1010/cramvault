import json, html, base64, datetime
B="https://shuhratjon1010.github.io/cramvault/"
G=[
("usmle-step-1-pharmacology","USMLE Step 1 Pharmacology","USMLE Step 1",[("Antidote for warfarin","Vitamin K (+ PCC/FFP for urgent reversal)"),("Antidote for heparin","Protamine sulfate"),("Beta-blocker overdose antidote","Glucagon"),("MOA of metformin","Decreases hepatic gluconeogenesis; activates AMPK"),("Drug class causing dry cough + angioedema","ACE inhibitors (bradykinin buildup)"),("Acetaminophen overdose antidote","N-acetylcysteine")]),
("sat-math-reading","SAT Math & Reading","SAT",[("Slope formula","m = (y2 − y1) / (x2 − x1)"),("Quadratic formula","x = (−b ± √(b² − 4ac)) / 2a"),("Area of a circle","A = πr²"),("Main idea question strategy","Read the first and last sentence of each paragraph"),("Command of evidence","Pick the line that directly supports your previous answer"),("Percent change","(new − old) / old × 100")]),
("cpa-far-accounting","CPA FAR Financial Accounting","CPA Exam (FAR)",[("Accounting equation","Assets = Liabilities + Equity"),("Lease classification (ASC 842) test","Ownership transfer, purchase option, major part of life, PV ≥ substantially all FV, specialized asset"),("Straight-line depreciation","(Cost − Salvage) / Useful life"),("Revenue recognition 5 steps","Contract, obligations, price, allocate, recognize"),("Working capital","Current assets − Current liabilities"),("Gain on bond retirement","Carrying value − Reacquisition price")]),
("bar-exam-mbe-contracts-torts","Bar Exam MBE Contracts & Torts","Bar Exam (MBE)",[("Elements of negligence","Duty, breach, causation, damages"),("Mailbox rule","Acceptance is effective upon dispatch"),("UCC 2-207 applies to","Sale of goods between merchants with additional terms"),("Res ipsa loquitur","Accident normally requires negligence + defendant had exclusive control"),("Consideration","Bargained-for exchange of legal detriment"),("Statute of frauds (MY LEGS)","Marriage, Year, Land, Executor, Goods ≥ $500, Surety")]),
("ap-biology","AP Biology","AP Biology",[("Function of mitochondria","ATP production via cellular respiration"),("Photosynthesis equation","6CO2 + 6H2O → C6H12O6 + 6O2"),("Hardy-Weinberg","p² + 2pq + q² = 1"),("Where is glycolysis?","Cytoplasm"),("Enzyme effect on activation energy","Lowers it"),("Mitosis phases","Prophase, metaphase, anaphase, telophase")]),
("ap-calculus-bc","AP Calculus BC","AP Calculus BC",[("Derivative of sin x","cos x"),("Integration by parts","∫u dv = uv − ∫v du"),("Ratio test converges if","lim |a(n+1)/a(n)| < 1"),("Taylor series of e^x","Σ xⁿ / n!"),("Arc length (parametric)","∫√((dx/dt)² + (dy/dt)²) dt"),("Polar area","½ ∫ r² dθ")]),
("ap-chemistry","AP Chemistry","AP Chemistry",[("Ideal gas law","PV = nRT"),("Gibbs free energy","ΔG = ΔH − TΔS"),("pH definition","pH = −log[H⁺]"),("Henderson–Hasselbalch","pH = pKa + log([A⁻]/[HA])"),("Molarity","M = mol solute / L solution"),("Spontaneous reaction when","ΔG < 0")]),
("general-chemistry-chem-101","General Chemistry I (CHEM 101)","CHEM 101",[("Avogadro's number","6.022 × 10²³ per mol"),("Density","d = m / V"),("Electron configuration order","1s 2s 2p 3s 3p 4s 3d"),("Limiting reagent","Reactant that is used up first"),("Percent yield","actual / theoretical × 100"),("VSEPR shape of CH4","Tetrahedral, 109.5°")]),
("anatomy-physiology-bio-201","Anatomy & Physiology (BIO 201)","BIO 201",[("Largest organ","Skin (integumentary system)"),("SA node function","Natural pacemaker of the heart"),("Functional unit of kidney","Nephron"),("Neurotransmitter at neuromuscular junction","Acetylcholine"),("Number of bones in adult body","206"),("Where gas exchange occurs","Alveoli")]),
("microeconomics-econ-101","Microeconomics (ECON 101)","ECON 101",[("Price elasticity of demand","%ΔQd / %ΔP"),("Profit-maximizing rule","Produce where MR = MC"),("Opportunity cost","Value of the next best alternative forgone"),("Consumer surplus","Willingness to pay − price paid"),("Perfect competition long run","P = MC = min ATC, zero economic profit"),("Price ceiling effect","Shortage when set below equilibrium")]),
]
def enc(p):
    return base64.urlsafe_b64encode(json.dumps(p,ensure_ascii=False,separators=(",",":")).encode()).decode().rstrip("=")
for slug,name,exam,cards in G:
    url=f"{B}study/{slug}.html"
    deck=f"{B}deck/import.html#"+enc({"v":1,"t":f"{name} — Cram Vault Starter Deck","c":exam,"cards":[list(c) for c in cards],"ref":"web"})
    faq=[(f"What is the fastest way to study for {name}?",f"Record lectures on-device with Cram Vault, then review the auto-generated FSRS flashcards daily — it schedules the {name} cards you're about to forget first."),
         (f"Can I import my Quizlet or Anki deck for {exam}?","Yes. Paste any term-tab-definition export into Cram Vault › Import and it becomes an FSRS deck plus a 1-page cheat sheet."),
         ("Is Cram Vault free?","Every student gets a 24-Hour Free Cram Pass. Sharing a deck with a classmate adds another 24 hours.")]
    ld=[{"@context":"https://schema.org","@type":"Course","name":f"{name} Study Guide","description":f"High-yield {name} flashcards, formulas and exam tips with FSRS spaced repetition.","url":url,"inLanguage":"en-US",
         "provider":{"@type":"Organization","name":"Cram Vault","sameAs":B},"educationalLevel":exam,"isAccessibleForFree":True,
         "hasCourseInstance":{"@type":"CourseInstance","courseMode":"online","courseWorkload":"PT20M"},"offers":{"@type":"Offer","price":"0","priceCurrency":"USD","category":"Free"}},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]
    cardsh="".join(f'<button class="card" onclick="this.classList.toggle(\'f\')"><span class="q">{html.escape(f)}</span><span class="a">{html.escape(b)}</span></button>' for f,b in cards)
    faqh="".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q,a in faq)
    open(f"study/{slug}.html","w").write(f"""<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name)} Study Guide &amp; Flashcards (2026) | Cram Vault</title>
<meta name="description" content="Free {html.escape(name)} flashcards and high-yield facts for US students. Flip the cards, then import the full deck into Cram Vault for FSRS spaced repetition.">
<link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(name)} Study Guide"><meta property="og:url" content="{url}"><meta property="og:image" content="{B}assets/cram_vault_icon_1024.png">
{"".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in ld)}
<style>body{{font-family:-apple-system,system-ui,sans-serif;background:#0f0d2e;color:#eef;max-width:820px;margin:auto;padding:24px;line-height:1.6}}a{{color:#40d9ff}}h1{{color:#33e699}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}}.card{{background:#1f1c47;color:#eef;border:1px solid #33e69966;border-radius:16px;min-height:120px;padding:16px;font-size:16px;cursor:pointer;text-align:left}}
.card .a{{display:none;color:#ffc84d}}.card.f .q{{display:none}}.card.f .a{{display:block}}.cta{{display:inline-block;background:linear-gradient(90deg,#33e699,#40d9ff);color:#000;padding:14px 22px;border-radius:14px;font-weight:700;text-decoration:none;margin:6px 6px 6px 0}}</style></head>
<body><a href="../index.html">← Cram Vault</a> · <a href="index.html">All study guides</a><h1>{html.escape(name)} Study Guide &amp; Flashcards</h1>
<p>High-yield {html.escape(name)} facts for US students. Tap a card to flip it, then import the whole deck into Cram Vault so FSRS spaced repetition schedules each card right before you'd forget it.</p>
<div class="grid">{cardsh}</div>
<p><a class="cta" href="{deck}">Import this deck</a><a class="cta" href="https://apps.apple.com/us/search?term=cram%20vault">Get Cram Vault on the App Store</a></p>
<h2>FAQ</h2>{faqh}<p><a href="../privacy.html">Privacy</a> · <a href="../terms.html">Terms</a> · <a href="../support.html">Support</a></p></body></html>""")
idx="".join(f'<li><a href="{s}.html">{html.escape(n)}</a> — {html.escape(e)}</li>' for s,n,e,_ in G)
open("study/index.html","w").write(f"""<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>US Exam &amp; Course Study Guides | Cram Vault</title><link rel="canonical" href="{B}study/">
<meta name="description" content="Free flashcard study guides for USMLE, SAT, CPA, Bar Exam, AP and intro college courses."><style>body{{font-family:-apple-system,system-ui;background:#0f0d2e;color:#eef;max-width:760px;margin:auto;padding:24px;line-height:1.8}}a{{color:#40d9ff}}</style></head>
<body><a href="../index.html">← Cram Vault</a><h1>US Exam &amp; Course Study Guides</h1><ul>{idx}</ul></body></html>""")
# llms.txt section
s=open("llms.txt").read().split("\n## Study guides")[0].rstrip()
s+="\n\n## Study guides\n"+"".join(f"- [{n}]({B}study/{sl}.html): free {n} flashcards and FAQ\n" for sl,n,_,_ in G)
open("llms.txt","w").write(s)
print(len(G))
