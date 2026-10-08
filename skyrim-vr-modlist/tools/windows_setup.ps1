<#
  Клонирует репозиторий (только папку skyrim-vr-modlist) на этот компьютер и скачивает отчёты сборок.

  Запуск:        powershell -ExecutionPolicy Bypass -File windows_setup.ps1
  Другая папка:  powershell -ExecutionPolicy Bypass -File windows_setup.ps1 -Target D:\Modding

  Репозиторий приватный: при первом запуске Git попросит войти в GitHub (откроется браузер).
  Повторный запуск обновляет уже скачанное (git pull).
#>
param(
  [string]$Target = 'E:\Modding',
  [string]$Repo   = 'https://github.com/MysteryMaFaK/ucheba.git',
  [string]$Branch = 'claude/wizardly-brahmagupta-qj2sb4'
)
$ErrorActionPreference = 'Stop'

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw 'Не найден git. Установите Git for Windows: https://git-scm.com/download/win'
}

New-Item -ItemType Directory -Force -Path $Target | Out-Null
$dst = Join-Path $Target 'ucheba'

if (-not (Test-Path (Join-Path $dst '.git'))) {
  # sparse-checkout: из репозитория берём только папку проекта, учебные отчёты не скачиваются
  git clone --filter=blob:none --no-checkout --branch $Branch $Repo $dst
  git -C $dst sparse-checkout set --no-cone '/skyrim-vr-modlist/'
  git -C $dst checkout $Branch
} else {
  git -C $dst fetch origin $Branch
  git -C $dst checkout $Branch
  git -C $dst pull --ff-only origin $Branch
}

$proj = Join-Path $dst 'skyrim-vr-modlist'
Write-Host ''
Write-Host "Готово: $proj"

if (Get-Command python -ErrorAction SilentlyContinue) {
  Write-Host 'Скачиваю отчёты сборок Wabbajack (около 42 МБ)...'
  python (Join-Path $proj 'tools\fetch_reports.py')
} else {
  Write-Host 'Python не найден: отчёты сборок не скачаны (нужны только для tools\whouses.py и воркфлоу).'
}

Write-Host ''
Write-Host 'Дальше: откройте папку проекта в Claude Code (вкладка Code) и вставьте промпт из NEW_CHAT_PROMPT.md.'
