# -*- coding: utf-8 -*-
"""Скриншоты 4 ЭБС: поиск + библиографическая запись."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots')
Q = 'государственное регулирование экономики'

def shot(page, name):
    page.screenshot(path=os.path.join(OUT, name + '.png'))
    print('OK', name)

def kill_cookie(page):
    page.evaluate("""() => {
      document.querySelectorAll('div,section,aside,app-cookie-alert').forEach(e=>{
        const t=(e.innerText||'');
        if(t.length<600 && /cookie|куки/i.test(t)) e.style.display='none';
      });
      document.body.style.overflow='auto';
    }""")

with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width':1280,'height':800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page(); page.set_default_timeout(45000)

    # ---------- ЮРАЙТ ----------
    page.goto('https://urait.ru/search?words=' + Q.replace(' ', '+'), wait_until='domcontentloaded')
    page.wait_for_timeout(6000); kill_cookie(page)
    try:
        page.get_by_text('Для вузов', exact=True).first.click(timeout=5000)
        page.wait_for_timeout(5000)
    except Exception as e:
        print('urait filter skip:', e)
    kill_cookie(page)
    shot(page, '06_urait_search')

    page.goto('https://urait.ru/bcode/584675', wait_until='domcontentloaded')
    page.wait_for_timeout(6000); kill_cookie(page)
    shot(page, '07_urait_book')

    # ---------- ЛАНЬ ----------
    page.goto('https://e.lanbook.com/search?query=' + Q.replace(' ', '%20'), wait_until='domcontentloaded')
    page.wait_for_timeout(7000); kill_cookie(page)
    shot(page, '08_lan_search')

    page.goto('https://e.lanbook.com/book/522974', wait_until='domcontentloaded')
    page.wait_for_timeout(7000); kill_cookie(page)
    try:
        page.get_by_text('Библиографическая запись', exact=True).first.click(timeout=5000)
        page.wait_for_timeout(1500)
    except Exception as e:
        print('lan bib skip:', e)
    page.evaluate("""() => {const el=[...document.querySelectorAll('*')].find(e=>/^Библиографическая запись/.test(e.innerText||'')&&e.children.length<6); if(el) el.scrollIntoView({block:'center'});}""")
    page.wait_for_timeout(1000)
    shot(page, '09_lan_bib')

    # ---------- ZNANIUM ----------
    page.goto('https://znanium.ru/catalog/wide-search?submitted=1&title=' + Q.replace(' ', '+'),
              wait_until='domcontentloaded')
    page.wait_for_timeout(6000); kill_cookie(page)
    shot(page, '10_znanium_search')

    page.goto('https://znanium.ru/catalog/document?id=430281', wait_until='domcontentloaded')
    page.wait_for_timeout(5000); kill_cookie(page)
    try:
        page.get_by_text('Бибзапись', exact=True).first.click(timeout=5000)
        page.wait_for_timeout(2000)
    except Exception as e:
        print('znanium bib skip:', e)
    page.evaluate("""() => {const el=[...document.querySelectorAll('*')].find(e=>/^Бибзапись/.test(e.innerText||'')&&e.children.length<6); if(el) el.scrollIntoView({block:'center'});}""")
    page.wait_for_timeout(1000)
    shot(page, '11_znanium_bib')

    # ---------- КОНСУЛЬТАНТ СТУДЕНТА ----------
    page.goto('https://www.studentlibrary.ru/', wait_until='domcontentloaded')
    page.wait_for_timeout(5000); kill_cookie(page)
    page.evaluate("""(q) => {
        document.getElementById('SearchText').value = q;
        const f = document.getElementById('frm_rds'); f.target='_top';
        call_submit('frm_rds','','','search');
    }""", Q)
    page.wait_for_timeout(8000); kill_cookie(page)
    shot(page, '12_studentlib_search')

    page.goto('https://www.studentlibrary.ru/ru/book/ISBN9785001720324.html', wait_until='domcontentloaded')
    page.wait_for_timeout(6000); kill_cookie(page)
    shot(page, '13_studentlib_bib')

    br.close()
print('DONE')
