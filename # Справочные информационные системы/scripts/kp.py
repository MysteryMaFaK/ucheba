# -*- coding: utf-8 -*-
"""Общий каркас для скриншотов заданий 3.1 в некоммерческой онлайн-версии КонсультантПлюс."""
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots31')
os.makedirs(OUT, exist_ok=True)
CARD_LAW = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&div=LAW'
HOME = 'https://www.consultant.ru/cons/cgi/online.cgi?req=home'

CLEAN = """() => {
  document.querySelectorAll('div,section,aside').forEach(e=>{
    const t=(e.innerText||'');
    if(t.length<500 && /(Пробный доступ|cookie|куки)/i.test(t)) e.style.display='none';
  });
}"""


def shot(page, name):
    page.evaluate(CLEAN)
    page.screenshot(path=os.path.join(OUT, name + '.png'))
    print('  OK', name)


def browser(pw):
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page()
    page.set_default_timeout(45000)
    return br, page
