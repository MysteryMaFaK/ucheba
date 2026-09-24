# -*- coding: utf-8 -*-
"""Скриншоты для отчёта 2.1: портал госуслуг НО + публичная база нотариусов ФНП."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots21')
os.makedirs(OUT, exist_ok=True)

SERVICE = ('https://gu.nnov.ru/services/31c7f896-8ac6-4898-8e72-317b89c33ef7'
           '/targets/167c116a-d66e-4c73-8492-c983dc3235cc/?onlyOneTarget=Y')
NOTARY = ('https://data.notariat.ru/directory/notary/?last_name=&first_name=&middle_name='
          '&chamber__region_id=52&address=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4')

CLEAN = """() => {
  document.querySelectorAll('div,section,aside').forEach(e=>{
    const t=(e.innerText||'');
    if(t.length<700 && /(cookie|куки|метаданные пользователя|Робот Макс|Чат бот)/i.test(t)) e.style.display='none';
  });
  document.body.style.overflow='auto';
}"""


def shot(page, name):
    page.screenshot(path=os.path.join(OUT, name + '.png'))
    print('OK', name)


def portal_search(page, query, name):
    # /search/ без параметров отдаёт страницу без видимого поля — ищем с главной
    page.goto('https://gu.nnov.ru/', wait_until='domcontentloaded')
    page.wait_for_timeout(7000)
    page.evaluate(CLEAN)
    box = page.locator('input[placeholder="Введите запрос"]:visible').first
    box.click()
    box.type(query, delay=15)
    page.keyboard.press('Enter')
    page.wait_for_timeout(7000)
    page.evaluate(CLEAN)
    shot(page, name)


with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page(); page.set_default_timeout(60000)

    # --- портал госуслуг НО
    page.goto('https://gu.nnov.ru/', wait_until='domcontentloaded')
    page.wait_for_timeout(7000); page.evaluate(CLEAN)
    shot(page, '01_gu_main')

    page.goto('https://gu.nnov.ru/services/', wait_until='domcontentloaded')
    page.wait_for_timeout(7000); page.evaluate(CLEAN)
    shot(page, '02_gu_catalog')

    portal_search(page, 'материальной помощи гражданам, находящимся в трудной жизненной ситуации',
                  '03_gu_search_tzs')

    page.goto(SERVICE, wait_until='domcontentloaded')
    page.wait_for_timeout(7000); page.evaluate(CLEAN)
    shot(page, '04_gu_service_about')

    page.evaluate("""() => {
      const t=[...document.querySelectorAll('*')].find(e=>e.textContent.trim()==='Подробнее'&&e.children.length===0);
      if(t) t.click();
    }""")
    page.wait_for_timeout(4000); page.evaluate(CLEAN)
    shot(page, '05_gu_service_details')

    # --- УСЗН и город
    page.goto('https://nnsovuszn.ru/?page_id=825', wait_until='domcontentloaded')
    page.wait_for_timeout(6000); page.evaluate(CLEAN)
    shot(page, '06_uszn_tzs')

    page.goto('https://admgor.nnov.ru/Gorod/Napravleniya-raboty/Socialnaya-politika/'
              'Dopolnitelnaya-adresnaya-pomoshch-grazhdanam-semyam-nahodyashchimsya-v-trudnoy-zhiznennoy-situacii',
              wait_until='domcontentloaded')
    page.wait_for_timeout(6000); page.evaluate(CLEAN)
    shot(page, '07_admgor_help')

    # --- публичная база нотариусов ФНП
    page.goto('https://data.notariat.ru/directory/notary/', wait_until='domcontentloaded')
    page.wait_for_timeout(5000); page.evaluate(CLEAN)
    shot(page, '08_notary_form')

    page.goto(NOTARY, wait_until='domcontentloaded')
    page.wait_for_timeout(5000); page.evaluate(CLEAN)
    shot(page, '09_notary_results')

    page.goto('https://data.notariat.ru/directory/chambers/', wait_until='domcontentloaded')
    page.wait_for_timeout(5000); page.evaluate(CLEAN)
    shot(page, '10_notary_chambers')

    page.goto('https://data.notariat.ru/directory/succession/search/', wait_until='domcontentloaded')
    page.wait_for_timeout(5000); page.evaluate(CLEAN)
    shot(page, '11_notary_succession')

    br.close()
print('DONE')
