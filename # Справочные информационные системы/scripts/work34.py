# -*- coding: utf-8 -*-
"""Папки документов «задание 1»…«задание 8» для 3.3 и чистка лишнего документа в папке 3.2."""
from work32 import *

PLAN33 = [
    (1, 'социальный налоговый вычет на лечение лекарства без рецепта врача', 0),
    (2, 'признаки платежеспособности банкнот и монеты Банка России', 3),
    (4, 'социальный вычет на обучение за границей дистанционное обучение', 1),
    (5, 'дни приезда и отъезда 183 дня налоговый резидент НДФЛ', 1),
    (6, 'НДС при получении задатка налоговая база', 0),
    (7, 'НДС передача подарков работникам безвозмездная передача', 1),
    (8, 'статья 346.12 налогоплательщики упрощенная система налогообложения', 1),
]


def make_folders(page):
    for i in range(1, 9):
        name = 'задание %d' % i
        # перезагрузка снимает выделение предыдущей папки — иначе новая ляжет внутрь неё
        page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        favorites_section(page, 'Папки')
        page.wait_for_timeout(4000)
        page.get_by_text('Создать папку', exact=True).first.click()
        page.wait_for_timeout(2500)
        inp = page.locator('input[type=text]:visible').last
        inp.click(); page.keyboard.press('Control+a'); page.keyboard.type(name, delay=35)
        page.keyboard.press('Enter'); page.wait_for_timeout(3500)
        print('папка:', name, flush=True)
    folders_page(page); collapse(page)
    shot(page, S33, '33_docfolders')
    print('ПАПКИ:', txt(page, 700), flush=True)


def fill_folders(page):
    for n, q, idx in PLAN33:
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        if len(ls) <= idx:
            print('!! задание %d: подходящего документа в комплекте нет' % n, flush=True)
            continue
        print('задание %d <- %s' % (n, ls[idx]['t'][:95]), flush=True)
        open_doc(page, ls[idx]['h'])
        try:
            to_folder(page, 'задание %d' % n)
        except Exception as e:
            print('   не положилось:', str(e)[:110], flush=True)
    folders_page(page); collapse(page)
    shot(page, S33, '33_docfolders_filled')
    print('ИТОГ:', txt(page, 800), flush=True)


with sync_playwright() as pw:
    ctx = pw.chromium.launch_persistent_context(
        PROFILE, channel='msedge', headless=True,
        viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.set_default_timeout(60000)
    page.goto(BASE + '/cgi/online.cgi?req=home', wait_until='domcontentloaded')
    page.wait_for_timeout(7000)
    t = page.evaluate("document.body?document.body.innerText:''")
    if 'Избранное' not in t:
        print('СЕССИЯ ИСТЕКЛА — нужен вход')
    else:
        make_folders(page)
        fill_folders(page)
    ctx.close()
