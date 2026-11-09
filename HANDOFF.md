# RDR2 rain & fog project: full handoff

This document records everything done on this repository so far: Vestigia, Rain Particles Fix and Realistic Weather
in Red Dead Redemption 2. It covers what the problems were, how they were found, the reasoning behind each decision,
the current state, and what is still open. It is written so that another AI or a new chat can continue without the
original conversation.

- **Branch with all the work:** `claude/great-clarke-0hc562` (not merged into `main`).
- **Full download link for the user:** `https://github.com/DiligentCube007/RDR2-MODS-Claude-Knoladge-/archive/refs/heads/claude/great-clarke-0hc562.zip`
- **Session dates:** 2026-11-08 to 2026-11-09.

---

## 0. TL;DR

- **Rain look:** Rain Particles Fix (RPF) is merged into Vestigia. Shower, Hurricane and Drizzle splashes were rebuilt
  from RPF files, because Vestigia had its own broken copies in `active/str/`.
- **The big bug, the moving 2D "mist plane" in rainy weather:** the cause was **Vestigia's local-atmosphere fog noise**.
  Vestigia sets `local_atmosphere_voxel_noise_min/max` to 0/2 where vanilla uses about 0.43/0.75, plus related
  localized-fog changes. It was found by bisecting: renaming `lml` → Vestigia → its weather timecycles → a group of
  timecycle keys, by comparing against the vanilla timecycles. **Fix:** those 11 keys are set back to each weather's own
  vanilla values in the 13 rainy timecycles (wilderness region). This is installed as option 15.
- **Drizzle needed more:** its `weather.xml` entry (Fog switch 1 → 0, density map `Rain` → `RainDense`, option 20) and
  then vanilla fog structure in both regions (option 21). It now shows soft vanilla-like haze patches. Options 22 and 23
  tone those down.
- **The user tunes everything through optional folders** in `Vestigia/variants/00 - COMPATIBLE OPTIONS (use these)/`,
  each with a readme and usually a `lines changed.txt`. Installed files are only changed for confirmed fixes.
- **The odd rain look** that started part of this was mostly **DLSS** (the user uses DLSS Swapper). The user has since
  turned DLSS off.

---

## 1. Repository layout

```
RDR2-MODS-Claude-Knoladge-/
├─ HANDOFF.md                         ← this file
├─ CLAUDE.md                          ← auto-loaded pointer for Claude Code sessions
├─ tools/
│   ├─ audit.py                       ← consistency check (run: python3 tools/audit.py)
│   └─ tc_lib.py                      ← helpers to read/edit timecycle files
├─ Vestigia/                          ← "VESTIGIA 2.0 - A Visual Mod" by no12 (LML mod)
│   ├─ install.xml                    ← LML install file (ResourceGroups ess/wea/tem/det + StreamingFiles active/str)
│   ├─ active/
│   │   ├─ ess/   ← Visual Essentials: weather.xml, visualsettings.dat, w_*.xml timecycles, timecycle_mods_*, particle files
│   │   ├─ str/   ← streamed files (ADDONDLC:/VESTIGIA/ACTIVE/STR/...): shower/hurricane/drizzle-ground/sleet-ground
│   │   │            particles, blizzard3/4, custom weathers w_sunnydenver/la/no/nyc/seattle.xml
│   │   ├─ wea/   ← weatherGraph.xml, weatherclimates.xml (weather system)
│   │   ├─ tem/   ← regionTemperatureInfo.xml, weatherTemperatureConfig.xml
│   │   └─ det/   ← fallensnow, terraintessellation, env_accumulation, pedbreathingsettings.meta, snowglints
│   ├─ RAIN_MERGE_README.md           ← user-facing changelog (Updates 1–7)
│   ├─ _backup_original_rain_files/   ← originals of everything replaced (not loaded by LML)
│   ├─ timecycle vanila/              ← VANILLA timecycles uploaded by the user (spelling "vanila" is intentional/existing)
│   ├─ vanilla reference/weather.xml  ← VANILLA weather.xml (extracted by the user with OpenIV)
│   ├─ variants/
│   │   ├─ README.md                  ← start-here table of all options
│   │   ├─ 00 - COMPATIBLE OPTIONS (use these)/   ← all options made in this project (01–23, 99)
│   │   └─ (Vestigia's own official variants: grass texturing, level of detail, motion blur, night brightness,
│   │       old timecycle versions, pickup glow, rain particles, remove extra weathers, taa options,
│   │       temperature settings, weather system speed)  ← some have "!! DO NOT USE" notes
│   └─ merges/                        ← Vestigia's official merges (therealten graphical fixes, mightyelf "perfect TAA")
├─ Vestigia - Rain Sheets (Optional)/  ← our optional LML add-on (own weather.xml with THUNDER_SHEET enabled)
├─ Rain Particles Fix-5452-Final-1771113852/  ← original RPF mod (WhyStopNow, Nexus 5452), reference only
└─ RW Release 10004 20 2026-10-26T06-42Z zhfBtEA9f/  ← Realistic Weather (sauvy11, Nexus 10004)
    ├─ RealisticWeather.asi (+ Sauvy_ASI/ presets, Optional - Trainer)   ← script mod, game folder
    ├─ lml/Sauvy/Sauvy - RW Grass Sway/visualsettings.dat   ← now identical to Vestigia's (user's merged file)
    ├─ lml/Sauvy/Sauvy - RW Sheet/Impact/thunder_render_sheet.xml
    └─ RW mist plane fix (whirlwind + debris).txt   ← our note (turned out NOT to be the cause)
```

