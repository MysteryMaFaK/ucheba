# Руководство по установке Skyrim VR Core 2026

Фазы, инструменты, пути и проверки. Читается вместе с `manifest.yaml` (что ставить) и `CONFLICTS.md` (порядок и запреты).

**Что здесь проверено, а что нет.** Пометка ⚠ означает: взято из общих знаний о Skyrim VR и MO2, а не из страницы мода или исходников. Агент сверяет такие места с актуальной страницей мода на Nexus (на вашем компьютере она открывается) и записывает расхождения в `install_log.md`. Список таких мест — в конце файла.

## 0. Подготовка компьютера

Из вики сборки FUS (проверено по репозиторию Kvitekvist/FUS):

1. Установите Microsoft Visual C++ Redistributable (x64, 2015–2022) и .NET 8 Runtime (desktop и console, x64).
2. Skyrim VR ставьте в **новую библиотеку Steam** (например `D:\SteamLibrary`), не в Program Files и не на рабочий стол. Язык игры в Steam — **English** (для английской сборки; для русской см. раздел «Русский язык»).
3. Запустите игру один раз до главного меню и выйдите: так инструменты найдут папку игры.
4. SteamVR: разрешение рендера **100% и глобально, и для игры**. Суперсэмплинг поверх апскейла Open Shaders только съедает кадры.
5. Отключите оверлеи (Discord и другие) и игровой режим Windows: они конфликтуют с SKSEVR. Оверлей Steam можно отключить, но тогда не будет достижений через Engine Fixes.
6. Видеопамять: 2K-текстуры по умолчанию, 4K только для близких предметов.

## 1. Инструменты и корень игры (фаза 1)

