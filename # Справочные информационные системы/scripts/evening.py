# -*- coding: utf-8 -*-
"""Вечерний прогон (после 20:00 МСК): тексты документов по пунктам 1, 3 и 5 задания 3.2."""
from kpfree import *
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
RES = json.load(open(os.path.join(HERE, 'res32a.json'), encoding='utf-8'))
OUT = os.path.join(HERE, 'evening.json')

JOBS = [
    ('1', '32_1_text', ['декларац', 'налог на добавленную стоимость', 'строк']),
    ('5', '32_5_text', ['взаимодейств', 'обмен информацией', 'Стороны']),
    ('3', '32_3_text', ['Дебет', 'Кредит', 'страхов']),
]

out = {}
with sync_playwright() as pw:
    br, page = browser(pw)
    for key, shotname, marks in JOBS:
        url = RES[key]['url']
        page.goto(url, wait_until='domcontentloaded')
        page.wait_for_timeout(11000)
        shot(page, shotname)
        texts = []
        for fr in page.frames:
            try:
                texts.append(fr.evaluate("document.body?document.body.innerText:''"))
            except Exception:
                pass
        t = max(texts, key=len) if texts else ''
        avail = 'расписани' not in t and 'недоступен' not in t
        out[key] = {'title': RES[key]['title'], 'len': len(t), 'available': avail, 'text': t}
        print('=== пункт %s | символов %d | доступен: %s' % (key, len(t), avail), flush=True)
        if avail:
            for m in marks:
                for line in t.split('\n'):
                    if re.search(m, line, re.I) and len(line.strip()) > 40:
                        print('  >', line.strip()[:220], flush=True)
                        break
        else:
            print('  ', t[:220].replace('\n', ' | '), flush=True)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    br.close()
print('СОХРАНЕНО:', OUT)