---

## 2. The user: setup and working preferences

**Setup:**
- Windows PC, RDR2 with **Lenny's Mod Loader (LML)** and ASI scripts.
- Uses **OpenIV** to extract game files. They extracted vanilla `weather.xml` and all vanilla timecycles for this project.
- Uses the **Rampage trainer** to switch weather.
- Uses **DLSS Swapper** (latest DLSS). They found that DLSS caused the strange rain look and turned DLSS off. Whether
  they now use TAA or DLAA is not confirmed.
- Takes HDR screenshots (`.jxr`). See section 11 for how to view them.
- **Installed mods:** Vestigia; RW (`.asi` in the game folder, plus LML parts); the Rain Sheets add-on is optional
  (unknown whether installed). RPF should be **removed** from `lml` because it is merged into Vestigia and would
  override the splash fix. RW Grass Sway and RW Sheet are not needed.

**How the user wants to work** (important):
1. **"Keep it working as now, but let me modify":** new ideas go into **option folders**, not into `active/`. Each option
   has `0 - current (installed)` or `0 - previous` to undo, a `readme.txt`, and usually a `lines changed.txt` for hand edits.
2. **Confirmed fixes may be installed by default.** The fog-noise fix and the Drizzle fixes were. Say so clearly and
   always provide the revert option.
3. **They want very clear "what and where" instructions:** which file, which folder (`lml/Vestigia/active/ess` or
   `active/str`), and which option folder.
4. **They like zips of just the relevant folder** (sent with SendUserFile) or a single link. The full branch zip is the
   fallback.
5. **They test in game and report back.** They respond well to **structured tests** (bisection) after several of
   the assistant's guesses were wrong. **Don't present guesses as fixes.** Label tests as tests.
6. They answer casually and sometimes ambiguously. Ask a short question when the meaning is unclear.
   - Example: "vertical" vs "horizontal" mist was corrected mid-task.
   - Example: "replace voxel noise" meant "remove the 2D look", not a new fog layer.
7. They don't want things removed without asking. They said "don't remove, just add 18". They were fine with removing
   the failed guess options 11–14 and test pack 98 afterwards.

**Unknown, so ask:** exactly which options they currently have copied onto their PC. Last known state:
- Option 15 fix installed (13 files).
- Option 16-1 (gentle wind) was on their Drizzle at one point, and possibly on other weathers.
- Option 20 (Drizzle `weather.xml`) installed.
- Option **21-1** (keeps Vestigia clouds) appears to be their Drizzle choice; they asked to soften it, which led to option 23.
- They may be testing 23-1 or 23-2.
- Option 19 (Rain fog 25% or 50%) unknown.

---

## 3. How LML and these mods load

- **LML `install.xml`:**
  - `<FileReplacement><GamePath>…</GamePath><FilePath>…</FilePath></FileReplacement>` replaces game files.
  - `<StreamingFiles>active/str</StreamingFiles>` streams a folder that `weather.xml` can reference via
    `ADDONDLC:/VESTIGIA/ACTIVE/STR/<name>`. This is how Vestigia adds new files (shower particles, custom sunny weathers).
  - `ResourceGroups` (`ess`, `wea`, `tem`, `det`) are Vestigia's modules.
- **Load order:** when two mods replace the same file, one wins. "Bottom of the list loads last and wins" comes from a
  community comment and is **unverified**. The design choice in this project was to **make duplicate files identical**,
  so load order doesn't matter: RPF files equal Vestigia's copies, and RW Grass Sway's `visualsettings.dat` equals
  Vestigia's. Or to use separate add-on folders that fail safe (Rain Sheets).
- **Vestigia `install.xml` references 15 files not in the repo:** snowheavy_* and blizzard(2)_*_ground particles,
  w_snow_odriscolls1, w_snow_pearson1, w_snowlight_pearson1, w_sunny, w_sunny_odriscols4, w_whiteout, w_whiteout_winter1.
  They are presumably on the user's PC (partial upload). The 4 thunder timecycles were also missing until the user
  uploaded them; they are now in `active/ess`.
- **RW (`RealisticWeather.asi`):** controls weather transitions, persistence, wind, gusts, debris and whirlwinds, and
  rain putting out fires. Its settings are in `RealisticWeather.ini` in the game folder, section `[RealisticWeather]`
  (created on first run), plus `Sauvy_ASI/RealisticWeatherTrainer/Persistence Presets/*.ini`. It overlaps with
  Vestigia's `wea` module (both affect weather pacing).

---

## 4. RDR2 file primer (as learned here)

### 4.1 `weather.xml` (`update:/common/data/levels/rdr3/weather.xml`)
- **`<WeatherGpuFx>`:** particle systems, each with `Name`, `SystemType` (`SYSTEM_TYPE_DROP`, `SYSTEM_TYPE_GROUND`,
  `SYSTEM_TYPE_SHEET`), textures (`rain`, `distortion_rain_n`, `rain_anim_td`, …), `driveType`, `windInfluence`,
  `gravity`, `particleStartThreshold`, `emitterSettingsName`, `renderSettingsName`.
  - **Gravity is set per weather here:** Drizzle -10, Rain -40, Thunder/Shower/Hurricane -70. This keeps each weather's
    fall speed even when the particle look is shared.
