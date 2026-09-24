# -*- coding: utf-8 -*-
"""Каркас для задания 3.3: быстрый поиск в КонсультантПлюс + открытие документа."""
import os, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots33')
os.makedirs(OUT, exist_ok=True)
SPLUS = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&page=splus'

CLEAN = """() => {
  document.querySelectorAll('div,section,aside').forEach(e=>{
    const t=(e.innerText||'');
    if(t.length<500 && /(Пробный доступ|Индивидуальное предложение|cookie)/i.test(t)) e.style.display='none';
  });
}"""


def shot(page, name):
    page.evaluate(CLEAN)
    page.screenshot(path=os.path.join(OUT, name + '.png'))
    print('  OK', name)


def browser(pw, headless=True):
    br = pw.chromium.launch(channel='msedge', headless=headless)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page()
    page.set_default_timeout(45000)
    return br, page


def quick_search(page, query):
    """Быстрый поиск: вводим вопрос, жмём «Найти», возвращаем страницу со списком."""
    page.goto(SPLUS, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)
    box = page.locator('input[type=text]:visible').first
    box.click()
    box.type(query, delay=12)
    page.wait_for_timeout(1500)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(9000)
