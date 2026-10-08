#!/usr/bin/env bash
# Фоновая запись результатов воркфлоу в репозиторий.
# Использование: tools/autosave.sh <кампания>=<папка_транскрипта> [...]   (останов: touch /tmp/autosave.stop)
cd "$(dirname "$0")/.." || exit 1
REPO=$(git rev-parse --show-toplevel)
while [ ! -e /tmp/autosave.stop ]; do
  for kv in "$@"; do
    python3 tools/save_journal.py "${kv#*=}" "${kv%%=*}" >/dev/null 2>&1
  done
  if [ -n "$(git -C "$REPO" status --porcelain skyrim-vr-modlist/data/partial)" ]; then
    git -C "$REPO" add skyrim-vr-modlist/data/partial
    git -C "$REPO" commit -q -m "Skyrim VR: промежуточные результаты агентов (автосохранение)

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01JDE8W73UhW9EDSYa84ACYx" && for d in 0 2 4; do sleep $d; git -C "$REPO" push -q 2>/dev/null && break; done
    echo "$(date +%T) сохранено: $(ls skyrim-vr-modlist/data/partial | wc -l) файлов"
  fi
  sleep 60
done
