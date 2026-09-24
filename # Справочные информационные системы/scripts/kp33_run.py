# -*- coding: utf-8 -*-
"""Задание 3.3: поиск ответов на 8 вопросов в КонсультантПлюс, скриншоты и фрагменты."""
from kp33 import *

TASKS = [
    (1, 'социальный налоговый вычет на лечение если нет рецепта врача на лекарства',
        ['рецепт', 'лекарств']),
    (2, 'признаки ветхих банкнот банка россии надпись', ['ветх', 'надпис']),
    (4, 'вычет НДФЛ на обучение за границей дистанционное обучение', ['за границ', 'дистанцион']),
    (5, 'учитываются ли дни приезда и отъезда иностранного гражданина при подсчете 183 дней НДФЛ',
        ['день приезда', 'дни приезда', 'отъезда']),
    (6, 'нужно ли начислять НДС при получении задатка', ['задат']),
    (7, 'облагается ли НДС передача подарков сотрудникам организации', ['подарк']),
    (8, 'формула расчета средней численности работников в целях применения УСН',
        ['средн', 'численност']),
]

result = {}

with sync_playwright() as pw:
    br, page = browser(pw)
    for num, query, keys in TASKS:
        print(f'--- задание {num}: {query}')
        quick_search(page, query)
        shot(page, f't{num}_1_list')

        link = page.locator('a[href*="req=doc"]').first
        title = (link.inner_text() or '').strip()
        # клик по ссылке выдачи не меняет страницу — переходим по адресу документа напрямую
        href = link.get_attribute('href')
        page.goto('https://www.consultant.ru/cons/cgi/' + href.replace('../cgi/', ''),
                  wait_until='domcontentloaded')
        page.wait_for_timeout(11000)
        shot(page, f't{num}_2_doc')

        url = page.url
        # текст документа лежит во вложенном фрейме — берём самый «толстый»
        texts = []
        for fr in page.frames:
            try:
                texts.append(fr.evaluate("document.body ? document.body.innerText : ''"))
            except Exception:
                pass
        txt = max(texts, key=len) if texts else ''
        # окно текста вокруг первого найденного ключевого слова
        frag, low = '', txt.lower()
        for k in keys:
            i = low.find(k.lower())
            if i > 0:
                frag = txt[max(0, i - 700): i + 1800]
                break
        if not frag:
            frag = txt[:2200]
        result[num] = {'query': query, 'title': title, 'url': url, 'fragment': frag}
        print('   ', title[:90].replace('\n', ' | '))
        print('    url:', url[:120])

    br.close()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kp33.json'),
          'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('SAVED kp33.json')
