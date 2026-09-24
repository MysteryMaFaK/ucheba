# -*- coding: utf-8 -*-
"""Скриншоты для отчёта 4.1: каталог ФБ ННГУ + 4 ЭБС. Edge headless, 2x DPI."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots')
Q = 'государственное регулирование экономики'
QU = 'ГОСУДАРСТВЕННОЕ РЕГУЛИРОВАНИЕ ЭКОНОМИКИ'

def shot(page, name):
    p = os.path.join(OUT, name + '.png')
    page.screenshot(path=p)
    print('OK', name)

def kill_cookie(page):
    page.evaluate("""() => {
      document.querySelectorAll('div,section,aside').forEach(e=>{
        const t=(e.innerText||'');
        if(t.length<600 && /cookie|куки|файлы cookie/i.test(t)) e.style.display='none';
      });
      document.body.style.overflow='auto';
    }""")

with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width':1280,'height':800}, device_scale_factor=2,
                         locale='ru-RU')
    page = ctx.new_page()
    page.set_default_timeout(45000)

    # --- 1.1 Сайт ФБ ННГУ, пункт "Электронный каталог"
    page.goto('https://lib.unn.ru/', wait_until='domcontentloaded')
    page.wait_for_timeout(3000)
    kill_cookie(page)
    shot(page, '01_lib_unn_main')

    # --- 1.2 Электронный каталог (МегаПро)
    page.goto('https://e-lib.unn.ru/MegaPro/Web', wait_until='domcontentloaded')
    page.wait_for_timeout(2500)
    shot(page, '02_megapro_main')

    # --- 1.3 Расширенный поиск: заполненная форма
    page.goto('https://e-lib.unn.ru/MegaPro/Web/Search/Ext', wait_until='domcontentloaded')
    page.wait_for_timeout(2000)
    page.select_option('#dict_0', '33')          # Ключевые слова
    page.select_option('#cond_0', '1')           # Включает
    page.fill('#term_0', QU)
    page.fill('input[name="filter_dateFrom"]', '2021')
    page.fill('input[name="filter_dateTo"]', '2026')
    page.check('input[name="filter_docType_mnv"]')   # Книги
    page.wait_for_timeout(700)
    shot(page, '03_megapro_ext_form')

    # --- 1.4 Результаты поиска
    page.click('input.search_button')
    page.wait_for_timeout(5000)
    shot(page, '04_megapro_results')

    # --- 2.1 Раздел ЭБС на сайте ФБ ННГУ
    page.goto('https://lib.unn.ru/elektronnye-resursy/elektronno-bibliotechnye-sistemy/',
              wait_until='domcontentloaded')
    page.wait_for_timeout(3000)
    kill_cookie(page)
    shot(page, '05_lib_unn_ebs')

    br.close()
print('DONE')