- **Weather types:** `Sun`, `Cloud`, `Wind*`, `Rain`, `Snow`, **`Fog` (the "Fog switch")**, `Humidity`, ripple/ocean
  settings, `DropSettingName` / `GroundSettingName` / **`SheetSettingName`** (`-` = none), `TimeCycleFilename`,
  `<Variations>` (story timecycles), `CloudSettingsName`, **`LocalizedDensityMap`** (the fog shape around the player).
- **Vanilla vs Vestigia, rainy weathers:**

  | Weather | Vanilla Fog / map | Vestigia (current) |
  |---|---|---|
  | DRIZZLE | 0 / RainDense | **0 / RainDense** (fixed, option 20) |
  | RAIN | 0 / Rain | 1 / Rain |
  | SHOWER | 0 / RainDense | 0 / RainDense |
  | THUNDER | 0 / Rain | 0 / RainDense |
  | THUNDERSTORM | 0 / Rain | 1 / Rain (sheet `-`; the add-on enables `THUNDER_SHEET`) |
  | HURRICANE | 0 / Rain | 1 / Rain |
  | HAIL / SLEET | 0 / default | 1 / none |

- **The vanilla `THUNDER_SHEET` item** (in the Rain Sheets add-on): `SYSTEM_TYPE_SHEET`, windInfluence 0.02, gravity -35,
  particleStartThreshold 0.3. Only THUNDERSTORM uses it in vanilla. Vanilla also has `BLIZZARD2_SHEET` for BLIZZARD,
  which Vestigia removed (snow; not done).

### 4.2 Weather particle files (`common:/data/levels/rdr3/weather/*.xml`)
Each rain type has 4 files (sometimes 6 with sheets):
- `*_render_drop`: look of falling drops
- `*_emitter_drop`: spawn and motion of drops
- `*_render_ground`: look of splashes
- `*_emitter_ground`: spawn of splashes

Key render settings:
- `textureRowsColsStartEnd`: the texture atlas grid. Vestigia's broken files had **0.1** here, which smeared the drops.
- `sizeMinMax`, `colour` (rgb plus alpha `w`).
- **`particleColorPercentage`:** the drop's own colour versus see-through refraction. RPF uses only 0.06, so drops are
  mostly refraction and are visible against bright sky but not against dark ground.
- `backgroundDistortion{VisibilityPercentage,AlphaBooster,Amount}` (refraction), `directionalAndAmbientMultiplier`
  (brightness), `translucency` / `wrapLightingTerm` (glow toward lights), `localLightsMultiplier` (lamps).
- `fadeNear_Far_Range`, `nearScale_Range`, `transitionFade` (blend between side and top-down sprite views),
  `dofAlphaOutputMultiplier`.

Key emitter settings:
- `boxCentreOffset` / `boxSize`: the spawn box that moves with the camera, 10×8×15 m for RPF rain.
- `lifeMinMax`, `velocityMin/Max`, `massMinMax`, wind multipliers, `noiseAmplitude*`.
- `sheetRadius/Interval/Burst` (sheets only).

`visualsettings.dat` → `rain.NumberParticles` (32768 in Vestigia, 16384 in vanilla) is the fixed particle budget.

### 4.3 Timecycle files (`update:/common/data/timecycle/w_*.xml`)
- **Layout:** `<cycle name=... regions="2">`, `<region name="GLOBAL">` (**wilderness**), then `<region name="URBAN">`
  (**towns**). There are **566 numeric keys per region**, each a single line of **13 time-of-day values**.
  **The two regions are independent.** Most fixes in this project were applied to GLOBAL only; Drizzle (option 21)
  covers both.
- Vestigia changes about **237 of the 566** keys per rainy timecycle compared with vanilla.
- **Story/variant timecycles** (`_finale1`, `_guama`, `_mp_pred`, `_nativeson3`, `_winter2` …) are sometimes left
  near-vanilla by Vestigia (`w_drizzle_finale1/1b`, `w_hurricane_guama`, `w_overcastdark_finale2`).
- **Custom Vestigia weathers** (SUNNYDENVER/LA/NO/NYC/SEATTLE) have their timecycles in `active/str` (streamed).
- See section 10 for the glossary of the keys that mattered.

### 4.4 Other files
- **`visualsettings.dat`:** about 2900 global graphics settings. The user's hand-merged version (Vestigia, RW grass sway
  and their own tuning) is installed in Vestigia **and** in RW Grass Sway (identical). Vestigia's official
  `visualsettings.dat` variants (TAA, motion blur, night brightness, pickup glow, grass) and the mightyelf TAA merge are
  full files based on Vestigia's original, so **copying them overwrites the user's merge**. Use the compatible
  options 03–07 instead, which are patched line by line.
- **`weatherGraph.xml`:** weather transition graph. `waitTimeMax` and `cost` are 100 in default, 400/200/50/25 in
  Vestigia's speed variants. **All of Vestigia's speed variants have a typo:** a second `SUNNY` node instead of
  `SUNNYSEATTLE`. The active file is correct; option 02 is built from the correct file.
- **`weatherclimates.xml`:** weather probabilities per region.

---

## 5. Chronological log, with the reasoning behind each step

