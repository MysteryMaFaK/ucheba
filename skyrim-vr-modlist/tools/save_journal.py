"""Достать результаты отдельных агентов воркфлоу из журнала и сохранить в data/partial/.
Запуск: python tools/save_journal.py <папка_транскрипта_воркфлоу> <кампания>
  кампания: install-spec | other-mods | core-additions | hitech
Папка транскрипта печатается инструментом Workflow ("Transcript dir: ...")."""
import json, os, sys
tdir, tag = sys.argv[1], sys.argv[2]
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
    json.dump(res, open(os.path.join(out, f'{tag}__{lab}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n += 1
    print('сохранено', f'{tag}__{lab}.json')
print(n, 'результатов')
