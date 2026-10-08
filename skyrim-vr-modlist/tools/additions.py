# Additions from the 2026-10-08 sweep of 27 popular Wabbajack lists + 2026 releases.
# Every item here was kept by two independent skeptic passes (VR compatibility, redundancy/value).

NX = "https://www.nexusmods.com/skyrimspecialedition/mods/{}"


def nx(i):
    return NX.format(i)


def N(**kw):
    kw["new"] = True
    return kw


NEW_SECTIONS = [
    # (insert after section id, section dict)
    ("vr", {
        "id": "hitech",
        "title": "Хайтек-новинки 2026",
        "lead": "Новые SKSE-технологии этого года, которые работают в VR. Метка «проверить» значит: VR заявлен автором или виден в исходниках, "
                "но в VR-сборках мод ещё не обкатан. Ставьте такие по одному, смотрите Documents/My Games/Skyrim VR/SKSE/sksevr.log и время кадра.",
        "items": [
            N(name="Smooth Terrain", id=186875, ver="0.6.0", tag="rec",
              note="Ваш пример. На лету дробит меши ландшафта вокруг игрока: холмы без углов, коллизия и сейвы не меняются. Одна DLL на SE/AE/VR (видно в исходниках), стоит в Yggdrasil VR рядом с Open Shaders. Метка AI Assisted. Начните с настроек по умолчанию и сверьте время кадра."),
            N(name="Helios + MMSF, Luma Utility, XEMI Utility", id=181533,
              extra=[("MMSF", nx(183073)), ("Luma", nx(177961)), ("XEMI", nx(159084))], ver="1.01", tag="opt",
              note="Ваш пример, преемник DIAL: свет в интерьерах с окнами следует за погодой и временем суток. Набор версий как в Stormcrown VR: Helios 1.01, Luma 1.7, MMSF 1.1, XEMI 1.6. Luma и MMSF 2.x с ним несовместимы. С интерьерным светом Lux связку никто не проверял."),
            N(name="Inventory Selfie VR — Redux", id=190704, ver="1.3", tag="rec",
              note="VR-замена Show Player In Inventory: в меню видно настоящее тело VRIK, без клона. Нужен VRIK 0.8.7+. Берите 1.3 — в ней исправлен вылет с HDT-SMP. Стоит в Tahrovin — Grit. Со старым View Yourself VR вместе не ставить."),
            N(name="Pull Arrows VR — Immersive Extraction", id=169833, ver="2.0", tag="rec",
              note="Стрелы, болты и брошенное оружие вытаскиваются из тел рукой: с сопротивлением, звуком и кровью. Нужны HIGGS, Weapon Throw VR и Broken Feathers. Есть в трёх VR-сборках."),
            N(name="Cold Breath NG", id=174838, tag="rec",
              note="Пар изо рта на холоде у игрока, NPC и существ, без скриптов. Автор прямо пишет «для 1.5.97/1.6/VR». Старые скриптовые моды пара убрать. Проверка: у NPC в Винтерхолде идёт пар, в sksevr.log нет ошибок."),
            N(name="Interactive Waters — VR (beta)", id=166560, tag="opt",
              note="Руки поднимают на воде рябь, волны и брызги, эффект зависит от скорости и силы удара. Только VR, стоит в Librum VR и Panda's Sovngarde. Бета."),
            N(name="Immersive Harvesting VR", id=186754, tag="opt",
              note="Растения срываются рукой через HIGGS, ингредиент сразу в ладони. Стоит в Yggdrasil VR. Метка AI-Generated. С автосбором не совмещать."),
            N(name="ISPVR — Immersive Spellcasting VR", id=164183, tag="opt",
              note="Магия кистью: сжал — заряд, вибрация — готово, раскрыл ладонь — выстрел. В VRIK выключить Open Hand Casting. Стоит в Panda's Sovngarde."),
            N(name="Steeds of Omega VR — NPC Mounted Combat", id=169221, ver="0.9.5 beta", tag="opt",
              note="Конные NPC в бою атакуют, отходят и не падают с лошадей; всадника можно стащить через HIGGS. Пара к Steeds of Ultima VR. Стоит в Tempus VR."),
            N(name="Dynamic Footprints SKSE", id=175254, tag="try",
              note="Работающая в VR часть идеи Dynamic Terrain Deformation: следы игрока, NPC и существ на снегу, пепле и песке. Автор: «рассчитан на SE, AE и VR, VR проверить не могу», есть отзыв о работе в VR. Вместо старых Footprints, не вместе."),
            N(name="DynamicShader — DynamicSnow", id=189713, tag="try",
              note="Настоящая деформация вершин ландшафта поверх Smooth Terrain: колеи в снегу, песке и грязи. В README только SE/AE, VR не подтверждён. Только для эксперимента на отдельном сохранении, не вместе с Dynamic Footprints."),
            N(name="XPMF — Extended Projected Materials Framework", id=192698, ver="0.7", tag="try",
              note="Проецируемый снег и пепел на объектах: текстура как у земли, под крышами чисто, учитывает Seasons of Skyrim. VR заявлен, нужен VR Address Library 0.266+. Версия 0.x."),
            N(name="Frostwalker", id=184628, tag="try",
              note="Морозная магия превращает воду в льдины, по которым можно идти. В исходниках есть отдельные VR-адреса. Проверка: заморозить воду морозным заклинанием."),
            N(name="Bobbing Framework", id=186081, tag="try",
              note="Лодки и плавучие предметы покачиваются на воде без замены мешей. В VR автор отключил хук отрисовки из-за вылетов. Проверка: лодки у Рифтена."),
            N(name="Immersive NPC Dialogue — VR", id=184804, tag="try",
              note="Разговор начинается взмахом руки в сторону NPC, варианты ответа — на запястье. Только SKSEVR, автор Interactive Waters. Ни в одной сборке пока нет."),
            N(name="Palm Compass VR", id=189452, tag="try",
              note="Компас уходит с HUD на ладонь: подняли раскрытую руку — компас над ней. Нужны VRIK и HIGGS. Метка AI-Generated."),
            N(name="Horizon Fix", id=184607, tag="opt",
              note="Убирает разрыв на горизонте: полоса перехода к небу и водная «юбка» до горизонта. В коде есть отдельная VR-ветка, в Open Shaders — фича-компаньон. В VR работает урезанно."),
        ],
    }),
    ("combat", {
        "id": "immersion",
        "title": "Мир, ИИ и погружение",
        "lead": "Поведение NPC, экономика, зоны и мелкие системы, которые оживляют мир. Почти всё здесь — плагины без DLL или моды с отдельной VR-сборкой.",
        "items": [
            N(name="Locational Encounter Zones", id=85212, tag="rec", note="Стража у входа в подземелье того же уровня, что и враги внутри. Одна DLL с VR-пресетом, 6 VR-сборок."),
            N(name="Don't Stay in The Water — NPC Water AI Fix", id=52164, file="VR 4.1", tag="rec", note="NPC перестают стоять в воде и топтаться у кромки в бою. Брать VR-файл 4.1, не AE-версию 5.x."),
            N(name="Combat Pathing Revolution + VR", id=86950, extra=[("VR-DLL", nx(87895))], tag="opt", note="NPC в бою кружат, отступают и обходят. Поверх основного — DLL с VR-страницы."),
            N(name="AI Overhaul", id=21654, tag="opt", note="Живее распорядок и реакции ванильных NPC. Путь B — файл «SE Only», путь A — AE-файл. Нужны патчи с NPC-модами."),
            N(name="Realistic AI Detection (RAID)", id=2345, tag="opt", note="Зорче зрение и слух врагов, дольше поиски, без скриптов. RAID 3 Medium или Lite."),
            N(name="Smart NPC Potions", id=40102, tag="opt", note="Враги носят и пьют зелья, используют яды. VR заявлен в changelog."),
            N(name="NPC Spell Variance", id=132097, ver="2.7.1+", tag="opt", note="Маги-NPC используют весь арсенал. VR-хук исправлен только в 2.7.1 — не брать старее."),
            N(name="NPCs React To Invisibility + NPCs React To Necromancy", id=91480, extra=[("Necromancy", nx(70428))], tag="opt", note="Озвученные реакции NPC на невидимость и поднятых мертвецов."),
            N(name="Enhanced Reanimation + VR", id=43500, extra=[("VR-файл", nx(59512))], tag="opt", note="Улучшенное поднятие мёртвых. Основной 1.5.1 и VR-файл 1.5.1 поверх; SE 1.5.2 без VR-обновления не ставить."),
            N(name="Frozen Electrocuted Combustion VR", id=59118, tag="opt", note="Замороженные, обугленные и наэлектризованные тела. Брать VR-страницу, не SE 3532."),
            N(name="Arena — An Encounter Zone Overhaul", id=33487, tag="opt", note="Опасность растёт по регионам, а не под уровень игрока. Совместим с Locational Encounter Zones."),
            N(name="Trade and Barter", id=23081, tag="opt", note="Настройка курсов торговли и золота торговцев."),
            N(name="Realistic Mining and Chopping for VR + VR Refit", id=16692, extra=[("VR Refit", nx(49205))], tag="rec",
              note="Руду и дрова добывают настоящими взмахами, а VR Refit роняет их физическими предметами. Файл «for VR - USSEP». 8 VR-сборок."),
            N(name="Gift by Hand VR", id=99809, tag="opt", note="Отдать предмет NPC, протянув его рукой."),
            N(name="Sleeping Expanded", id=59250, tag="opt", note="Разные позы сна NPC и реакции на спящих."),
            N(name="Be Seated — Skyrim VR Edition", id=16613, tag="opt", note="Сесть где угодно — на землю, у костра."),
            N(name="SunHelm Survival", id=39414, tag="opt", note="Голод, жажда, усталость, холод. CC-выживание на странице отключено, дубля нет."),
            N(name="Recipe Auto-Learn + Reading Is Good", id=84909, extra=[("Reading Is Good VR", nx(42026))], tag="opt", note="Рецепты открывают эффекты ингредиентов; книги навыков дают опыт сразу. У Reading Is Good брать VR-файл."),
            N(name="Mum's the Word NG", id=77409, tag="opt", note="Снимает метку «украдено», если кражу никто не видел — с HIGGS легко схватить чужое. VR заявлен."),
            N(name="Honed Metal", id=61015, file="VR", tag="opt", note="Кузнецы и маги за плату куют и зачаровывают снаряжение."),
            N(name="GIST — Genuinely Intelligent Soul Trap", id=15755, tag="opt", note="Душа идёт в самый подходящий камень."),
            N(name="SCIE — Crafting Inventory Extender", id=170497, ver="2.6", tag="opt", note="Верстак берёт материалы из ближних сундуков и у спутников. В 2.6 исправлен VR-вылет на старте."),
            N(name="Dirt and Blood", id=38886, tag="opt", note="На телах копятся грязь и кровь, смываются водой. Поставить VR-патч «No Washing Animation»."),
            N(name="Dynamic Things Alternative + Random Barrel Roll", id=60741, extra=[("Random Barrel Roll", nx(78195))], tag="opt", note="Разнообразие контейнеров и случайный поворот бочек через BOS VR."),
            N(name="Better Resource Warnings", id=26751, tag="opt", note="Сердцебиение и дыхание при низком здоровье — в шлеме звук заметнее полосок."),
            N(name="Sink Or Swim NG", id=78610, tag="opt", note="В тяжёлой броне игрок тонет и идёт по дну. Сборка NG для AE/VR, не старая 42962."),
            N(name="Tamrielic Names + NPCs Names Distributor", id=73153, extra=[("NND", nx(73081))], tag="opt", note="Безымянные NPC получают имена по расе. Полезно с ИИ-NPC."),
        ],
    }),
]

