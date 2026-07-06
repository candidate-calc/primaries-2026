# -*- coding: utf-8 -*-
import re, json, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(BASE,'research','candidates-page.html'), encoding='utf-8').read()
tags = re.findall(r'<img[^>]+class="attachment-large[^>]+>', html)
photos = []
for t in tags:
    src = re.search(r'src="([^"]+)"', t).group(1)
    if any(x in src for x in ('website.svg','CVd2.png','logo','.svg')): continue
    photos.append(src)
print('photo count:', len(photos))
names = ['משה_רדמן','ערן_עציון','מורן_זר','יעל_כהן','לי_הופמן','רם_שפע','יריב_אופנהיימר','אוליביה','נאור_נרקיס','מהרטה','עמרי_רונן','ירון_ניב','רתם_סיון','אליס_גולדמן','אבי_דבוש','דימה','בנימין','ענבר_בזק','גיל_ביילין','יאיר_רובינשטיין','דני_אלגרט','אמיר','הדס_רגולסקי','אבישי','חן_אריאלי','מיכל_רוזין','ערן_ניסן','אפרת_רייטן','קטי','אחסאן','נדאל','ענבל','יאיא_פינק','עאיד','נאווה_רוזוליו','מאלכ','איתי_לשם','גלעד_קריב','גאלב','יואב_אגמי','אמילי_מואטי','אביתר','תומר_אביטל','סומיה','מורן_מישל','גבי_לסקי','נעמה_לזימי','איהאב','מוסי_רז','עלי_סלאלחה','נמרוד_שפר']
match, mism = [], []
for i, src in enumerate(photos):
    if i < len(names):
        (match if names[i] in src else mism).append((i+1, src.split('/')[-1][:70]))
print('name-in-url matches:', len(match), '| no-name-in-url:', len(mism))
with open(os.path.join(BASE,'research','photo-map.json'),'w',encoding='utf-8') as f:
    json.dump(photos, f, ensure_ascii=False, indent=1)
with open(os.path.join(BASE,'research','photo-mismatch.txt'),'w',encoding='utf-8') as f:
    for i,s in mism: f.write(f'{i}: {s}\n')
