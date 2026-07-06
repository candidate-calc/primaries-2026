# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(BASE,'docs','data.js'), encoding='utf-8').read()
d = json.loads(src[src.index('=')+1:].rstrip(';'))
with open(os.path.join(BASE,'research','links-check.txt'),'w',encoding='utf-8') as f:
    for c in d['candidates']:
        f.write("%02d: wiki=%s site=%s\n" % (c['id'], 'Y' if c['wiki'] else '-', c['site'] or '-'))
print('ok')
