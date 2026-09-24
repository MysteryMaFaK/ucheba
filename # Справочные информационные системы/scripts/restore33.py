# -*- coding: utf-8 -*-
"""Восстановление папок закладок «задание 1»…«задание 8» и чистка дубликатов папок документов.

Переключение разделов Избранного делается только с проверкой заголовка: клик по координатам
иконок ненадёжен — панель бывает свёрнутой и развёрнутой, координаты разъезжаются.
"""
from work32 import *
S33D = os.path.join(HERE, 's33')
os.makedirs(S33D, exist_ok=True)

PLAN = [
    (1, 'социальный налоговый вычет на лечение без рецепта врача лекарства', 1),
    (2, 'признаки платежеспособности банкнот и монеты Банка России', 3),
    (4, 'социальный вычет на обучение за границей дистанционное обучение', 1),
    (5, 'дни приезда и отъезда 183 дня налоговый резидент НДФЛ', 1),
    (6, 'НДС при получении задатка налоговая база', 0),
    (7, 'НДС передача подарков работникам безвозмездная передача', 1),
    (8, 'статья 346.12 налогоплательщики упрощенная система налогообложения', 1),
]


def section_title(page):
    return page.evaluate("""()=>{const t=document.querySelector('.x-page-favorites-title-toolbar__title');
        return t?t.textContent.trim():'';}""")


def goto_section(page, name, tries=4):
    """Открыть раздел Избранного и убедиться по заголовку, что попали именно в него."""
    for _ in range(tries):
        page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        # развернуть панель, если она свёрнута до иконок
        page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
            .find(x=>x.children.length===0 && x.textContent.trim()==='Развернуть' && x.offsetParent);
            if(e) e.click();}""")
        page.wait_for_timeout(2000)
        page.evaluate("""(n)=>{const e=[...document.querySelectorAll('*')]
            .filter(x=>x.children.length===0 && x.textContent.trim()===n && x.offsetParent);
            if(e.length) e[0].click();}""", name)
        page.wait_for_timeout(4000)
        if section_title(page) == name:
            return True
        print('  не попал в раздел «%s» (заголовок: %s), повтор' % (name, section_title(page)), flush=True)
    return False


def make_folders(page):
    for i in range(1, 9):
        name = 'задание %d' % i
        if not goto_section(page, 'Закладки'):
            print('!! раздел «Закладки» не открылся', flush=True); return False
        page.get_by_text('Создать папку', exact=True).first.click()
        page.wait_for_timeout(2500)
        inp = page.locator('input[type=text]:visible').last
        inp.click(); page.keyboard.press('Control+a'); page.keyboard.type(name, delay=35)
        page.keyboard.press('Enter'); page.wait_for_timeout(3000)
        print('папка закладок:', name, flush=True)
    goto_section(page, 'Закладки')
    shot(page, S33D, '33_folders')
    print('ДЕРЕВО ЗАКЛАДОК:', txt(page, 700), flush=True)
    return True


def set_bookmarks(page):
    for n, q, idx in PLAN:
        name = 'задание %d' % n
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        if len(ls) <= idx:
            print('!! %s: документа нет' % name, flush=True); continue
        print('%s <- %s' % (name, ls[idx]['t'][:90]), flush=True)
        open_doc(page, ls[idx]['h'])
        try:
            open_fav_dialog(page)
            page.evaluate("""(n)=>{const tas=[...document.querySelectorAll('textarea')]
                .filter(e=>e.offsetParent);
                if(tas[0]){ tas[0].focus(); tas[0].value=n;
                            tas[0].dispatchEvent(new Event('input',{bubbles:true})); }}""", name)
            page.wait_for_timeout(1000)
            page.evaluate(EXPAND, name)
            page.wait_for_timeout(3000)
            page.evaluate("""(n)=>{const e=[...document.querySelectorAll('*')]
                .filter(x=>x.children.length===0 && x.textContent.trim()===n);
                if(e.length) e[e.length-1].click();}""", name)
            page.wait_for_timeout(1500)
            shot(page, S33D, '33_t%d_dialog' % n)
            page.evaluate("""()=>{const b=[...document.querySelectorAll('*')]
                .filter(e=>e.children.length===0 && e.textContent.trim()==='Добавить');
                if(b[0]) b[0].click();}""")
            page.wait_for_timeout(4000)
            print('   закладка поставлена', flush=True)
        except Exception as e:
            print('   ошибка:', str(e)[:120], flush=True)
    goto_section(page, 'Закладки')
    shot(page, S33D, '33_fav_tree')
    print('ЗАКЛАДКИ ИТОГ:', txt(page, 800), flush=True)


def drop_dup_folders(page):
    """В разделе «Папки» убрать дубликаты «задание N» от 22.09, оставив комплект от 23.09."""
    if not goto_section(page, 'Папки'):
        print('!! раздел «Папки» не открылся — дубликаты не трогаю', flush=True); return
    marked = page.evaluate("""()=>{
      const rs=[...document.querySelectorAll('tr,li,div')]
        .filter(r=>r.querySelector('input[type=checkbox]'));
      let n=0;
      for(const r of rs){
        const t=(r.innerText||'').replace(/\\s+/g,' ').trim();
        if(/^задание \\d \\(\\d+\\) 22\\.09\\.2026/.test(t) && t.length<45){
          const b=r.querySelector('input[type=checkbox]');
          if(b && !b.checked){ b.click(); n++; }
        }
      }
      return n;
    }""")
    print('дубликатов отмечено:', marked, flush=True)
    shot(page, S33D, 'dbg_dups_marked')
    if marked == 0 or marked > 8:
        print('НЕ УДАЛЯЮ — неожиданное количество', flush=True); return
    page.evaluate("""()=>{const t=[...document.querySelectorAll('*')]
        .find(e=>/trash|delete|basket|remove/i.test((e.className||'').toString()) && e.offsetParent);
        if(t) t.closest('a,button,div').click();}""")
    page.wait_for_timeout(3000)
    for label in ('Удалить', 'Да', 'ОК'):
        try:
            page.get_by_text(label, exact=True).last.click(timeout=4000)
            page.wait_for_timeout(3000)
            print('подтверждено:', label, flush=True)
            break
        except Exception:
            pass
    goto_section(page, 'Папки')
    shot(page, S33D, '33_docfolders_filled')
    print('ПАПКИ ИТОГ:', txt(page, 800), flush=True)


def job(page):
    if make_folders(page):
        set_bookmarks(page)
    drop_dup_folders(page)


if __name__ == '__main__':
    run(job)
