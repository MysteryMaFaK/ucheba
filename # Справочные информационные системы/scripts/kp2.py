# -*- coding: utf-8 -*-
"""Каркас работы в авторизованной интранет-версии КонсультантПлюс (student2.consultant.ru)."""
import os, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE = os.path.join(HERE, 'kpprofile')
BASE = 'https://student2.consultant.ru'
HOME = BASE + '/cgi/online.cgi?req=home'


def shots_dir(name):
    d = os.path.join(HERE, name)
    os.makedirs(d, exist_ok=True)
    return d


def open_ctx(pw, headless=True):
    ctx = pw.chromium.launch_persistent_context(
        PROFILE, channel='msedge', headless=headless,
        viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.set_default_timeout(60000)
    return ctx, page


FAV_TABS = {'Закладки': 0, 'Папки': 1, 'Документы на контроле': 2}


def favorites_section(page, name):
    """Раздел Избранного по кнопке боковой панели: координаты иконок зависят от того, свёрнута ли панель."""
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(7000)
    page.evaluate("""(i)=>{const b=document.querySelectorAll('.x-page-favorites-sidebar-button');
        if(b[i]) b[i].click();}""", FAV_TABS[name])
    page.wait_for_timeout(4000)
    title = page.evaluate("""()=>{const t=document.querySelector('.x-page-favorites-title-toolbar__title');
        return t ? t.textContent.trim() : '';}""")
    if title != name:
        raise RuntimeError('открылся раздел «%s» вместо «%s»' % (title, name))


def shot(page, folder, name):
    page.screenshot(path=os.path.join(folder, name + '.png'))
    print('  OK', name, flush=True)


def quick_search(page, query):
    """Быстрый поиск: вводим запрос и жмём кнопку «Найти»."""
    page.goto(BASE + '/cgi/online.cgi?req=card&page=splus', wait_until='domcontentloaded')
    page.wait_for_timeout(7000)
    page.evaluate("""(q) => {
      const i=[...document.querySelectorAll('input[type=text]')].find(x=>x.offsetParent);
      i.focus(); i.value=q; i.dispatchEvent(new Event('input',{bubbles:true}));
    }""", query)
    page.wait_for_timeout(1200)
    page.get_by_text('Найти', exact=True).first.click()
    page.wait_for_timeout(9000)


def doc_links(page, limit=8):
    return page.evaluate("""(n) => [...document.querySelectorAll('a[href*="req=doc"]')]
        .map(a=>({t:(a.innerText||'').replace(/\\s+/g,' ').trim(), h:a.getAttribute('href')}))
        .slice(0,n)""", limit)


def open_doc(page, href):
    page.goto(BASE + '/cgi/' + href.replace('../cgi/', ''), wait_until='domcontentloaded')
    page.wait_for_timeout(10000)


def doc_text(page):
    texts = []
    for fr in page.frames:
        try:
            texts.append(fr.evaluate("document.body ? document.body.innerText : ''"))
        except Exception:
            pass
    return max(texts, key=len) if texts else ''
