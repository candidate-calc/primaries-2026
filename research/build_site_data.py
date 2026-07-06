# -*- coding: utf-8 -*-
# מייצר docs/data.js לאתר: דירוגים (מה-CSV) + תוכן קובצי ה-MD.
import csv, json, os, glob, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(BASE, 'docs')
os.makedirs(DOCS, exist_ok=True)

TOPICS = ["ביטחון וחטופים","דמוקרטיה ומשפט","דת ומדינה ושוויון בנטל","הסדרה ושלום",
          "שוויון אזרחי ושותפות","כלכלה עבודה ורווחה","חינוך ובריאות","סביבה ואקלים",
          "שקיפות וטוהר מידות","מגדר ולהט\"ב"]
TRAITS = ["יושרה","חריצות וביצוע","אומץ ציבורי","חיבור ועבודה רוחבית","מקצועיות וניסיון"]
TDIMS = ["הצהרות","תקשורת","שטח","הצלחה","קרדיט"]
CDIMS = ["עדות עצמית","קרדיט עמיתים","תקשורת","שטח"]

def read_csv(name):
    with open(os.path.join(BASE,'research',name), encoding='utf-8-sig') as f:
        return list(csv.reader(f))

trows = read_csv('ratings-topics.csv')[1:]
crows = read_csv('ratings-traits.csv')[1:]

cands = []
cmap = {int(r[0]): r for r in crows}
dossier_files = {int(os.path.basename(p).split('-')[0]): os.path.basename(p)
                 for p in glob.glob(os.path.join(BASE,'candidates','*.md'))}
for r in trows:
    i = int(r[0]); name = r[1]; ev = float(r[2])
    vals = [float(x) for x in r[3:]]
    T = [vals[t*5:(t+1)*5] for t in range(10)]
    cv = [float(x) for x in cmap[i][2:]]
    C = [cv[c*4:(c+1)*4] for c in range(5)]
    cands.append({'id': i, 'name': name, 'ev': ev, 'T': T, 'C': C, 'file': dossier_files.get(i,'')})

docs = {}
for fn in ['README.md','01-plan.md','02-sources.md','03-topics-traits.md','04-scoring-method.md']:
    with open(os.path.join(BASE,fn), encoding='utf-8') as f: docs[fn] = f.read()
dossiers = {}
for i, fn in dossier_files.items():
    with open(os.path.join(BASE,'candidates',fn), encoding='utf-8') as f: dossiers[i] = f.read()

data = {
 'topics': TOPICS, 'traits': TRAITS, 'tdims': TDIMS, 'cdims': CDIMS,
 'candidates': cands,
 'defaults': {'wT':[5]*10, 'wC':[5]*5, 'alpha':[1,1,2,3,2], 'gamma':[0.5,2,2,1.5], 'lam':0.7, 'beta':0.25},
 'docs': docs, 'dossiers': dossiers,
 'meta': {'collected':'6.7.2026','vote':'20.7.2026'}
}
with open(os.path.join(DOCS,'data.js'),'w',encoding='utf-8') as f:
    f.write('window.PRIMARIES_DATA = ')
    json.dump(data, f, ensure_ascii=False)
    f.write(';')

shutil.copy2(os.path.join(BASE,'primaries-scoring.xlsx'), os.path.join(DOCS,'primaries-scoring.xlsx'))
print('data.js written,', len(cands), 'candidates,', len(dossiers), 'dossiers')
