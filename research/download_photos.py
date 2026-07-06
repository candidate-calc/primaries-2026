# -*- coding: utf-8 -*-
import json, os, io, urllib.request, urllib.parse
from PIL import Image
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = os.path.join(BASE, 'docs', 'photos')
os.makedirs(PHOTOS, exist_ok=True)
urls = json.load(open(os.path.join(BASE,'research','photo-map.json'), encoding='utf-8'))
assert len(urls) == 51
ok, fail = 0, []
for i, url in enumerate(urls, 1):
    out = os.path.join(PHOTOS, f'{i:02d}.jpg')
    if os.path.exists(out): ok += 1; continue
    try:
        q = urllib.parse.quote(url, safe=':/')
        req = urllib.request.Request(q, headers={'User-Agent':'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=30).read()
        img = Image.open(io.BytesIO(data)).convert('RGB')
        img.thumbnail((240, 240))
        img.save(out, 'JPEG', quality=82)
        ok += 1
    except Exception as e:
        fail.append((i, str(e)[:80]))
print('ok:', ok, 'failed:', fail)