### Phase 1: merge Rain Particles Fix into Vestigia (commit `c4eaa7b`)
- **Problem:** the two mods were inconsistent, and Shower drops looked odd.
- **Finding:** RPF replaces rainstorm, thunder, drizzle-drop and sleet-drop files (12 files). Vestigia references its
  **own copies** for SHOWER, HURRICANE, DRIZZLE_GROUND and SLEET_GROUND via `ADDONDLC:/VESTIGIA/ACTIVE/STR/...`. These
  are clones of Vestigia's old rainstorm/thunder files with broken values: texture grid 0.1, edgeSoftness 1000,
  localLights 1000, swapped velocity ±100. RPF never touched them, so Shower kept the broken look.
- **Done:**
  - The 12 RPF files were copied 1:1 into `active/ess`.
  - **Shower** was rebuilt from RPF rainstorm files.
  - **Hurricane** was rebuilt from RPF thunder files, keeping Vestigia's stronger wind: mass up to 2.8, positional wind
    ×5, gust ×2, angle variation 30.
  - **Drizzle ground** was rebuilt from RPF rainstorm ground at 50% splash size.
  - `drizzle_emitter_drop` and `drizzle_emitter_ground` were set to the RPF rainstorm versions, since Vestigia's were
    exact copies of its old rainstorm files.
  - **Gravity per weather stays in `weather.xml`.**
  - Backups are in `_backup_original_rain_files/`.
- **Result:** the user said "the shower weather looks good now".

