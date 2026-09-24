# -*- coding: utf-8 -*-
"""Печать списка названий: проверяем, вызывает ли система window.print, и снимаем печатную форму."""
from work32 import *
import os
CARD = BASE + '/cgi/online.cgi?req=card&div=LAW'


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(4000)


def dom_click(page, label):
    return page.evaluate("""(n)=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim()===n && x.offsetParent);
        if(!e.length) return 'нет: '+n;
        e[e.length-1].click(); return 'ok';}""", label)


with sync_playwright() as pw:
    ctx = pw.chromium.launch_persistent_context(
        PROFILE, channel='msedge', headless=True,
        viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    ctx.add_init_script("window.print = () => { window.__printed = true; };")
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.set_default_timeout(45000)
    page.goto(CARD, wait_until='domcontentloaded'); page.wait_for_timeout(9000)

    open_field(page, 'Принявший орган')
    page.evaluate("""()=>{const i=document.querySelector('.x-search-box__input');
        i.focus(); i.value='Минфин'; i.dispatchEvent(new Event('input',{bubbles:true}));}""")
    page.wait_for_timeout(4000)
    dom_click(page, 'Минфин России'); page.wait_for_timeout(3000)

    open_field(page, 'Дата')
    dom_click(page, 'Диапазон дат:'); page.wait_for_timeout(1200)
    ins = page.locator('input.x-date__input:visible'); n = ins.count()
    ins.nth(n - 2).click(); page.keyboard.press('Home'); page.keyboard.type('01012015', delay=110)
    dom_click(page, 'Поиск по полю «Дата»'); page.wait_for_timeout(700)
    ins.nth(n - 1).click(); page.keyboard.press('Home'); page.keyboard.type('31122016', delay=110)
    dom_click(page, 'Поиск по полю «Дата»'); page.wait_for_timeout(900)
    dom_click(page, 'Применить'); page.wait_for_timeout(5000)

    open_field(page, 'Текст документа')
    page.evaluate("""()=>{const t=document.querySelector('input[placeholder*="Слова для поиска"]');
        t.focus(); t.value='БУХГАЛТЕРСКАЯ ОТЧЕТНОСТЬ';
        t.dispatchEvent(new Event('input',{bubbles:true}));}""")
    page.wait_for_timeout(1500)
    dom_click(page, 'Найти'); page.wait_for_timeout(6000)
    dom_click(page, 'Показать список документов'); page.wait_for_timeout(9000)

    # меню «…» на панели списка — ищем команду печати/сохранения списка
    page.evaluate("document.querySelector('.icon.dots-16').closest('a,button,div').click()")
    page.wait_for_timeout(2500)
    shot(page, S32, '32_p2_menu_stud')
    print('МЕНЮ:', page.evaluate("""()=>[...document.querySelectorAll('*')]
        .filter(e=>e.offsetParent&&e.children.length===0&&e.textContent.trim().length>2
                && e.textContent.trim().length<45)
        .map(e=>e.textContent.trim()).slice(-14)"""), flush=True)
    page.keyboard.press('Escape'); page.wait_for_timeout(1500)

    page.evaluate("document.querySelector('.icon.print-16').closest('a,button,div').click()")
    page.wait_for_timeout(5000)
    print('window.print вызван:', page.evaluate("!!window.__printed"), flush=True)
    shot(page, S32, '32_p2_printdlg_stud')
    print('ЭКРАН:', txt(page, 400), flush=True)

    pdf = os.path.join(S32, 'spisok_minfin_stud.pdf')
    try:
        page.pdf(path=pdf, format='A4', print_background=True)
        print('PDF СПИСКА:', pdf, os.path.getsize(pdf), flush=True)
    except Exception as e:
        print('pdf не вышел:', str(e)[:150], flush=True)
    ctx.close()
