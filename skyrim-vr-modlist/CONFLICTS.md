# Конфликты, порядок и запреты

Агент сверяется с этим файлом перед каждой фазой. Если правило расходится с карточкой мода, главнее это правило.

## Группы «одно из»

В каждой группе ставится один мод. По умолчанию — указанный, если пользователь не выбрал иначе в `OVERRIDES`.

| Группа | Варианты | По умолчанию | Правило |
|---|---|---|---|
| `masters-path` | Путь A. Обновлённые мастера SSE 1.6.1170 + 4 бесплатных CC; Путь B. USSEP 4.2.5b + Skyrim VR USSEP patch for 4.2.5b | Путь A. Обновлённые мастера SSE 1.6.1170 + 4 бесплатных CC | ставится один; по умолчанию первый, пока критик не уточнил |
| `footprints` | Dynamic Footprints SKSE; Footprints + SPID for Footprints | Dynamic Footprints SKSE | ставится один; по умолчанию первый, пока критик не уточнил |
| `racemenu` | RacemenuVR; RaceMenu VR 2 | RacemenuVR | ставится один; по умолчанию первый, пока критик не уточнил |
| `shaders` | Open Shaders; Community Shaders Expanded (CSX), VR-сборка | Open Shaders | ставится один; по умолчанию первый, пока критик не уточнил |
| `water` | Simplicity of Sea; Water for ENB | Simplicity of Sea | ставится один; по умолчанию первый, пока критик не уточнил |
| `grass` | Merethic Grasslands; Cathedral 3D Grass Library + 3D-растения | Merethic Grasslands | ставится один; по умолчанию первый, пока критик не уточнил |
| `audio-stack` | Audio Overhaul for Skyrim; Immersive Sounds Compendium + AOS–ISC patch | Audio Overhaul for Skyrim | ставится один; по умолчанию первый, пока критик не уточнил |
| `ai-npc` | SkyrimNet; Mantella; CHIM | SkyrimNet | ставится один; по умолчанию первый, пока критик не уточнил |

## Порядок в MO2 (левая панель)

Разделители сверху вниз: 00 Инструменты и корень → 01 Мастера и USSEP → 02 SKSEVR и библиотеки → 03 Фиксы движка → 04 Шейдеры и свет → 05 VR-ядро → 06 Хайтек 2026 → 07 Интерфейс → 08 Звук → 09 Свет, погода, вода, VFX → 10 Ландшафт, трава, деревья → 11 Анимации и физика → 12 Бой и геймплей → 13 Мир, ИИ, погружение → 14 ИИ-NPC → 15 VR-рантайм и производительность.


## Порядок плагинов

Сначала LOOT, затем эти правила:


## Не ставить в VR

| Что | Почему |
|---|---|
| Community Shaders 1.7 и новее | Официальный CS убрал поддержку VR. Нужен Open Shaders или CSX. |
| Два шейдерных пакета сразу | Open Shaders, CSX и CS используют одни и те же файлы. Только один. |
| ENB | Несовместим с семейством CS и слишком дорог для VR. |
| SSE Engine Fixes, Address Library for SKSE, SKSE64 | Это версии для SE/AE. В VR — Engine Fixes VR, VR Address Library, SKSEVR. |
| Backported Extended ESL Support | Без VR-поддержки. Вместо него Skyrim VR ESL Support. |
| Scrambled Bugs | В VR не работает. Вместо него Poached Bugs VR. |
| SSE Display Tweaks | Нет VR-сборки, частоту кадров в VR задаёт шлем. |
| Precision, True Directional Movement, SkyParkour, SkyClimb | Только для плоского режима. В VR их роль играют PLANCK, Physical Collision VR, VR Climbing. |
| Skyrim Upscaler (PureDark, включая AIO 2026) или vrperfkit вместе с апскейлом Open Shaders | Два апскейлера дерутся за один кадр, а AIO 2026 вообще сделан для плоской игры. Апскейл — только встроенный. |
| ENB Light и Particle Lights for ENB | Не работают с CS 1.4+ и Open Shaders. Свет — через Light Placer. Исключение — CSX. |
| Volumetric Mists с Azurite III | FUS убрал его ради производительности, автор погоды больше не рекомендует. |
| Разделённые меши Lux | С Light Limit Fix не нужны, только добавляют draw calls. |
| Две сборки OpenComposite | Старый OpenComposite Fixes Custom Build или Unleashed — что-то одно. |
| Fuz Ro D-oh VR без необходимости | Принудительно включает субтитры. Ставить, только если его требует другой мод. |
| Dynamic Terrain Deformation, Grid Inventory | Ваши примеры, но только SE/AE: в исходниках VR выключен. В VR вместо них Smooth Terrain, Dynamic Footprints. |
| Show Player In Inventory | Работает через камеру от третьего лица в плоском меню. В VR — Inventory Selfie VR Redux. |
| Meridian UI и моды на нём | Интерфейс на Chromium только для SE/AE, VR в разработке. |
| HorsePower, Skyrim Mounted Movesets | SE-DLL и анимации от третьего лица. В VR — Steeds of Ultima и Steeds of Omega VR. |
| StepUpOnto, EVG Animated Traversal, DovaJump | Перелезание и прыжки игрока для плоского режима. В VR — VR Climbing. |
| Intellightent | Уже встроен в Open Shaders как Shadow Caster Manager, отдельная DLL его отключит. |
| EVLaS (DLL-версия) | Только SE/AE, объёмный свет уже даёт Open Shaders. |
| TrueHUD, Detection Meter, Oxygen Meter 2, Compass Navigation Overhaul, Tween Menu Overhaul, Loading Menu Overhaul, Dragonborn's Bestiary | Плоские HUD и меню на SE-DLL. |
| SmoothCam, First Person FOV и Height Fix, Camera Persistence Fixes, Auto Input Switch, BTPS, Better AltTab | Камеру и ввод в VR задают шлем и контроллеры. |
| CFPAO, Female/Male Player Animations, Disable Turn Animation, Offset Movement Animation, Dynamic Crafting Animations | Анимации игрока: телом управляет VRIK. |
| Custom Skills Framework, Console Commands Extender, LeveledList Crash Fix, Sprint Sneak Movement Speed Fix, Equip Enchantment Fix, CARP, Better Combat Escape NG, Survival Mode Improved, IFrame Generator, Use or Take, KreatE, Classic Sprinting Redone, Simple Dual Sheath | Популярные в SE-сборках DLL без VR-версии — проверено по каждому. |
| USSEP Behaviour Patch | SE-патч поведений; поведения VR собирает Pandora. |
| Nemesis вместе с Pandora | Оба пишут одни и те же файлы. Только один генератор. |
| Open Shaders With DLSS5 Neural Rendering | Неофициальный экспериментальный форк, с Open Shaders не смешивать. |