| Что | Куда | Заметки |
|---|---|---|
| Mod Organizer 2 2.5.2, портативный инстанс | `MO2_DIR`, например `D:\Modding\SkyrimVR-MO2` | Игра — Skyrim VR, профиль `Core 2026`, **локальные INI и сохранения** включены |
| Root Builder (Kezyma, #31720) | плагин MO2 | Файлы для корня игры кладутся в подпапку `Root` внутри мода, плагин переносит их в `GAME_DIR` при запуске и убирает при выходе ⚠ режим копирования/ссылок выбрать в его настройках |
| SSEEdit (#164) | отдельная папка вне Steam и MO2 | Как исполняемый файл MO2; для VR — запуск с аргументом `-tes5vr` или переименование `TES5VREdit.exe` ⚠ |
| LOOT | отдельно | Skyrim VR поддерживается |
| BethINI Pie + плагин для Skyrim VR | отдельно | INI под VR |
| Pandora Behaviour Engine+ | отдельная папка, исполняемый файл MO2, вывод в отдельный мод | VR-поддержка возвращена в 4.1.2-beta ⚠ проверить текущий релиз |
| Synthesis | отдельная папка, вывод в отдельный мод | Только в конце, после всех модов |
| fpsVR или SteamVR Frame Timing | — | Время кадра CPU и GPU, а не загрузка видеокарты |

Папка `Skyrim VR` в `Documents\My Games` и INI: игра читает `SkyrimVR.ini`, `SkyrimPrefs.ini` из профиля MO2, если включены локальные INI.

### Мастера игры и USSEP

Выбор — `MASTERS_PATH` из `SYSTEM_PROMPT.md`.

- **Путь A (есть Skyrim SE/AE).** Следуйте гайду infernalryan «Skyrim Initial Setup (VR)» (обновлён 23.07.2026) и «Updating Game Masters»: обновлённые мастера SSE 1.6.1170 и бесплатные CC переносятся в отдельный мод MO2. Затем ставятся свежий USSEP, «Skyrim VR Strings Fix for Updated SSE Master Files» (проверьте поддержку вашего языка), «Survival Mode Prompt Removed» (Disable Permanently), «Survival Text Removed»; при белых деревьях — «Skyrim VR Fixes for Latest USSEP».
- **Путь B (SE/AE нет).** USSEP **4.2.5b** (из старых файлов страницы #266) и «Skyrim Vr USSEP patch for USSEP 4.2.5b» (#91475). Моды, которым нужен свежий USSEP или записи SE 1.6, на этом пути не ставятся.

Чистка мастеров в SSEEdit: Quick Auto Clean для Update, Dawnguard, HearthFires, Dragonborn. Свежий USSEP **не чистить** — он поставляется чистым.

## 2. SKSEVR, библиотеки, фиксы (фаза 2)

1. **SKSEVR 2.0.12** — загрузчик (`sksevr_loader.exe`) и DLL (`sksevr_1_4_15.dll`, `sksevr_steam_loader.dll`) идут в **Root**, скрипты — обычный мод. Запускать игру только через загрузчик SKSEVR из MO2.
2. **VR Address Library for SKSEVR** — обновлять вместе с каждым SKSE-плагином; новые версии плагинов требуют новые адреса.
3. **Engine Fixes VR** — Part 1 как мод, **Part 2 — в Root**. В настройках включить `MaxStdio = 8192`: это требование Skyrim VR ESL Support ⚠ имя файла настроек и ключ сверить со страницей Engine Fixes VR. Старый отдельный ObjectLOD/Shadow Map fix не ставить — он внутри с 7.4.9.
4. **Skyrim VR ESL Support** — только с официальным SKSEVR 2.0.12; ставится до генерации DynDOLOD.
5. **Crash Logger SSE AE VR** (+ PDB) — логи вылетов.
6. Образец «основной мод + VR-DLL поверх»: powerofthree's Papyrus Extender → Papyrus Extender VR; po3 Tweaks → po3 Tweaks VR; Container Distribution Framework → CDF VR; Light Placer → Light Placer VR. Сначала основной, VR-файлы ставятся поверх и перезаписывают.

Контрольный запуск: `sksevr.log` ⚠ (обычно `Documents\My Games\Skyrim VR\SKSE\sksevr.log`) — каждая DLL должна быть загружена без ошибок. Вылеты — `crash-*.log` Crash Logger в той же папке.

## 3. Шейдеры, свет, VR-ядро (фаза 3)

- **Open Shaders** (или CSX — выбор `SHADERS`) — ставится как обычный мод, **вместо** Community Shaders. Не ставить оба. Нужны Engine Fixes VR и VR Address Library. Настройки: DLAA при запасе GPU, иначе DLSS Quality/Balanced; фовеальный рендеринг включить; генерацию кадров в VR не использовать. Включайте тяжёлые функции по одной с замером: Wetness, SSGI/AO, Screen Space Shadows, Terrain Blending.
- VRIK, HIGGS, PLANCK и надстройки 2026 года ставятся цепочкой зависимостей из манифеста: сначала VRIK, HIGGS, PLANCK, затем Physical Collision VR, True Wield VR, Immersive Weapon Penetration VR.
- Старый Pseudo Physical Weapon Collision не ставить вместе с Physical Collision VR.

## 4. Интерфейс и звук (фаза 4)

SkyUI VR, MCM Helper, затем остальное из манифеста. Для звуковых модов нужен Sound Record Distributor. Группа `audio-stack`: один из вариантов (см. `CONFLICTS.md`).

## 5. Свет, погода, вода, ландшафт (фаза 5)

- **Lux** — в установщике **без** разделённых мешей (split meshes). Меши с префиксом `Lux_` не удалять.
- **CS Light** — не включать одновременно «ENB lights for effect shaders» и «Magic FX lights». При Embers XD включить опцию под него.
- Azurite Weathers III + MCM + HDR; Volumetric Mists не ставить.
- Одна вода: `water`. Одна трава: `grass`. Прекэш травы NGIO — в конце (раздел «Финальная генерация»).

## 6. Анимации (фаза 6)

OAR-пакеты NPC; XPMSSE + **VR-фикс скелета первого лица** (грузится после XPMSSE). Только **один** генератор поведений — Pandora; Nemesis не ставить. Запуск Pandora из MO2 после всех анимационных модов, вывод в отдельный мод, расположенный ниже всех модов-источников.

## 7–9. Геймплей, хайтек, ИИ-NPC

- Бой и геймплей: SimonRim (Adamant, Mysticism, Thaumaturgy, Apothecary, Mundus) вместе с Poached Bugs VR (файл Simonrim Choice Config).
- Хайтек-новинки 2026: ставить **по одному**, после каждого — запуск и проверка `sksevr.log` по полю `verify`. Метка `try` — только с разрешения пользователя.
- ИИ-NPC: один из SkyrimNet, Mantella, CHIM (группа `ai-npc`). Для SkyrimNet в VR нужны Skyrim VR ESL Support, Skyrim VR Refocused, MFG Fix NG и po3 Tweaks (SE и VR).

## 10. Финальная генерация (после текстур)

Строго по порядку; каждый шаг читает результат предыдущего, вывод — в отдельный мод внизу списка:

1. Все моды и текстуры установлены; LOOT; конфликты в xEdit.
2. PGPatcher (ParallaxGen) — если стоят PBR или parallax-текстуры.
3. Synthesis-патчеры.
4. Прекэш травы NGIO: `GrassControl.ini` включить `Use-grass-cache` и `Only-load-from-cache`; создать `PrecacheGrass.txt` в корне игры ⚠ для VR — папка с `SkyrimVR.exe`; запустить «Precache Grass» из меню MO2 Tools; папку `Grass` из Overwrite — в отдельный мод.
5. xLODGen — LOD рельефа (ресурс SSE Terrain Tamriel #54680), режим TES5VR ⚠ (имя исполняемого файла `TES5VRLODGenx64.exe` или аргумент).
6. TexGen, затем DynDOLOD 3 (Resources SE 3 + DynDOLOD DLL NG) в режиме TES5VR; руководство `DynDOLOD_Manual_TES5VR.html` внутри архива.
7. Тестовый прогон: Вайтран, Рифтен, лес у Ривервуда — время кадра и `crash-*.log`.

## Русский язык

Сборки Wabbajack требуют английскую игру. Для русской игры понадобятся: русские строки в Strings Fix, переводы ESP-модов (вкладка Translations на Nexus, xTranslator), шрифты с кириллицей для SkyUI VR, Scaleform Translation++ VR и Dynamic String Distributor (уже в ядре). Список конкретных модов — во второй подборке «Skyrim VR Other Mods 2026», раздел «Русификация».

## ⚠ Что агенту проверить на актуальных страницах

1. Имя файла настроек Engine Fixes VR и ключ `MaxStdio`.
2. Режим и настройки Root Builder 5.x (копирование или ссылки) для VR.
3. Аргумент или имя исполняемого файла xEdit, xLODGen и DynDOLOD для VR (`-tes5vr` или переименование).
4. Путь `sksevr.log` и вид строки об ошибке загрузки плагина.
5. Папка для `PrecacheGrass.txt` в VR.
6. Выбор игры в Synthesis для Skyrim VR.
7. Текущие релизы Pandora (VR), OpenComposite Unleashed (корневые файлы и `opencomposite.ini`), Open Shaders.
8. Названия опций установщиков (FOMOD) там, где в карточке стоит «неизвестно — общие правила».
