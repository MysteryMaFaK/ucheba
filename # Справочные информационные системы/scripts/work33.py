# -*- coding: utf-8 -*-
"""Второй сеанс в авторизованной версии: печать списка (3.2 п.2) и папки документов для 3.3."""
import os
from work32 import (PROFILE, BASE, S32, S33, EXPAND, shot, quick_search, doc_links,
                    open_doc, open_fav_dialog, to_folder, folders_page, collapse,
                    open_folder, txt, sync_playwright, time)

CARD = BASE + '/cgi/online.cgi?req=card&div=LAW'

# документы, найденные в задании 3.3 (запрос, номер строки в выдаче)
PLAN33 = [
    (1, 'социальный налоговый вычет на лечение лекарства без рецепта врача', 0),
    (2, 'признаки платежеспособности банкнот и монеты Банка России', 3),
    (4, 'социальный вычет на обучение за границей дистанционное обучение', 1),
    (5, 'дни приезда и отъезда 183 дня налоговый резидент НДФЛ', 1),
    (6, 'НДС при получении задатка налоговая база', 0),
    (7, 'НДС передача подарков работникам безвозмездная передача', 1),
    (8, 'статья 346.12 налогоплательщики упрощенная система налогообложения', 1),
]


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


def print_list_p2(page):
    """3.2 п.2: та же подборка в авторизованной версии + печать списка названий."""
    page.goto(CARD, wait_until='domcontentloaded'); page.wait_for_timeout(8000)

    open_field(page, 'Принявший орган')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('Минфин', delay=20)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(4500)
    page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim()==='Минфин России');
        if(e.length) e[e.length-1].click();}""")
    page.wait_for_timeout(2500)
    try:
        page.get_by_text('Применить', exact=True).first.click(timeout=6000)
        page.wait_for_timeout(5000)
    except Exception:
        pass

    open_field(page, 'Дата')
    page.wait_for_timeout(1500)
    page.get_by_text('Диапазон дат:', exact=True).first.click(); page.wait_for_timeout(1000)
    ins = page.locator('input[type=text]:visible'); n = ins.count()
    ins.nth(n - 2).click(); page.keyboard.press('Home'); page.keyboard.type('01012015', delay=110)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(700)
    ins.nth(n - 1).click(); page.keyboard.press('Home'); page.keyboard.type('31122016', delay=110)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(900)
    page.get_by_text('Применить', exact=True).first.click(); page.wait_for_timeout(6000)

    open_field(page, 'Текст документа')
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('БУХГАЛТЕРСКАЯ ОТЧЕТНОСТЬ', delay=18)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(6000)
    shot(page, S32, '32_p2_card_stud')

    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(9000)
    shot(page, S32, '32_p2_list_stud')
    print('СПИСОК (Студент):', txt(page, 700), flush=True)

    # отметить весь список и вызвать печать (окно печати браузера подавлено заглушкой window.print)
    page.mouse.click(1000, 700); page.wait_for_timeout(800)
    page.keyboard.press('NumpadAdd'); page.wait_for_timeout(2500)
    shot(page, S32, '32_p2_marked_stud')
    page.evaluate("document.querySelector('.icon.print-16').closest('a,button,div').click()")
    page.wait_for_timeout(6000)
    shot(page, S32, '32_p2_print_stud')
    print('ПЕЧАТЬ:', txt(page, 600), flush=True)
    page.keyboard.press('Escape'); page.wait_for_timeout(1500)

    # выгрузка списка названий в Word
    try:
        with page.expect_download(timeout=30000) as di:
            page.evaluate("document.querySelector('.icon.word-16').closest('a,button,div').click()")
        d = di.value
        p = os.path.join(S32, 'spisok_minfin_stud.docx'); d.save_as(p)
        print('ФАЙЛ СПИСКА:', p, flush=True)
    except Exception as e:
        print('выгрузка не вышла:', str(e)[:140], flush=True)


def make_folders33(page):
    for i in range(1, 9):
        name = 'задание %d' % i
        # перезагрузка снимает выделение предыдущей папки — иначе новая ляжет внутрь неё
        page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        page.mouse.click(32, 203)
        page.wait_for_timeout(4000)
        page.get_by_text('Создать папку', exact=True).first.click()
        page.wait_for_timeout(2500)
        inp = page.locator('input[type=text]:visible').last
        inp.click(); page.keyboard.press('Control+a'); page.keyboard.type(name, delay=35)
        page.keyboard.press('Enter'); page.wait_for_timeout(3500)
        print('папка создана:', name, flush=True)
    folders_page(page); collapse(page)
    shot(page, S33, '33_docfolders')
    print('ПАПКИ:', txt(page, 600), flush=True)


def fill_folders33(page):
    for n, q, idx in PLAN33:
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        if len(ls) <= idx:
            print('!! задание %d: в комплекте нет подходящего документа' % n, flush=True)
            continue
        print('задание %d <- %s' % (n, ls[idx]['t'][:95]), flush=True)
        open_doc(page, ls[idx]['h'])
        try:
            to_folder(page, 'задание %d' % n)
        except Exception as e:
            print('   не удалось положить:', str(e)[:110], flush=True)
    folders_page(page); collapse(page)
    shot(page, S33, '33_docfolders_filled')
    print('ИТОГ:', txt(page, 700), flush=True)


def drop_stray(page):
    """Из папки «Дистанционная торговля» убрать приказ Росстата — попал туда по ошибке."""
    folders_page(page)
    open_folder(page, 'Дистанционная торговля')
    page.evaluate("""()=>{const a=[...document.querySelectorAll('a[href*="req=doc"]')]
        .find(e=>/Росстат/.test(e.innerText||''));
        if(a) a.click();}""")
    page.wait_for_timeout(2500)
    page.keyboard.press('Shift+Delete')          # в меню папки указано как горячая клавиша
    page.wait_for_timeout(3000)
    shot(page, S32, '32_p4_dropmenu')
    for label in ('Удалить', 'Да', 'ОК'):
        try:
            page.get_by_text(label, exact=True).last.click(timeout=4000)
            page.wait_for_timeout(3000)
            print('подтверждено:', label, flush=True)
            break
        except Exception:
            pass
    folders_page(page)
    open_folder(page, 'Дистанционная торговля')
    collapse(page)
    shot(page, S32, '32_p4_folder')
    print('ПАПКА ПОСЛЕ:', txt(page, 600), flush=True)


def main(page):
    drop_stray(page)
    print_list_p2(page)
    make_folders33(page)
    fill_folders33(page)


with sync_playwright() as pw:
    ctx = pw.chromium.launch_persistent_context(
        PROFILE, channel='msedge', headless=False,
        viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU',
        args=['--window-size=1320,900'])
    # печать списка не должна открывать системный диалог — он рвёт сеанс автоматизации
    ctx.add_init_script("window.print = () => { window.__printed = true; };")
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.set_default_timeout(60000)
    page.goto(BASE + '/', wait_until='domcontentloaded')
    print('ОКНО ОТКРЫТО — войдите в систему, если попросит.', flush=True)

    deadline = time.time() + 900
    ok = False
    while time.time() < deadline:
        try:
            t = page.evaluate("document.body ? document.body.innerText : ''")
            if 'Избранное' in t and 'Журнал' in t:
                ok = True
                break
        except Exception:
            pass
        time.sleep(3)

    if not ok:
        print('НЕ ДОЖДАЛСЯ ВХОДА', flush=True)
    else:
        print('АВТОРИЗОВАН, работаю', flush=True)
        try:
            main(page)
        except Exception as e:
            print('ОШИБКА:', str(e)[:300], flush=True)
    page.wait_for_timeout(2000)
    ctx.close()
print('ГОТОВО')