ADD = {
    "tools": [
        N(name="DynDOLOD 3 + Resources SE 3 + DynDOLOD DLL NG", id=68518, extra=[("Resources", nx(52897)), ("DLL NG", nx(97720))], ver="Alpha-210 / 59 / 43", tag="core",
          note="Генератор дальних LOD. Режим TES5VR, DLL NG общая для SE/AE/VR, старую DLL VR не ставить. Запуск — на финальном этапе."),
        N(name="xLODGen", url="https://stepmodifications.org/forum/topic/13451-xlodgen/", ver="132", tag="core",
          note="LOD рельефа перед DynDOLOD. Ресурс SSE Terrain Tamriel — в блоке финальной генерации."),
        N(name="MCM Memory", id=189722, ver="1.5.3", tag="rec",
          note="Сохраняет настройки всех MCM и сам восстанавливает их в новой игре. Преемник MCM Recorder, VR-фикс в 1.5.3. Стоит в Stormcrown VR."),
        N(name="More Informative Console", id=19250, tag="opt", note="Консоль показывает плагин-источник, перезаписи, меши — главный инструмент отладки. Есть VR-файл."),
        N(name="Lights Conflict Resolver", id=175086, tag="opt", note="Находит дубли в конфигах Light Placer, чтобы свет не удваивался. Свет у нас из Light Placer, CS Light и Lux — дубли реальны."),
        N(name="VR Keyboard", id=64319, tag="opt", note="Виртуальная клавиатура для имён и поиска — с OpenComposite оверлея SteamVR нет."),
        N(name="PGPatcher (бывш. ParallaxGen)", id=120946, ver="2.x", tag="opt", note="Патчер мешей под parallax и PBR. Понадобится на этапе текстур."),
        N(name="NIF Preview for MO2", id=137741, tag="opt", note="3D-превью мешей прямо в окне конфликтов MO2 2.5.x."),
    ],
    "frameworks": [
        N(name="Scaleform Translation Plus Plus VR", id=60210, ver="1.4.1", tag="rec",
          note="Для игры на русском: вложенные переводы SkyUI и запасной английский, в MCM не будет сырых $KEY. Стоит в 4 VR-сборках."),
        N(name="UIExtensions", id=17561, tag="opt", note="Библиотека меню, без DLL. Ставить, когда её потребует мод."),
        N(name="Object Categorization Framework", id=81469, tag="opt", note="Разметка предметов через KID для сортировки и иконок I4."),
        N(name="Dynamic String Distributor", id=107676, tag="opt", note="Правит тексты на лету по JSON — удобно для русификации без ESP-переводов. VR-пресет в исходниках."),
        N(name="MCM Unlocked", id=180186, tag="opt", note="Снимает лимит SkyUI в 128 MCM и ускоряет меню. VR заявлен, стоит в Stormcrown VR. Метка AI-Generated."),
        N(name="Dynamic Leveled Lists + Dynamic Container Loot", id=172083, extra=[("DCL", nx(172018))], ver="0.x", tag="opt",
          note="Сливает конфликтующие левел-листы прямо в игре. В установщике выбрать VR. Те же списки не сливать ещё и Bashed Patch."),
    ],
    "fixes": [
        N(name="Save Unbaker VR", id=86265, tag="rec", note="Часть данных берётся из плагинов, а не из сохранения — меньше поломок при смене модов. Во всех крупных VR-сборках 2025–2026."),
        N(name="Dragonactorscript Infinite Loop Fix", id=87940, tag="rec", note="Чинит бесконечный цикл в скрипте драконов, который забивает Papyrus. Вариант под USSEP."),
        N(name="Telekinesis Aim Fix VR", id=191729, tag="rec", note="Телекинез бросает туда, куда указывает рука. Стоит в Yggdrasil VR и Tahrovin — Grit."),
        N(name="Collision Sentinel", id=181445, tag="opt", note="Защищает от вылетов из-за битой коллизии в модовых мешах и пишет виновника в лог. VR 1.4.15 в списке поддержки, стоит в Grit-сборках. Метка AI-Generated."),
        N(name="Recursion Monitor", id=76867, tag="opt", note="Обрывает зацикленную Papyrus-рекурсию до того, как она обрушит FPS."),
        N(name="Combat Music Fix NG", id=110459, tag="opt", note="Боевая музыка выключается после боя. Проверить загрузку в sksevr.log."),
        N(name="Fixed Mesh Lighting", id=53653, tag="opt", note="Предметы перестают светиться в темноте."),
        N(name="Aurora Fix + Sky Reflection Fix", id=77834, extra=[("Sky Reflection Fix", nx(110604))], tag="opt",
          note="Сияние не застревает при смене мира; отражение неба привязано к камере — вода и кубмапы отражают правильно. Обе DLL общие для SE/AE/VR."),
        N(name="Water Effects Brightness and Reflection Fix", id=63862, tag="opt", note="Убирает пересвеченные брызги, пену и водопады."),
        N(name="Unaggressive Dragon Priests Fix + Dwemer Gates Don't Reset", id=69026, extra=[("Dwemer Gates", nx(26331))], tag="opt", note="Два мелких фикса логики, которых нет в USSEP."),
        N(name="CritterSpawn Congestion Fix", id=67276, tag="opt", note="Снимает затор скриптов спавна бабочек и рыб."),
        N(name="Unofficial Skyrim Modder's Patch (USMP)", id=49616, tag="opt", note="Фиксы поверх USSEP: ассеты, AI-пакеты, навмеши. Версию подбирать под выбранный путь USSEP."),
        N(name="Saving on Steed — Horse Save Load Fix", id=173629, ver="0.1.2", tag="try", note="Чинит выброс в небо после загрузки сейва верхом. Две VR-сборки ставят 0.1.2, но VR автор не заявлял. Ветку 0.2 не брать."),
    ],
    "vr": [
        N(name="Arctal's VRIK Tweaks", id=63663, tag="rec", note="Быстрые жесты для заклинаний и криков, правка ragdoll, fNearDistance против мерцания снега. 8 VR-сборок, есть русификация."),
        N(name="No Stagger Mod", id=16335, tag="rec", note="Убирает пошатывание игрока — в VR оно дёргает камеру и укачивает. Во всех 9 VR-сборках."),
        N(name="Neutral VR Animations for VRIK", id=28831, tag="opt", note="Тело VRIK не принимает боевые стойки."),
        N(name="SKSEVR Perk Extender", id=16330, tag="opt", note="Без него большие перк-моды вылетают при входе в дерево. Его statsmenu.swf не давать перезаписать."),
        N(name="Smooth Carriage Ride VR + Im Walkin' Here VR", id=129594, extra=[("Im Walkin' Here", nx(39433))], tag="opt", note="Комфорт: карета не трясёт камеру, NPC не сдвигают игрока толчками."),
        N(name="No more werewolf hat", id=104975, tag="opt", note="Голова вервольфа больше не закрывает обзор."),
        N(name="VR Equip", id=83092, tag="opt", note="Поднёс вещь к телу — надел, ко рту — съел."),
        N(name="Auto Sneak and Jump VR", id=23649, tag="opt", note="Скрытность — когда реально приседаете, прыжок — когда подпрыгиваете. Со Sprint Jump VR выбрать одну схему."),
        N(name="Spell Auto-Aim VR", id=119689, tag="opt", note="Мягкое автонаведение заклинаний. Не совместим со SpellBender VR."),
        N(name="Durability VR + Immersive Smithing", id=76830, extra=[("Immersive Smithing", nx(72298))], tag="opt", note="Износ снаряжения с полосками на запястье и физическая кузня с молотом."),
        N(name="PLANCK VR Stability Patch", id=188233, tag="opt", note="Неофициальная пересборка DLL PLANCK 0.8.1. Ставить, если PLANCK вылетает. Перезаписывает activeragdoll.dll."),
        N(name="VRIK Closed Fist", id=182410, tag="opt", note="Свободные руки сжимаются в кулак. Пара к Lethal Unarmed VR."),
        N(name="Steeds of Ultima — VR Mounted Combat", id=81220, tag="opt", note="Магия, крики и посохи с седла. Nemesis-патч собрать через Pandora."),
    ],
    "ui": [
        N(name="Essential Favorites VR + Favorite Misc Items", id=59554, extra=[("Favorite Misc Items", nx(42750))], tag="rec",
          note="Избранное нельзя случайно продать или выронить — с HIGGS это частая беда. Favorite Misc Items добавляет в Избранное факелы и кирки, VR-файл."),
        N(name="VR Menu Mouse Fix", id=33414, tag="opt", note="Курсор от контроллера в MCM, поиске SkyUI, назначении клавиш."),
        N(name="Crafting Categories for SkyUI VR (COCKS)", id=81409, file="VR", tag="opt", note="Категории в меню кузницы вместо одного длинного списка."),
        N(name="Floating Subtitles VR", id=183714, tag="opt", note="Субтитры висят над говорящим NPC. Нужен ImGui VR Helper. Метка AI-Generated."),
        N(name="Floating Damage NG", id=184159, tag="opt", note="Числа урона висят в 3D у цели. Нужен ImGui VR Helper 1.5.4+."),
        N(name="Clear HUD VR + Clean Menu", id=49657, extra=[("Clean Menu", nx(53524))], tag="opt", note="Чистый HUD и главное меню. Unobtrusive HUD не нужен — дублирует Clear HUD."),
        N(name="Minimal Enemy Healthbar VR", id=17812, tag="opt"),
        N(name="Dynamic Location Pop-ups (VR)", id=155978, extra=[("основной", nx(153122))], tag="opt", note="Название локации при каждом входе."),
        N(name="RacemenuVR", id=156898, tag="opt", note="Редактор персонажа. Проверенный вариант из 4 VR-сборок."),
        N(name="RaceMenu VR 2", id=192158, ver="0.1.x beta", tag="try", note="Новая надстройка: стабильный вид лица, Sculpt с undo, своя клавиатура. Бета, вместо RacemenuVR."),
        N(name="I5 — Information Injector Improved", id=192976, ver="0.4", tag="try", note="Преемник I4: меню не тормозит при каждом обновлении. VR включён в 0.3. Если I4 не вылетает — оставить I4."),
    ],
    "gfx": [
        N(name="Rim Lighting Removed", id=164488, tag="opt", note="Убирает ванильную ореольную подсветку объектов. Дело вкуса, стоит в Panda's Sovngarde."),
        N(name="Native Water Light Stabilizer", id=186700, tag="try", note="Меньше мерцания бликов на воде. VR заявлен, но один пользователь писал, что с ним не грузится Open Shaders — проверять только вместе с OS 2.17."),
    ],
    "world": [
        N(name="Embers XD", id=37085, tag="rec", note="Объёмный огонь, искры и дым у костров, факелов и свечей. В CS Light выбрать опцию под Embers XD. 7 VR-сборок."),
        N(name="Moons and Stars + SKSEVR DLL", id=73336, extra=[("SKSEVR DLL", nx(73667))], ver="2.0.2", tag="rec",
          note="Реальные звёзды, фазы лун, вращение неба. Держаться 2.0.2 — у 2.1 нет VR-DLL."),
        N(name="Storm Lightning for SSE and VR", id=29243, tag="rec", note="Разряды в землю, синхронный гром, вспышки. Дополняет грозы Azurite."),
        N(name="Natural Waterfalls", id=87261, tag="opt", note="Брызги, пена и туман вместо ванильных полотен водопадов."),
        N(name="KittyVFX — Frost, Fire, Lightning, Dragon Breath, Healing, Portals", id=112509, tag="opt", note="Серия новых эффектов магии, без DLL. Магия кастуется прямо перед глазами."),
        N(name="Deadly Spell Impacts + Parallax Spell Impacts", id=12939, extra=[("Parallax", nx(83935))], tag="opt", note="Выжженные и обледенелые следы заклинаний на поверхностях."),
        N(name="slightly Better Dust + Improved Sparks", id=133368, extra=[("Improved Sparks", nx(19831))], tag="opt", note="Мелкая пыль вместо облаков, настоящие искры от ударов."),
        N(name="Volcanic Tundra — Heat Wave Effects", id=13749, tag="opt", note="Марево над горячими источниками. Если в шлеме мешает — выключить."),
    ],
    "land": [
        N(name="LOD Model Library for DynDOLOD", id=87521, tag="rec", note="Качественные дальние скалы, руины и постройки для DynDOLOD 3. Стандарт next-gen сборок 2026."),
        N(name="No Grass In Caves", id=12431, tag="opt"),
        N(name="Better Dynamic Snow + Better Dynamic Ash", id=9121, extra=[("BDA", nx(54754))], tag="opt", note="Снег и пепел на объектах по геометрии."),
        N(name="Simple Snow Improvements (BOS)", id=78702, tag="opt", note="Чинит блеск и швы снега через BOS VR."),
        N(name="Footprints + SPID for Footprints", id=3808, extra=[("SPID for Footprints", nx(54924))], tag="opt", note="Проверенные следы на снегу и песке. Или Dynamic Footprints SKSE из хайтек-раздела — одно из двух."),
        N(name="Auto Parallax", id=79473, tag="opt", note="Отключает параллакс на мешах без карты высот. Нужен на этапе parallax-текстур."),
    ],
    "anim": [
        N(name="XPMSSE + XP32 First Person Skeleton CTD Bugfix for VR", id=1988, extra=[("VR-фикс", nx(34301))], tag="core",
          note="Расширенный скелет — база для FSMP и многих анимаций. Без VR-фикса поверх SE-скелет в VR даёт вылеты."),
        N(name="NPC Animation Remix + Gesture Animation Remix (OAR)", id=63471, extra=[("Gesture Remix", nx(64420))], tag="rec",
          note="Стойки, ходьба и жесты NPC в диалогах. В VR собеседник в метре от вас — деревянные позы видно сразу."),
        N(name="Expressive Facial Animation — Male + Female", id=19532, extra=[("Female", nx(19181))], tag="rec", note="Мимика и моргание NPC. Дополняет MFG Fix NG и ИИ-NPC."),
        N(name="Pristine Vanilla Movement", id=66635, tag="opt", note="Исправленные ванильные анимации передвижения — база под OAR-пакеты."),
        N(name="Arm Movement Animations (OAR)", id=62849, tag="opt", note="NPC при ходьбе держат руки естественно."),
        N(name="Take a Seat + Improved Table Transitions", id=54193, extra=[("Table Transitions", nx(84160))], tag="opt", note="Позы сидения и плавный вход за стол без телепорта."),
        N(name="Lively Children Animations (OAR)", id=67557, tag="opt"),
        N(name="EVG Conditional Idles", id=34006, tag="opt", note="NPC мёрзнет, устал, ранен. Animation Variance не брать — дублирует Remix."),
        N(name="Goetia Animations — Spell Casting + Conditional Shouts", id=70204, extra=[("Shouts", nx(76388))], tag="opt", note="Каст и крики у NPC-магов. У игрока в VR не видны."),
        N(name="Leviathan / Vanargand Animations (стойки и атаки NPC)", id=47092, tag="opt", note="Разнообразие врагов в ближнем бою. Sneak-пакеты для игрока не брать."),
        N(name="Conditional Tavern Cheering (OAR)", id=63029, tag="opt"),
        N(name="Super Fast Get Up Animation", id=46714, tag="opt", note="С PLANCK враги падают часто — быстрый подъём не тормозит бой."),
        N(name="Variadic Collision Dynamics", id=183892, extra=[("Resources", nx(184110))], tag="try", note="Капсула коллизии меняется по позе — меньше застреваний. Капсула игрока в VR — зона PLANCK, конфликт вероятен."),
        N(name="A-Pose Bug Fix", id=168903, tag="try", note="Только как лекарство, если появится A-поза. VR не подтверждён."),
    ],
    "combat": [
        N(name="Simple Offence Suppression (VR)", id=59508, tag="rec", note="Спутники и нейтралы не становятся врагами от случайного удара — с физическим боем это обычное дело."),
        N(name="Mysticism — A Magic Overhaul", id=27839, tag="rec", note="Переработка всей магии, пара к Adamant. Без DLL, 7 VR-сборок."),
        N(name="Thaumaturgy + Apothecary + Mundus", id=57138, extra=[("Apothecary", nx(52130)), ("Mundus", nx(33411))], tag="opt", note="Зачарование, алхимия и камни-хранители из набора SimonRim. Опциональную DLL Enchantment XP Tweak не ставить без проверки."),
        N(name="Experience", id=17751, tag="opt", note="Уровень за квесты и исследование. DLL с VR Address Library, стоит в Stormcrown VR."),
        N(name="Death Drop Overhaul", id=151590, tag="opt", note="Оружие убитых падает с инерцией, его можно поднять HIGGS."),
        N(name="Magic Sneak Attacks VR + Physical Dodge VR", id=68028, extra=[("Physical Dodge", nx(58605))], tag="opt", note="Скрытые атаки магией; уклонение рывком корпуса."),
        N(name="Throat Slit — VR", id=184140, tag="opt", note="Горло перерезают движением руки с кинжалом."),
        N(name="Dynamic Bloodpool Framework", id=172080, tag="opt", note="Лужи крови растекаются по рельефу. VR Address Library в требованиях, стоит в Panda's Sovngarde."),
        N(name="DF Asset Packs + Next-Gen Decapitations", id=126328, extra=[("Humanoid", nx(126327)), ("Decapitations", nx(135254))], tag="opt", note="Нужны, если стоит Dismembering Framework."),
        N(name="Sanguine Symphony", id=148388, tag="opt", note="Конфиги Core Impact Framework: отклик зависит от брони и места удара."),
    ],
    "audio": [
        N(name="UHDAP — Music HQ", id=18115, tag="opt", note="Ванильная музыка без артефактов. Голоса EN — только при английской озвучке."),
        N(name="Wildwood Echoes + Murmurs and Mead", id=112008, extra=[("Murmurs and Mead", nx(114716))], tag="opt", note="Звуки леса и 18 вариантов шума таверн."),
        N(name="Haunting Harmonies of Hjaalmarch + Whispers of the Daedric Princes", id=125873, extra=[("Whispers", nx(141931))], tag="opt", note="Атмосфера болот Морфала и шёпот у святилищ. Позиционный звук в шлеме."),
        N(name="Immersive Draw Sheathe Sounds VR", id=44992, tag="opt"),
    ],
    "perf": [
        N(name="S.L.A.C.K. — Save and Load Accelerator", id=163969, file="VR", tag="rec",
          note="Ускоряет запись и чтение ко-сейвов SKSE в разы. Дополняет Seamless Saving VR. Отдельный VR-архив под SKSEVR 2.0.12."),
    ],
}