### Phase 2: first "mist" fix and visualsettings (commits `86c9b52`, `23a21f8`)
- **The user reported:** a 2D mist effect in rain that pops in and out.
- **First hypothesis:** the ground-splash sprites. They had `transitionFade=false` (instant switch between side and
  top-down sprite views) and `backgroundDistortionAmount` 10000 (10× RPF's own thunder value).
  - **Done:** set `transitionFade=true` and distortion 1000 on the 5 rain ground renders. Kept installed.
  - **It did NOT fix the later "plane" problem**, which turned out to be fog (Phase 6).
- **`visualsettings.dat`:** RW Grass Sway's file is near-vanilla plus 9 `grass.Wind*` lines. Vestigia's is heavily
  tuned. The user provided their own hand-merged file, now installed in both mods.
  - The temperature colour correction keys in this file have **no effect**, because Vestigia sets
    `postfx_weather_color_correction` to 0 in all timecycles.

### Phase 3: optional Rain Sheets add-on (commits `6bf385a`, `2d04640`)
- **The user wanted the rain sheet / gust effect as an option.** Vestigia has `SheetSettingName` `-` everywhere, and no
  sheet particle item.
- **Done:** a separate LML folder with a copy of Vestigia's `weather.xml` plus the vanilla `THUNDER_SHEET` item, with
  THUNDERSTORM using it.
  - The first version guessed `SYSTEM_TYPE_DROP`. That was **wrong**. After the user supplied the vanilla `weather.xml`,
    it was corrected to the exact vanilla entry (`SYSTEM_TYPE_SHEET`).
- **Must stay in sync:** the add-on's `weather.xml` must always equal Vestigia's plus the sheet. Any `weather.xml` change
  must be applied to both. `tools/audit.py` checks this.

### Phase 4: rain visibility and blue haze (commits `cdbe28f`, `80e1079`)
- **Rain visibility:** too visible against sky and lights, too faint against the ground.
  - **Cause:** RPF drops are 94% refraction.
  - **Done:** raised the drops' own colour to 0.30, lowered refraction to 1.6 / 1.5, lowered translucency and wrap
    lighting, and lowered `localLights` to 1.0 and ambient to 0.5 / 0.8. Drizzle: own colour 0.75, translucency 0.5.
  - Presets are in option 01 (softer / balanced / stronger / pure RPF).
- **Blue haze even at 25 °C:** Vestigia's `local_atmosphere_fill_ambient_light_color` is deep blue (0.006, 0.005, 0.19)
  in almost every weather.
  - **Done:** moved it halfway toward grey in the rainy timecycles, **GLOBAL region only**: drizzle (+finale1/1b),
    rain, shower (+3), hurricane (+guama).
  - Not in sleet, hail or thunder (open item).

### Phase 5: options framework, and DLSS
- The `variants/00 - COMPATIBLE OPTIONS (use these)/` folder was created (commit `ea39b21`). Vestigia's official
  variants got `!! DO NOT USE` notes where they would undo fixes or overwrite the merged `visualsettings.dat`.
- **DLSS:** the user found that "strange rain" was mainly DLSS. It reconstructs thin transparent particles poorly,
  especially against flat sky. Advice given:
  - Without DLSS, try rain visibility 1 or 3, or option 08-2.
  - With DLSS, use DLAA, a higher quality mode, or a different preset or DLL.
  - With TAA, keep native resolution, lower Resolution Scale if needed, and consider Jester's TAA (option 03-2).

### Phase 6: THE 2D MIST PLANE HUNT (the main problem)

**Symptom (the user's words, refined over time):**
- A 2D "plane" of fog, vertical, about 10–20 m up, round or square, that moves with the player.
- It tries to mimic gusts of wind and rain.
- It is present from the moment a save loads.
- It appears in all rainy weathers: strongest in Shower, unnoticed in Hurricane, and also in Hail.
- Sometimes two at once.
- Vanilla has a similar effect, but bigger and much less noticeable.

**Hypotheses that were WRONG**, each built as an option and tested by the user. Kept here so nobody repeats them:

| # | Hypothesis | Why it seemed right | Result |
|---|---|---|---|
| 1 | Rain sheet (thunder sheet emitter is 10 m ahead, 10 m up, 5 m radius) | Matched "circular, 10–20 m up" exactly | It appears in all rainy weathers, but sheets only exist in Thunderstorm with the add-on |
| 2 | Ground-splash sprites (distortion ×100, depth-of-field ×36, spawn box 0–27 m ahead) | Matched "near the ground, moves with you" | Option 12; not the cause |
| 3 | Edge of the rain spawn box (10×8×15 m) seen through refraction | Matched "square that looks round" | Option 11; not the cause |
| 4 | RW `.asi` wind debris and whirlwinds (`SevereDebris*`, `Whirlwind*` in `RealisticWeather.ini`) | Strings in the `.asi` showed it spawns dust ptfx near the player | User disabled them; not the cause |
| 5 | `weather.xml` Fog switch = 1 in rainy weathers | Vanilla has 0 | Option 13; no effect **at that time**, because localized fog density was 0 in Vestigia's timecycles. **Later it did matter for Drizzle** (Phase 8). |
| 6 | Timecycle `no_rain` (patchy rain cells) | Hurricane 0 (no plane), Shower up to 0.8 (worst), a perfect correlation | Option 14; not the cause. The correlation was coincidental. |

**The systematic approach that worked:**
1. **Vanilla vs mods:** the user renamed `lml` → no plane. So it's an LML mod.
2. **Which mod:** only Vestigia was installed → the plane was there. So it's Vestigia.
3. **Which part of Vestigia** (troubleshooting pack 99): test `install.xml` files that each drop one group of
   `FileReplacement`s.
   - Test **A, without the 58 weather timecycle replacements → plane gone.** Particles, `visualsettings`,
     `timecycle_mods` and `det` were all ruled out.
   - Safe because the custom sunny weathers load their timecycles from `str`.
4. **Which timecycle settings:**
   - **First attempt, compared with Hurricane** (where it seemed absent). This was flawed: the user pointed out that
     Hurricane may have it too, hidden by its very thick fog (`local_atmosphere_fog_density` 0.031, about 9× Shower).
     Lesson: **masking**.
   - **Second attempt, compared with the vanilla timecycles** the user extracted. Groups of keys in all rainy
     timecycles were set back to vanilla (pack 98):
     - A: fog volumes. Plane still present.
     - **B: fog noise and localized fog. Fixed: "much much better, effect all around the player and field, more
       cinematic".**
     - C: fog shadows. Plane still present.
     - (D, rain haze, and E, all combined, were not needed.)
   - **Cross-check:** Hail was not in the test set and still had the plane. It had Vestigia's 0/2 noise (vanilla 0.5/0.6).
5. **Fix installed** (commit `f519b33`, option 15): the 11 keys in `tools/tc_lib.FOG_NOISE_FIX_KEYS` were set to each
   weather's own vanilla values, **GLOBAL region**, in drizzle, rain, shower (+finale2, guama, mp_pred), sleet, hail and
   hurricane. Then thunder, thunderstorm, thunderstorm_mp_pred and thunderstorm_nativeson3 were added (commit
   `d59d40a`) after the user uploaded Vestigia's copies; thunderstorm had noise 0/**3**.

**Why it caused a plane** (best understanding): the voxel noise sets how fog density varies inside the near-camera
volumetric fog grid. Vestigia's 0–2 range is extreme: it collapses the haze into one or two dense blobs with hard
edges, which read as flat 2D planes that follow the camera grid. Vanilla's narrow range (about 0.43–0.75) spreads it
evenly. Vestigia had also turned localized fog off (`density_mult` 0) and raised its wind from 1 to 5.

### Phase 7: fog look tuning on top of the fix (options 16–19)
- **16 wind-driven fog:** localized fog wind ×2/×3, voxel wind ×1.5/×2, large-scale wind ×1.5/×2. The strong version
  also widens the noise to ×1.4 (still far below 0–2).
- **17 volumetric-only:** sets `localized_fog_density_mult` (assumed to be a flatter layer) to 0 and adds its share to
  `..._raymarch`, plus fog density ×1.1 / ×1.4. **The user said this wasn't what they meant.** They wanted the 2D
  look gone, not a new layer. Key explanation given: **voxel noise is the pattern inside the volumetric fog, not a
  separate 2D effect.**
- **18 noise off:** `voxel_noise_min = max` (perfectly smooth fog, no visible drift), or a narrowed range of 30%.
- **19 rain fog 25% / 50% closer to vanilla** (Rain only): `local_atmosphere_fog_density`, `fog_height` and
  `fog_falloff` interpolated toward vanilla. Rain fog thickness is 6.8× vanilla installed, 5.4× at 25%, 3.9× at 50%.
  Each comes in no-wind, 16-1 and 16-2 versions.
- **Fog amounts, Vestigia versus vanilla** (daily average of `local_atmosphere_fog_density`):
  - Rain 6.8×, Shower 3.1×, Sleet 2.7×
  - Hail 13.5×, Hurricane 22.5×
  - Thunder 1.6×, Thunderstorm 1.6×
  - Drizzle 1.0×

### Phase 8: Drizzle still had the plane (options 20–23)
- **Why Drizzle was different:** after option 15 switched the game's localized fog back on, Drizzle's own Vestigia
  differences became visible:
  - `weather.xml` DRIZZLE has Fog = 1 and map `Rain` (vanilla: 0 and `RainDense`). Shower already matched vanilla.
  - Drizzle has the **strongest** vanilla localized fog (0.1–0.3, against Shower's 0.05–0.1).
  - Fog volumes are mist/dust/smoke = 1/1/1 (vanilla 0/0/0.1).
  - Fog falloff is 1000 (vanilla 500), with fog height down to 5 m.
  - The URBAN region was not fixed.
- **Option 20 (installed):** DRIZZLE Fog 1 → 0, map `Rain` → `RainDense`, in both Vestigia's `weather.xml` and the
  add-on's. The plane was still there.
- **Option 21 (21-2 installed):** **every fog-structure key of Drizzle set to vanilla, in GLOBAL and URBAN**, keeping
  Vestigia's colours and lighting (including the haze fix):
  - fog height and falloff
  - fog volumes
  - rain haze (`local_atmosphere_rain_threshold` / `_density_falloff`)
  - fog shadows
  - voxel noise and localized fog
  - all `*wind*` keys
  - `no_rain`
  - in 21-2, also all `local_atmosphere_cloud_*`

  The versions are 21-1 (without clouds), 21-2 (with clouds) and 21-3 (full vanilla `w_drizzle.xml`, the guaranteed
  fallback).
  - **Result:** "not a single plane but multiple around the field and player, which is better". This is the vanilla
    behaviour. **The user prefers 21-1** (keeps Vestigia clouds).
- **Most likely source of the remaining patches:** vanilla **rain haze**, `local_atmosphere_rain_threshold` (0.2–0.5)
  and `_density_falloff` (0.005–0.01). It is active at only 4 of the 13 time columns in vanilla Drizzle. Vestigia had
  it at 0/0, which is probably off.
  - **Option 22** (built on 21-2): weaker rain haze (threshold halfway to 1) or none.
  - **Option 23** (built on **21-1**): a bit softer (noise range ×0.6, threshold +25%), much softer (noise ×0.3,
    threshold +50%, fog density ×1.15), or rain haze off (a diagnostic).
  - **Waiting for the user's feedback on 23.**

### Phase 9: consistency audit
`tools/audit.py` checks that:
- all XML parses,
- the fog-noise fix is present in all 13 rainy timecycles,
- the add-on `weather.xml` is in sync with Vestigia's,
- particle pairs are identical (Shower = Rain, Hurricane = Thunder for look),
- `visualsettings` is identical in both mods,
- every option's "current/installed" copy equals the installed file.

All of those pass. The open items it reports are listed in section 8.

---

## 6. Current installed state, exactly

| Area | State |
|---|---|
| Rain particles | RPF-based. Shower = rainstorm, Hurricane = thunder (+ wind), Drizzle ground = rainstorm at 50% size. Ground splashes: `transitionFade` true, distortion amount 1000 (AlphaBooster still 100, depth-of-field ×36 on rain/shower/drizzle). |
| Drop visibility | "Balanced": own colour 0.30 (drizzle 0.75), ambient 0.5 (rain/shower) / 0.8 (thunder/hurricane) / 0.85 (drizzle), refraction 1.6 / 1.5, translucency 0.2 / 0.3 / 0.5 |
| Fog-noise fix (option 15) | 13 rainy timecycles, GLOBAL region. **Drizzle: whole fog structure vanilla in both regions (21-2).** |
| Haze colour fix | GLOBAL fill ambient halfway to grey in drizzle (+finale1/1b), rain, shower (+3), hurricane (+guama) |
| `weather.xml` | Vestigia's plus DRIZZLE vanilla Fog/map. RAIN, THUNDERSTORM, HURRICANE, HAIL and SLEET still Fog = 1. |
| Rain Sheets add-on | In sync with Vestigia's `weather.xml` plus `THUNDER_SHEET` |
| `visualsettings.dat` | The user's merged file, identical in Vestigia and RW Grass Sway |
| `weatherGraph` | Default Vestigia (wait 100), with the correct SUNNYSEATTLE node |

---

## 7. Options catalogue (`Vestigia/variants/00 - COMPATIBLE OPTIONS (use these)/`)

| # | Name | Files | Notes |
|---|---|---|---|
| 01 | rain visibility | 5 `*_render_drop` | 0 balanced* / 1 softer / 2 stronger / 3 pure RPF |
| 02 | weather speed (typo fixed) | `weatherGraph.xml` → `wea` | 0 default* (100) / 400 / 200 / 50 / 25 |
| 03–07 | TAA / motion blur / night brightness / pickup glow / grass texturing | `visualsettings.dat` | Patched onto the user's merged file. Each has `lines changed.txt`. Combine by hand-editing. Night brightness overrides 2 star values the user tuned. |
| 08 | rain particles (full set) | 23 particle files | 0 current* / 1 original combine (no later tweaks, no mist fix) / 2 RPF look + all fixes (no visibility tweaks) |
| 09 | drizzle visibility | `drizzle_render_drop` | brighter Drizzle, same size and amount |
| 10 | heavy rain light glow | 4 render_drop | less glow toward lights |
| 15 | fog noise (MIST PLANE FIX) | rain/fog `w_*.xml` | 0 previous / 1 rainy weathers* / 2 all weathers (46 files) |
| 16 | wind-driven fog | 12 rain timecycles (no drizzle) | 1 gentle / 2 strong + wisps |
| 17 | volumetric-only fog | 12 (no drizzle) | A / B thicker / C + wind. The user said it wasn't what they wanted; kept anyway. |
| 18 | fog noise off (smooth volumetric) | 12 (no drizzle) | 1 noise off / 2 very faint |
| 19 | rain fog closer to vanilla (25% or 50%) | `w_rain.xml` | 6 versions (25/50 × no-wind/16-1/16-2) |
| 20 | drizzle fog plane fix (`weather.xml`) | `weather.xml` (+ add-on copy) | 1 installed* / 0 previous |
| 21 | drizzle fog structure like vanilla | `w_drizzle.xml` | 1 keeps Vestigia clouds (**the user's choice**) / 2 + clouds* / 3 full vanilla / 0 previous |
| 22 | drizzle rain haze (patches) | `w_drizzle.xml` (on 21-2) | weaker / none |
| 23 | drizzle patches softer (for 21-1) | `w_drizzle.xml` (on 21-1) | a bit softer / much softer / rain haze off. **Waiting for feedback.** |
| 24 | drizzle fog closer to shower | `w_drizzle.xml` (on 21-1 / 23-1 / 23-2) | fog amount (density, height, falloff, localized, raymarch, rain haze) 50% or 100% toward Shower; shape untouched |
| 99 | TROUBLESHOOTING | test `install.xml` files | A no weather timecycles / B no timecycle_mods / C no particles / D no visualsettings / E no det |

\* = installed.

**Options that change the same files and must not be stacked blindly:**
- 15, 16, 17, 18 and 19 (timecycles). 19 has versions with 16 built in.
- 21, 22 and 23 (Drizzle).
- 01, 08, 09 and 10 (particles; apply 09/10 by hand after 01/08).

**Removed** (failed guesses, or superseded by 15): 11 rain spawn area, 12 ground splash, 13 rain Fog switch, 14 `no_rain`,
and timecycle test pack 98. They can be recovered from git history (before commit `f519b33`).

---

## 8. Open issues and suggested next steps (prioritised)

1. **Feedback pending on options 23 and 24.** The user said Drizzle was still too foggy and wanted it closer to Shower, which led to option 24.
   Original item: **feedback pending on option 23** (Drizzle patches softer on 21-1). If the user picks one, consider installing it as
   the default for Drizzle, or making an in-between version.
2. **The town (URBAN) region of the other 12 rainy timecycles still has Vestigia fog noise** (for example 0/0.5 against
   vanilla 0.5/0.6). The plane may appear in towns. Fix by applying `FOG_NOISE_FIX_KEYS` to URBAN too, ideally as an
   option first.
3. **Fog switch = 1** in `weather.xml` for RAIN, THUNDERSTORM, HURRICANE, HAIL and SLEET (vanilla 0). HAIL and SLEET
   also have no LocalizedDensityMap (vanilla `default`), and THUNDER uses `RainDense` (vanilla `Rain`). This is the same
   kind of issue that affected Drizzle, so if a plane shows in those weathers, apply the option 20 change there.
   **Always update the Rain Sheets add-on copy too.**
4. **The haze colour fix is missing** in sleet, hail, thunder and thunderstorm (+2 variants), which keep the deep-blue
   haze. Add it for consistency (50% toward the per-column grey average, GLOBAL).
5. Some semantics are still **inferred**: is `localized_fog_density_mult` a flat layer? Does rain_threshold 0/0 mean off?
   Treat them as hypotheses and test.
6. Possibly Blizzard's `BLIZZARD2_SHEET` (removed by Vestigia) as an optional add-on. The user hasn't asked for it.
7. Rampage trainer weather switching was inconsistent with Vestigia's timecycles (mostly right after loading a save).
   Likely RW `.asi` ownership/persistence plus slow transitions. Not investigated further.
8. The 15 files referenced by `install.xml` but missing from the repo (see section 3). Ask the user to upload them if
   they're needed.

---

## 9. Methodology and lessons (read this before debugging anything visual)

- **Bisect, don't guess.** Six plausible guesses failed; the bisection (mods → modules → files → key groups) found the
  cause in four test rounds. Build tests as **swap-in files plus the original to restore**, and tell the user to test
  one at a time.
- **Compare against vanilla, not against another weather.** Comparing with Hurricane was misleading because its thick
  fog masked the effect.
- **A fix can switch a dormant system back on.** Restoring vanilla localized fog exposed Drizzle's Vestigia
  `weather.xml` settings, which had been invisible because Vestigia's timecycle density was 0. When something new
  appears after a fix, look at settings that only became active because of it.
- **Check both timecycle regions** (GLOBAL and URBAN) and the story variants.
- **Correlation is not causation:** `no_rain` matched the symptom perfectly and still wasn't the cause.
- **Keep duplicated files identical** (Vestigia and RPF, Vestigia and RW Grass Sway, Vestigia and the add-on's
  `weather.xml`) so load order never matters, and run `tools/audit.py` after every change.
- **Communicate uncertainty:** say what is inferred from key names, and label tests as tests.

---

## 10. Glossary: timecycle keys that mattered (confidence in brackets)

| Key | Meaning | Vestigia → vanilla (Shower) |
|---|---|---|
| `local_atmosphere_voxel_noise_min/max` | Remap range of the 3D noise modulating near-camera volumetric fog density. **Too wide gives 2D blobs.** (high: confirmed by test) | 0/2 → 0.428/0.747 |
| `local_atmosphere_voxel_noise_scale_mult_z` | Vertical stretch of the noise (med) | 1.5 → 1 |
| `local_atmosphere_voxel_detail_wind_vertical_speed` | Vertical scroll of the fog detail (med) | -20 → -5 |
| `local_atmosphere_localized_fog_density_mult` | Localized (player-centred, density-map driven) fog amount; possibly the non-raymarched part (low–med) | 0 → 0.05–0.1 |
| `local_atmosphere_localized_fog_density_mult_raymarch` | The same fog, raymarched near the camera (med) | 0.01–0.1 → 0.3–0.5 |
| `local_atmosphere_localized_fog_noise_bounds_x/y`, `_wind_velocity`, `_height_offset` | Patchiness, drift and offset of the localized fog (med) | wind 5 → 1 |
| `local_atmosphere_fog_density` / `_height` / `_falloff` | Overall volumetric fog amount, height and thinning with altitude (high) | Rain 0.0059 / 1000 / 1000 against vanilla 0.00087 / ~460 / ~540 |
| `local_atmosphere_rain_threshold` / `_density_falloff` | Rain haze in the air; 0/0 probably off (low–med) | Drizzle vanilla 0–0.5 / 0–0.01 at 4 of 13 times |
| `local_atmosphere_fog_volume_{mist,dust,smoke,pollution,waterfall}_density_mult` | Strength of placed fog volumes (box/ellipsoid) (high) | Vestigia 1/1/1/0/5 against Shower vanilla 0.15/0/0.1/0.2/1 |
| `fog_shadow_amount`, `local_atmosphere_fog_shadow_amount`, `fog_shadow_falloff` | Shadows inside fog, computed within a limited range (med) | Shower 0.9 / 0.9 / 100 against vanilla 0 / 0.24–0.7 / 236–1000 |
| `no_rain` | Fraction of rain-free area (patchy rain) (med); NOT the plane | Shower 0–0.8, vanilla 0 |
| `local_atmosphere_fill_ambient_light_color_r/g/b` | Colour of ambient fill light in fog: the haze colour (high) | Vestigia deep blue (0.006, 0.005, 0.19) |
| `postfx_weather_color_correction` | Strength of the temperature/humidity colour grading from `visualsettings.dat` (high) | Vestigia 0 everywhere, so temperature tint is off |
| `local_atmosphere_cloud_*` | Volumetric cloud layer shape/noise/height/shadow (high) | Changed in 21-2 for Drizzle only |

---

## 11. Technical notes and pitfalls

- **Line endings and encoding:** almost all files are **CRLF**. Some timecycles (`w_thunder.xml`, `w_thunderstorm.xml`,
  `w_drizzle.xml` from the user) are **UTF-8 with BOM**. Read and write with `encoding='utf-8', newline=''` in Python.
  `sed` substitutions keep CRLF as long as the pattern doesn't touch line ends.
- **Paths contain spaces and parentheses** (`00 - COMPATIBLE OPTIONS (use these)`). Quote everything in shell.
  - URL-encode for GitHub raw links: `https://github.com/DiligentCube007/RDR2-MODS-Claude-Knoladge-/raw/claude/great-clarke-0hc562/<url-encoded path>`.
  - GitHub can't zip a subfolder, so send zips with SendUserFile, or commit a small zip and give its raw link (as was
    done for `thunder fix (4 files).zip` in option 15).
- **The `rm` safety check** blocks `rm "$VAR"/*`. Use literal paths or `"${VAR:?}"`.
- **Viewing `.jxr` HDR screenshots:** create a venv, `pip install imagecodecs numpy pillow`,
  `imagecodecs.jpegxr_decode(...)`, then tone-map: scale by 0.18/median luminance, Reinhard, sRGB gamma. Save PNGs in
  the scratchpad, crop with ImageMagick `convert -crop`, and view with the Read tool.
- **How options were built:** a Python script per option (in the session scratchpad, now gone). The pattern:
  1. Copy the installed files to `0 - current (installed)`.
  2. Generate the modified files with `tools/tc_lib.py` functions (`regions`, `get`, `put`, `to_vanilla`).
  3. Validate with `xml.etree.ElementTree.parse`.
  4. Write `readme.txt` and `lines changed.txt` (CRLF).
  5. Add a row to `variants/README.md`.
  6. Verify with `diff | grep -c '^>'` that only the intended lines changed.
  7. Commit, push, zip the option folder and send it.
- **Commits:** end with the Co-Authored-By / Claude-Session lines given by the harness. Push with
  `git push -u origin claude/great-clarke-0hc562`. Don't create PRs unless asked.
- **The user's uploads** arrive as files under `/root/.claude/uploads/<session>/`, or are committed via GitHub web
  ("Add files via upload"), so run `git pull` before working.

---

## 12. Quick start for the next session

1. `git checkout claude/great-clarke-0hc562 && git pull origin claude/great-clarke-0hc562`
2. Read this file and `Vestigia/variants/README.md`.
3. Run `python3 tools/audit.py`.
4. Ask the user:
   - Which options are copied onto their PC right now (especially 16, 19, 21-1/21-2, 22/23, Rain Sheets add-on)?
   - What was the result of option 23?
5. Continue with section 8.
