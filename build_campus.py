import json,html,base64,datetime,sys
sys.path.insert(0,'.')
from study_more import G2
B="https://shuhratjon1010.github.io/cramvault/"
exec(open('build_study_guides.py').read().split('from study_more')[0].split('def enc')[0])  # loads G (first 10)
ALL={s:(n,c) for s,n,e,c in G+G2}
CS=[("Big-O of binary search","O(log n)"),("Recursion needs","A base case and a smaller subproblem"),("Stack vs queue","LIFO vs FIFO"),("Hash table average lookup","O(1)"),("Python list append cost","Amortized O(1)"),("Pass-by-reference risk","Mutating a shared object changes it everywhere")]
ALL["cs"]=("Intro Computer Science",CS)
CH="general-chemistry-chem-101"; OC="organic-chemistry-ii-chem-202"; BI="cell-biology-bio-101"; CA="calculus-i-math-101"; ST="ap-statistics"; LA="linear-algebra-math-201"
U=[
("uc-berkeley","UC Berkeley","Berkeley, CA",[("CHEM 3A",OC),("CS 61A","cs"),("MATH 51",CA)]),
("ucla","UCLA","Los Angeles, CA",[("CHEM 14A",CH),("LIFESCI 7A",BI),("MATH 31A",CA)]),
("university-of-michigan","University of Michigan","Ann Arbor, MI",[("CHEM 210",OC),("EECS 280","cs"),("MATH 115",CA)]),
("ut-austin","UT Austin","Austin, TX",[("CH 301",CH),("BIO 311C",BI),("M 408C",CA)]),
("university-of-florida","University of Florida","Gainesville, FL",[("CHM 2045",CH),("BSC 2010",BI),("MAC 2311",CA)]),
("nyu","NYU","New York, NY",[("CHEM-UA 125",CH),("CSCI-UA 101","cs"),("MATH-UA 121",CA)]),
("ohio-state","Ohio State University","Columbus, OH",[("CHEM 1210",CH),("BIOLOGY 1113",BI),("MATH 1151",CA)]),
("penn-state","Penn State","University Park, PA",[("CHEM 110",CH),("BIOL 110",BI),("MATH 140",CA)]),
("university-of-washington","University of Washington","Seattle, WA",[("CHEM 142",CH),("BIOL 180",BI),("MATH 124",CA)]),
("unc-chapel-hill","UNC Chapel Hill","Chapel Hill, NC",[("CHEM 101",CH),("BIOL 101",BI),("MATH 231",CA)]),
("georgia-tech","Georgia Tech","Atlanta, GA",[("CHEM 1310",CH),("CS 1301","cs"),("MATH 1551",CA)]),
("uiuc","University of Illinois Urbana-Champaign","Champaign, IL",[("CHEM 102",CH),("CS 124","cs"),("MATH 221",CA)]),
("uw-madison","UW–Madison","Madison, WI",[("CHEM 103",CH),("COMP SCI 300","cs"),("MATH 221",CA)]),
("purdue","Purdue University","West Lafayette, IN",[("CHM 11500",CH),("CS 18000","cs"),("MA 16100",CA)]),
("usc","USC","Los Angeles, CA",[("CHEM 105a",CH),("BISC 120",BI),("MATH 125g",CA)]),
("cornell","Cornell University","Ithaca, NY",[("CHEM 2070",CH),("CS 1110","cs"),("MATH 1910",CA)]),
("columbia","Columbia University","New York, NY",[("CHEM UN1403",CH),("COMS W1004","cs"),("MATH UN1101",CA)]),
("upenn","University of Pennsylvania","Philadelphia, PA",[("CHEM 1012",CH),("CIS 1200","cs"),("MATH 1400",CA)]),
("harvard","Harvard University","Cambridge, MA",[("CS 50","cs"),("STAT 110",ST),("MATH 21b",LA)]),
("stanford","Stanford University","Stanford, CA",[("CS 106A","cs"),("CHEM 31A",CH),("MATH 51",LA)]),
]
def enc(p): return base64.urlsafe_b64encode(json.dumps(p,ensure_ascii=False,separators=(",",":")).encode()).decode().rstrip("=")
import os; os.makedirs("campus",exist_ok=True)
for i,(slug,name,city,courses) in enumerate(U):
    url=f"{B}campus/{slug}.html"
    cards=[]; 
    for code,key in courses: cards+=[(f"{code}: {f}",b) for f,b in ALL[key][1][:2]]
    codes=" / ".join(c for c,_ in courses)
    deck=f"{B}deck/import.html#"+enc({"v":1,"t":f"{name} {codes} — Cram Vault Starter Deck","c":name,"cards":[list(c) for c in cards],"ref":"campus"})
    faq=[(f"How do I study for {courses[0][0]} at {name}?",f"Record each {courses[0][0]} lecture on-device with Cram Vault. It builds a 1-page cheat sheet with timestamps and FSRS flashcards that resurface what you are about to forget before the midterm."),
         (f"Is Cram Vault affiliated with {name}?",f"No. Cram Vault is an independent study app; course codes are listed only so {name} students can find relevant starter decks."),
         ("Does it work offline in the lecture hall?","Yes. Transcription, the whiteboard scanner and flashcard scheduling all run on-device.")]
    ld=[{"@context":"https://schema.org","@type":"EducationalOrganization","name":name,"address":{"@type":"PostalAddress","addressLocality":city.split(", ")[0],"addressRegion":city.split(", ")[1],"addressCountry":"US"},
         "hasCourse":[{"@type":"Course","name":f"{code} exam prep","courseCode":code,"description":f"Starter flashcards for {name} {code} ({ALL[k][0]}).","provider":{"@type":"Organization","name":"Cram Vault","sameAs":B}} for code,k in courses]},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]
    ch="".join(f'<button class="card" onclick="this.classList.toggle(\'f\')"><span class="q">{html.escape(f)}</span><span class="a">{html.escape(b)}</span></button>' for f,b in cards)
    cl="".join(f'<li><b>{html.escape(code)}</b> — {html.escape(ALL[k][0])}'+(f' · <a href="../study/{k}.html">full study guide</a>' if k!="cs" else "")+'</li>' for code,k in courses)
    more="".join(f'<li><a href="{U[(i+k)%len(U)][0]}.html">{html.escape(U[(i+k)%len(U)][1])}</a></li>' for k in range(1,6))
    open(f"campus/{slug}.html","w").write(f"""<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name)} Exam Prep: {html.escape(codes)} Flashcards | Cram Vault</title>
<meta name="description" content="Free {html.escape(name)} exam-prep flashcards for {html.escape(codes)}. Flip the cards, then import the starter deck into Cram Vault.">
<link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(name)} Exam Prep"><meta property="og:url" content="{url}"><meta property="og:image" content="{B}assets/cram_vault_icon_1024.png">
{"".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in ld)}
<style>body{{font-family:-apple-system,system-ui,sans-serif;background:#0f0d2e;color:#eef;max-width:820px;margin:auto;padding:24px;line-height:1.6}}a{{color:#40d9ff}}h1{{color:#33e699}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}}.card{{background:#1f1c47;color:#eef;border:1px solid #33e69966;border-radius:16px;min-height:120px;padding:16px;font-size:16px;cursor:pointer;text-align:left}}
.card .a{{display:none;color:#ffc84d}}.card.f .q{{display:none}}.card.f .a{{display:block}}.cta{{display:inline-block;background:linear-gradient(90deg,#33e699,#40d9ff);color:#000;padding:14px 22px;border-radius:14px;font-weight:700;text-decoration:none;margin:6px 6px 6px 0}}small{{color:#99a}}</style></head>
<body><a href="../index.html">← Cram Vault</a> · <a href="index.html">All campuses</a> · <a href="../study/index.html">Study guides</a>
<h1>{html.escape(name)} Exam Prep: {html.escape(codes)}</h1>
<p>High-yield starter flashcards for big intro courses at {html.escape(name)} ({html.escape(city)}). Tap a card to flip it, then import the deck so FSRS spaced repetition schedules every card before your midterm.</p>
<h2>Courses</h2><ul>{cl}</ul>
<div class="grid">{ch}</div>
<p><a class="cta" href="{deck}">Import this deck</a><a class="cta" href="https://apps.apple.com/us/search?term=cram%20vault">Get Cram Vault on the App Store</a></p>
<h2>FAQ</h2>{"".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q,a in faq)}
<h2>More campuses</h2><ul>{more}</ul>
<p><small>Cram Vault is not affiliated with or endorsed by {html.escape(name)}.</small></p>
<p><a href="../privacy.html">Privacy</a> · <a href="../terms.html">Terms</a> · <a href="../support.html">Support</a></p></body></html>""")
idx="".join(f'<li><a href="{s}.html">{html.escape(n)}</a> — {html.escape(" / ".join(c for c,_ in cs))}</li>' for s,n,_,cs in U)
open("campus/index.html","w").write(f"""<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>US University Exam Prep Hubs | Cram Vault</title><link rel="canonical" href="{B}campus/">
<meta name="description" content="Free exam-prep flashcards for intro courses at 20 major US universities."><style>body{{font-family:-apple-system,system-ui;background:#0f0d2e;color:#eef;max-width:760px;margin:auto;padding:24px;line-height:1.8}}a{{color:#40d9ff}}</style></head>
<body><a href="../index.html">← Cram Vault</a> · <a href="../study/index.html">Study guides</a><h1>US University Exam Prep Hubs</h1><ul>{idx}</ul></body></html>""")
s=open("llms.txt").read().split("\n## Campus exam hubs")[0].rstrip()
s+="\n\n## Campus exam hubs\n"+"".join(f"- [{n}]({B}campus/{sl}.html): {' / '.join(c for c,_ in cs)} starter flashcards\n" for sl,n,_,cs in U)
open("llms.txt","w").write(s)
print(len(U))
