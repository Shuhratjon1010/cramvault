import json, html
BASE="https://shuhratjon1010.github.io/cramvault/"
APP={"@context":"https://schema.org","@type":"SoftwareApplication","name":"Cram Vault","operatingSystem":"iOS, iPadOS","applicationCategory":"EducationalApplication",
 "offers":[{"@type":"Offer","price":"0","priceCurrency":"USD","description":"24-Hour Free Cram Pass"},{"@type":"Offer","price":"9.99","priceCurrency":"USD","description":"Instant Exam Pass"},{"@type":"Offer","price":"39.99","priceCurrency":"USD","description":"Semester & Annual Pass"}],
 "description":"On-device AI lecture recorder and whiteboard scanner that builds a 1-page exam cheat sheet, FSRS flashcards and timed quizzes."}
P=[
("mcat-study-app.html","MCAT Study App — Biochem Lecture Notes, Flashcards & Timed Quizzes","MCAT","MCAT biochemistry, glycolysis, Krebs cycle and rate-limiting enzymes",
 [("Which enzymes are rate-limiting for the MCAT?","PFK-1 for glycolysis and isocitrate dehydrogenase for the Krebs cycle — Cram Vault flags these as high-yield automatically."),("Does it work without Wi-Fi?","Yes. Transcription, OCR and flashcard generation run 100% on your iPhone or iPad.")]),
("nclex-nursing-notes.html","NCLEX Nursing Notes App — Pharmacology Cheat Sheets & Flashcards","NCLEX-RN","high-alert cardiac meds, digoxin, heparin and warfarin antidotes",
 [("Can I turn nursing lectures into NCLEX flashcards?","Record your pharmacology lecture and Cram Vault builds FSRS spaced-repetition cards like 'Antidote for heparin → protamine sulfate'."),("Is patient data uploaded?","No. Audio never leaves your device.")]),
("ap-exam-cram-sheet.html","AP Exam Cram Sheet Maker — APUSH, AP Bio, AP Chem 1-Page Notes","AP Exams","AP US History, the Constitutional Convention and the Federalist Papers",
 [("How do I make a 1-page AP cram sheet?","Record class, snap the board, and tap Export PDF — Cram Vault prints a US-Letter 1-page sheet."),("Is it free?","Every student gets a 24-Hour Free Cram Pass.")]),
("organic-chemistry-lecture-notes.html","Organic Chemistry Lecture Notes App — SN1/SN2 Mechanisms & Formulas","Organic Chemistry","SN1 vs SN2 mechanisms, rate laws and leaving groups",
 [("Can it read reaction mechanisms off the whiteboard?","Cram Vault perspective-corrects the board and uses accurate on-device text recognition to pull rate laws and formulas."),("Can I jump to where the professor explained it?","Yes — every bullet is Tap-to-Timestamp.")]),
("lsat-law-school-briefs.html","LSAT & Law School Briefs App — Case Notes, Outlines & Flashcards","LSAT & Law School","case briefs, black-letter rules and cold-call prep",
 [("Can it brief a law school lecture?","Cram Vault detects definitions and 'this will be on the exam' cues to build rule outlines and flashcards."),("Does it help LSAT prep?","Turn LSAT course lectures into flashcards and timed 4-option quizzes.")]),
]
for fn,title,exam,topic,faq in P:
    url=BASE+fn
    howto={"@context":"https://schema.org","@type":"HowTo","name":f"How to turn a {exam} lecture into a 1-page cheat sheet","step":[{"@type":"HowToStep","position":i+1,"text":t} for i,t in enumerate(["Open Cram Vault and tap Record — no login needed.","Snap the whiteboard whenever the professor writes a formula.","Tap Finish to get your 1-page cheat sheet, flashcards and timed quiz.","Study with FSRS flashcards until your Exam Readiness hits 90%+."])]}
    fq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    app=dict(APP,url=url)
    ld="\n".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in (app,fq,howto))
    faqh="".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q,a in faq)
    open(fn,"w").write(f"""<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | Cram Vault</title><meta name="description" content="Cram Vault for {exam}: record lectures on-device, scan whiteboards, and get a 1-page cheat sheet, FSRS flashcards and timed quizzes on {topic}.">
<link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}assets/cram_vault_icon_1024.png">
{ld}
<style>body{{font-family:-apple-system,system-ui,sans-serif;background:#0f0d2e;color:#eef;max-width:760px;margin:auto;padding:24px;line-height:1.6}}a{{color:#40d9ff}}h1{{color:#33e699}}.cta{{display:inline-block;background:linear-gradient(90deg,#33e699,#40d9ff);color:#000;padding:14px 22px;border-radius:14px;font-weight:700;text-decoration:none}}</style></head>
<body><a href="index.html">← Cram Vault</a><h1>{html.escape(title)}</h1>
<p>Built for US {exam} students: Cram Vault records your lecture with on-device speech recognition, scans the whiteboard, and turns {topic} into a <b>1-page exam cheat sheet</b>, <b>FSRS spaced-repetition flashcards</b> and a <b>timed 4-option quiz</b> with an Exam Readiness Score.</p>
<p><a class="cta" href="https://apps.apple.com/us/search?term=cram%20vault">Start your 24-Hour Free Cram Pass</a></p>
<h2>How it works</h2><ol>{"".join(f"<li>{s['text']}</li>" for s in howto['step'])}</ol>
<h2>Pricing (USD)</h2><p>24-Hour Free Cram Pass · $9.99 Instant Exam Pass · $39.99/year Semester &amp; Annual Pass.</p>
<h2>FAQ</h2>{faqh}<p><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="support.html">Support</a></p></body></html>""")
print("ok",len(P))
