# -*- coding: utf-8 -*-
"""Все действия в авторизованной версии: выполняются сразу после входа, в том же окне.

Сессия «КонсультантПлюс: Студент» живёт недолго, поэтому отдельные headless-запуски
каждый раз упираются в форму логина.
"""
import os, sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE = os.path.join(HERE, 'kpprofile')
BASE = 'https://student2.consultant.ru'
S32 = os.path.join(HERE, 's32'); os.makedirs(S32, exist_ok=True)
S33 = os.path.join(HERE, 's33'); os.makedirs(S33, exist_ok=True)

EXPAND = """(n)=>{
  const i=[...document.querySelectorAll("input[type=text]")]
    .find(e=>e.offsetParent && /поиск/i.test(e.placeholder||""));
  if(!i) return "no input";
  i.focus(); i.value=n; i.dispatchEvent(new Event("input",{bubbles:true}));
  let p=i.parentElement, btn=null;
  for(let k=0;k<4&&p;k++){
    btn=[...p.querySelectorAll("*")].find(e=>e.children.length===0&&e.textContent.trim()==="Найти");
    if(btn) break; p=p.parentElement;
  }
  if(!btn) return "no btn";
  btn.click(); return "ok";
}"""


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
    page.wait_for_timeout(9000)


def open_fav_dialog(page):
    page.evaluate("[...document.querySelectorAll('[title=\"Еще\"]')][0].click()")
    page.wait_for_timeout(2000)
    page.get_by_text('Добавить в Избранное…', exact=True).first.click()
    page.wait_for_timeout(4000)


def to_folder(page, folder):
    open_fav_dialog(page)
    page.wait_for_timeout(2000)
    page.get_by_text('Папки', exact=True).last.click()
    page.wait_for_timeout(3000)
    page.evaluate(EXPAND, folder)
    page.wait_for_timeout(3000)
    page.evaluate("""(n)=>{const els=[...document.querySelectorAll('*')]
        .filter(e=>e.children.length===0 && e.textContent.trim()===n);
        if(els.length) els[els.length-1].click();}""", folder)
    page.wait_for_timeout(1500)
    page.evaluate("""()=>{const b=[...document.querySelectorAll('*')]
        .filter(e=>e.children.length===0 && e.textContent.trim()==='Добавить');
        if(b[0]) b[0].click();}""")
    page.wait_for_timeout(4000)


def folders_page(page):
    favorites_section(page, 'Папки')


def collapse(page):
    page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim()==='Свернуть');
        if(e.length) e[e.length-1].click();}""")
    page.wait_for_timeout(1200)


def open_folder(page, name):
    el = page.locator('.x-components-favorites-folder-text', has_text=name).first
    el.dblclick()
    page.wait_for_timeout(5000)


def txt(page, n=500):
    return page.evaluate("document.body?document.body.innerText:''")[:n].replace('\n', ' | ')


# ==================== работа ====================
def main(page):
    # --- 3.2 п.4: ФЗ-29 о качестве пищевых продуктов в папку «Дистанционная торговля» ---
    quick_search(page, 'Федеральный закон 29-ФЗ о качестве и безопасности пищевых продуктов')
    ls = doc_links(page, 4)
    for l in ls[:4]:
        print('КАНДИДАТ 29-ФЗ:', l['t'][:110], flush=True)
    pick = next((l for l in ls if '29-ФЗ' in l['t'] or 'качестве и безопасности' in l['t']), None)
    if pick:
        print('-> в папку:', pick['t'][:90], flush=True)
        open_doc(page, pick['h'])
        shot(page, S32, '32_p4_fz29_stud')
        to_folder(page, 'Дистанционная торговля')

    # --- 3.2 п.8: документ ФНС о счетах-фактурах на контроль ---
    quick_search(page, 'письмо ФНС России о порядке заполнения счетов-фактур')
    ls = doc_links(page, 5)
    for l in ls[:5]:
        print('КАНДИДАТ ФНС:', l['t'][:110], flush=True)
    fns = next((l for l in ls if 'ФНС' in l['t']), None)
    if fns:
        open_doc(page, fns['h'])
        shot(page, S32, '32_p8_fns_doc')
        page.evaluate("[...document.querySelectorAll('[title=\"Еще\"]')][0].click()")
        page.wait_for_timeout(2500)
        shot(page, S32, '32_p8_fns_menu')
        try:
            page.get_by_text('Поставить на контроль', exact=True).first.click()
            page.wait_for_timeout(5000)
            shot(page, S32, '32_p8_fns_after')
            print('КОНТРОЛЬ ФНС:', txt(page, 300), flush=True)
        except Exception as e:
            print('контроль не вышел:', str(e)[:120], flush=True)

    # --- скриншоты папок и контроля ---
    for name, sn in [('Дистанционная торговля', '32_p4_folder'),
                     ('Уставный капитал АО', '32_p6_ao'),
                     ('Уставный капитал ООО', '32_p6_ooo')]:
        folders_page(page)
        try:
            open_folder(page, name)
            collapse(page)
            shot(page, S32, sn)
            print(name, '->', txt(page, 420), flush=True)
        except Exception as e:
            print('папка не открылась:', name, str(e)[:100], flush=True)

    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    favorites_section(page, 'Документы на контроле')          # «Документы на контроле»
    page.wait_for_timeout(5000)
    collapse(page)
    shot(page, S32, '32_p8_list')
    print('КОНТРОЛЬ:', txt(page, 500), flush=True)


def run(job):
    with sync_playwright() as pw:
      ctx = pw.chromium.launch_persistent_context(
          PROFILE, channel='msedge', headless=False,
          viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU',
          args=['--window-size=1320,900'])
      page = ctx.pages[0] if ctx.pages else ctx.new_page()
      page.set_default_timeout(60000)
      page.goto(BASE + '/', wait_until='domcontentloaded')
      print('ОКНО ОТКРЫТО — войдите в систему в этом окне.', flush=True)

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
              job(page)
          except Exception as e:
              print('ОШИБКА:', str(e)[:300], flush=True)
      page.wait_for_timeout(2000)
      ctx.close()
    print('ГОТОВО')


if __name__ == '__main__':
    run(main)
