"""Достать результаты отдельных агентов воркфлоу из журнала и сохранить в data/partial/.
Запуск: python tools/save_journal.py <папка_транскрипта_воркфлоу> <кампания> [--overwrite]
  кампания: install-spec | other-mods | core-additions | hitech
Папка транскрипта печатается инструментом Workflow ("Transcript dir: ...").
Существующий файл с тем же именем НЕ перезаписывается молча: если содержимое отличается, скрипт предупреждает;
с --overwrite старая версия уходит в data/partial/_backup/, новая записывается."""
import json, os, shutil, sys
args = [a for a in sys.argv[1:] if not a.startswith('--')]
overwrite = '--overwrite' in sys.argv
tdir, tag = args[0], args[1]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'partial')
os.makedirs(out, exist_ok=True)
lines = [json.loads(l) for l in open(os.path.join(tdir, 'journal.jsonl'), encoding='utf-8')]
labels = {d['agentId']: d['label'] for d in lines if d.get('type') == 'started'}
n = 0
for d in lines:
    if d.get('type') != 'result':
        continue
    res = d['result']
    if isinstance(res, str):
        try: res = json.loads(res)
        except Exception: pass
    lab = labels.get(d['agentId'], d['agentId']).replace(':', '_').replace('/', '_')
    path = os.path.join(out, f'{tag}__{lab}.json')
    text = json.dumps(res, ensure_ascii=False, indent=1)
    if os.path.exists(path):
        if open(path, encoding='utf-8').read() == text:
            continue  # то же содержимое
        if not overwrite:
            print('ПРОПУЩЕНО (файл есть и отличается; --overwrite заменит, старый уйдёт в _backup):', os.path.basename(path))
            continue
        os.makedirs(os.path.join(out, '_backup'), exist_ok=True)
        shutil.copy2(path, os.path.join(out, '_backup', os.path.basename(path)))
    open(path, 'w', encoding='utf-8').write(text)
    n += 1
    print('сохранено', os.path.basename(path))
print(n, 'результатов записано')
