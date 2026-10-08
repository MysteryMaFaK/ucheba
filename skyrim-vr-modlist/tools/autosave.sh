#!/usr/bin/env bash
# Фоновая запись результатов воркфлоу в data/partial/ (по желанию — с коммитом и пушем).
# Использование: tools/autosave.sh [--push] <кампания>=<папка_транскрипта> [...]
# Останов: создать файл .autosave.stop в папке проекта. Без --push только сохраняет файлы, git не трогает.
# Коммит и пуш делайте только если владелец разрешил. Ничего не перезаписывает (см. save_journal.py).
cd "$(dirname "$0")/.." || exit 1
PUSH=0; [ "$1" = "--push" ] && { PUSH=1; shift; }
rm -f .autosave.stop
while [ ! -e .autosave.stop ]; do
  for kv in "$@"; do
    python3 tools/save_journal.py "${kv#*=}" "${kv%%=*}" >/dev/null 2>&1
  done
  if [ "$PUSH" = 1 ] && [ -n "$(git status --porcelain data/partial)" ]; then
    git add data/partial && git commit -q -m "Skyrim VR: промежуточные результаты агентов (автосохранение)" && git push -q 2>/dev/null
  fi
  echo "$(date +%T) сохранено файлов: $(ls data/partial | wc -l)"
  sleep 60
done