# notes to append to existing page items, by item id
PATCH_NOTES = {
    133568: " Старый MfgFix-vr 1.0 вместе не ставить.",
    57339: " Нужен XPMSSE с VR-фиксом.",
}

# replace VR Climbing with the fork fresh VR lists moved to
REPLACE = {
    168553: dict(name="VR Climbing — Aelove Ver", id=170321, ver="0.11.3", tag="opt", new=True,
                 note="Форк VR Climbing с доп. настройками, свежие VR-сборки перешли на него. Ставить вместо оригинала 168553. Нужны HIGGS и Skyrim VR Tools. Метка AI-generated."),
}

DONT_ADD = [
    ("Dynamic Terrain Deformation, Grid Inventory", "Ваши примеры, но только SE/AE: в исходниках VR выключен. В VR вместо них Smooth Terrain, Dynamic Footprints."),
    ("Show Player In Inventory", "Работает через камеру от третьего лица в плоском меню. В VR — Inventory Selfie VR Redux."),
    ("Meridian UI и моды на нём", "Интерфейс на Chromium только для SE/AE, VR в разработке."),
    ("HorsePower, Skyrim Mounted Movesets", "SE-DLL и анимации от третьего лица. В VR — Steeds of Ultima и Steeds of Omega VR."),
    ("StepUpOnto, EVG Animated Traversal, DovaJump", "Перелезание и прыжки игрока для плоского режима. В VR — VR Climbing."),
    ("Intellightent", "Уже встроен в Open Shaders как Shadow Caster Manager, отдельная DLL его отключит."),
    ("EVLaS (DLL-версия)", "Только SE/AE, объёмный свет уже даёт Open Shaders."),
    ("TrueHUD, Detection Meter, Oxygen Meter 2, Compass Navigation Overhaul, Tween Menu Overhaul, Loading Menu Overhaul, Dragonborn's Bestiary", "Плоские HUD и меню на SE-DLL."),
    ("SmoothCam, First Person FOV и Height Fix, Camera Persistence Fixes, Auto Input Switch, BTPS, Better AltTab", "Камеру и ввод в VR задают шлем и контроллеры."),
    ("CFPAO, Female/Male Player Animations, Disable Turn Animation, Offset Movement Animation, Dynamic Crafting Animations", "Анимации игрока: телом управляет VRIK."),
    ("Custom Skills Framework, Console Commands Extender, LeveledList Crash Fix, Sprint Sneak Movement Speed Fix, Equip Enchantment Fix, CARP, Better Combat Escape NG, Survival Mode Improved, IFrame Generator, Use or Take, KreatE, Classic Sprinting Redone, Simple Dual Sheath",
     "Популярные в SE-сборках DLL без VR-версии — проверено по каждому."),
    ("USSEP Behaviour Patch", "SE-патч поведений; поведения VR собирает Pandora."),
    ("Nemesis вместе с Pandora", "Оба пишут одни и те же файлы. Только один генератор."),
    ("Open Shaders With DLSS5 Neural Rendering", "Неофициальный экспериментальный форк, с Open Shaders не смешивать."),
]

DONT_REPLACE = {
    "Skyrim Upscaler VR (PureDark) или vrperfkit вместе с апскейлом Open Shaders":
        ("Skyrim Upscaler (PureDark, включая AIO 2026) или vrperfkit вместе с апскейлом Open Shaders",
         "Два апскейлера дерутся за один кадр, а AIO 2026 вообще сделан для плоской игры. Апскейл — только встроенный."),
}
