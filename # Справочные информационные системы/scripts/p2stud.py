# -*- coding: utf-8 -*-
"""3.2 п.2 в авторизованной версии: подборка Минфина 2015-2016 и печать списка названий."""
from work32 import *
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

    # --- Принявший орган: выбор из словаря закрывает диалог сам ---
    open_field(page, 'Принявший орган')
    page.evaluate("""()=>{const i=document.querySelector('.x-search-box__input');
        i.focus(); i.value='Минфин'; i.dispatchEvent(new Event('input',{bubbles:true}));}""")
    page.wait_for_timeout(4000)
    dom_click(page, 'Минфин России')
    page.wait_for_timeout(3000)
    shot(page, S32, '32_p2_organ_stud')

    # --- Дата: диапазон 01.01.2015 … 31.12.2016 ---
    open_field(page, 'Дата')
    dom_click(page, 'Диапазон дат:')
    page.wait_for_timeout(1200)
    ins = page.locator('input.x-date__input:visible')
    n = ins.count()
    ins.nth(n - 2).click(); page.keyboard.press('Home'); page.keyboard.type('01012015', delay=110)
    page.wait_for_timeout(500)
    dom_click(page, 'Поиск по полю «Дата»')       # закрыть всплывший календарь
    page.wait_for_timeout(700)
    ins.nth(n - 1).click(); page.keyboard.press('Home'); page.keyboard.type('31122016', delay=110)
    page.wait_for_timeout(500)
    dom_click(page, 'Поиск по полю «Дата»')
    page.wait_for_timeout(900)
    shot(page, S32, '32_p2_date_stud')
    print('ПРИМЕНИТЬ ДАТУ:', dom_click(page, 'Применить'), flush=True)
    page.wait_for_timeout(5000)

    # --- Текст документа ---
    open_field(page, 'Текст документа')
    print('ДИАЛОГ ТЕКСТА:', page.evaluate("""()=>[...document.querySelectorAll('*')]
        .filter(e=>e.offsetParent&&e.children.length===0&&e.textContent.trim().length>1
                && e.textContent.trim().length<40)
        .map(e=>e.textContent.trim()).slice(-18)"""), flush=True)
    ph = page.evaluate("""()=>[...document.querySelectorAll('input,textarea')]
        .filter(e=>e.offsetParent).map(e=>({ph:e.placeholder||'', cls:(e.className||'').slice(0,45)}))""")
    print('ИНПУТЫ ТЕКСТА:', ph, flush=True)
    page.evaluate("""()=>{const t=document.querySelector('input[placeholder*="Слова для поиска"]');
        t.focus(); t.value='БУХГАЛТЕРСКАЯ ОТЧЕТНОСТЬ';
        t.dispatchEvent(new Event('input',{bubbles:true}));}""")
    page.wait_for_timeout(1500)
    print('НАЙТИ ТЕКСТ:', dom_click(page, 'Найти'), flush=True)
    page.wait_for_timeout(6000)
    shot(page, S32, '32_p2_card_stud')
    print('КАРТОЧКА:', txt(page, 400), flush=True)

    # --- список ---
    dom_click(page, 'Показать список документов')
    page.wait_for_timeout(9000)
    shot(page, S32, '32_p2_list_stud')
    print('СПИСОК:', txt(page, 700), flush=True)

    # отметить весь список и распечатать
    page.mouse.click(1000, 700); page.wait_for_timeout(800)
    page.keyboard.press('NumpadAdd'); page.wait_for_timeout(2500)
    shot(page, S32, '32_p2_marked_stud')
    page.evaluate("""()=>{const b=document.querySelector('.icon.print-16');
        if(b) b.closest('a,button,div').click();}""")
    page.wait_for_timeout(6000)
    shot(page, S32, '32_p2_print_stud')
    print('ПЕЧАТЬ:', txt(page, 600), flush=True)
    ctx.close()
