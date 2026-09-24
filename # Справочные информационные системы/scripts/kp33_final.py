# -*- coding: utf-8 -*-
"""Задание 3.3, КонсультантПлюс: финальный прогон по нормативным документам."""
from kp33 import *

# (номер, запрос, индекс документа в выдаче, ключи для вырезки фрагмента)
PLAN = [
 (1, 'социальный вычет лекарственные препараты рецептурный бланк сведения из медицинской документации',
     1, ['рецептурн', 'назначени']),
 (2, 'признаки платежеспособности банкнот Банка России ветхие посторонние надписи',
     3, ['надпис', 'ветх']),
 (4, 'социальный налоговый вычет обучение иностранная организация дистанционная форма обучения',
     2, ['иностранной организации', 'обучение своих детей']),
 (5, 'письмо минфина дни приезда и отъезда 183 дня резидент НДФЛ',
     0, ['приезда']),
 (6, 'письмо минфина задаток включается в налоговую базу по НДС',
     0, ['задат']),
 (7, 'передача подарков сотрудникам НДС статья 146 НК РФ',
     2, ['подарк']),
 (8, 'Приказ Росстата указания по заполнению формы П-4 средняя численность работников',
     0, ['средняя численность', 'средней численности']),
]

result = {}
with sync_playwright() as pw:
    br, page = browser(pw)
    for num, query, idx, keys in PLAN:
        print(f'--- задание {num}')
        quick_search(page, query)
        try:
            page.get_by_text('Законодательство', exact=True).first.click()
            page.wait_for_timeout(6000)
        except Exception:
            pass
        shot(page, f'n{num}_1_list')

        items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
            .map(a=>({t:(a.innerText||'').replace(/\\s+/g,' ').trim(), h:a.getAttribute('href')}))""")
        if idx >= len(items):
            print('   !! мало результатов:', len(items)); continue
        it = items[idx]
        page.goto('https://www.consultant.ru/cons/cgi/' + it['h'].replace('../cgi/', ''),
                  wait_until='domcontentloaded')
        page.wait_for_timeout(11000)
        shot(page, f'n{num}_2_doc')

        texts = []
        for fr in page.frames:
            try:
                texts.append(fr.evaluate("document.body ? document.body.innerText : ''"))
            except Exception:
                pass
        txt = max(texts, key=len) if texts else ''
        frag, low = '', txt.lower()
        for k in keys:
            i = low.find(k.lower())
            if i > 0:
                frag = txt[max(0, i - 900): i + 2400]
                break
        if not frag:
            frag = txt[:2600]
        result[num] = {'query': query, 'title': it['t'][:220], 'url': page.url,
                       'len': len(txt), 'fragment': frag}
        print('   ', it['t'][:110])
        print('    len:', len(txt))
    br.close()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kp33_final.json'),
          'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('SAVED')
