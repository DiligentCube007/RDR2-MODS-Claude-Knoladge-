# Vestigia + Rain Particles Fix: merged rain

All rain in Vestigia now uses the **Rain Particles Fix** (RPF) look. Everything else in Vestigia
(timecycles, snow, fog, weather system, temperatures) is untouched.

## Why the Shower weather looked odd

Each rain type in RDR2 uses 4 particle files:

| File            | Controls                                                        |
|-----------------|-----------------------------------------------------------------|
| `*_render_drop`   | **Look** of falling drops (texture, size, light, transparency)  |
| `*_emitter_drop`  | **Spawning/motion** of falling drops (spawn box, life, mass, wind)    |
| `*_render_ground` | **Look** of splashes on the ground                              |
| `*_emitter_ground`| **Spawning** of splashes                                        |

`weather.xml` connects each weather to its files and also sets that weather's **gravity**
(fall speed): Drizzle -10, Rain -40, Thunderstorm / Shower / Hurricane -70.

RPF fixes only **Rain (rainstorm)**, **Thunderstorm**, **Drizzle drops** and **Sleet drops**.
Vestigia's **Shower**, **Hurricane** and **Drizzle splashes** use their own copies in
`active/str/`. RPF never touches those copies, so they kept Vestigia's old broken settings:

* `textureRowsColsStartEnd = 0.1` (invalid texture grid, which makes drops look smeared or blocky)
* `localLightsMultiplier = 1000`, `edgeSoftness = 1000`, `particleColorPercentage = 1.0` (drops look
  too bright and solid grey)
* emitter `velocityMin = +100 / velocityMax = -100` (min and max swapped) and `bounciness = 10`

As a result, Rain used one look and Shower used another.

## What was changed

### A) Copied 1:1 from Rain Particles Fix (into `active/ess/`)
`drizzle_render_drop`, `rainstorm_render_drop`, `rainstorm_emitter_drop`, `rainstorm_render_ground`,
`rainstorm_emitter_ground`, `sleet_render_drop`, `thunder_render_drop`, `thunder_emitter_drop`,
`thunder_render_ground`, `thunder_emitter_ground`, `thunder_render_sheet`, `thunder_emitter_sheet`

### B) Vestigia-only files rebuilt from RPF (new files that RPF itself doesn't have)
| Vestigia file                      | Built from (RPF)            | Weather-specific part kept                          |
|------------------------------------|-----------------------------|-----------------------------------------------------|
| `str/shower_render_drop`           | `rainstorm_render_drop`     | none (look only)                                    |
| `str/shower_emitter_drop`          | `rainstorm_emitter_drop`    | Vestigia's original was an exact copy of rainstorm  |
| `str/shower_render_ground`         | `rainstorm_render_ground`   | none (look only)                                    |
| `str/shower_emitter_ground`        | `rainstorm_emitter_ground`  | none                                                |
| `str/hurricane_render_drop`        | `thunder_render_drop`       | none (look only)                                    |
| `str/hurricane_emitter_drop`       | `thunder_emitter_drop`      | stronger wind: mass 1.4–2.8, positional wind ×5, gusts ×2, angle variation 30 |
| `str/hurricane_render_ground`      | `thunder_render_ground`     | none (look only)                                    |
| `str/hurricane_emitter_ground`     | `thunder_emitter_ground`    | none                                                |
| `str/drizzle_render_ground`        | `rainstorm_render_ground`   | splashes at 50% size (Vestigia's drizzle ratio)     |
| `str/drizzle_emitter_ground`       | `rainstorm_emitter_ground`  | Vestigia's original was an exact copy of rainstorm  |
| `ess/drizzle_emitter_drop`         | `rainstorm_emitter_drop`    | Vestigia's original was an exact copy of rainstorm  |

**Per-weather fall speed is kept.** Gravity comes from Vestigia's `weather.xml`, which was not
changed, so Drizzle still falls slower than Rain and Shower/Thunder/Hurricane still fall hardest.

### Not touched (not rain)
Hail, Sleet emitter and Sleet ground (ice texture), all Snow and Blizzard files, Underwater.

## Install / load order
* Copy the `Vestigia` folder into `lml/` as usual.
* **Rain Particles Fix is now built into Vestigia**, so you can disable or remove it. If you keep it,
  load order doesn't matter, because both mods now contain identical rain files.
* *Realistic Weather* "RW Sheet" also replaces `thunder_render_sheet.xml`. If you want RW's version,
  put it above Vestigia in load order. Vestigia's own `weather.xml` disables sheets (`-`) anyway.

## Undo
The original files are in `_backup_original_rain_files/` (same `ess/` and `str/` layout). Copy them
back into `active/` to undo the change. LML ignores this folder.

---

# Update 2: rain "mist" popping + RW grass sway merge

## Rain ground "mist" that pops in and out
The misty layer near the ground in rain comes from the **ground-splash particles**
(`*_render_ground`). They are flat 2D animated splash sprites, and they also bend the image
behind them (refraction). Two settings made them pop:

| Setting | Before | After | Why |
|---|---|---|---|
| `transitionFade` | false | **true** | The sprites switch between "seen from the side" and "seen from above" as the camera tilts. With this off, the switch happens instantly and looks like a pop. |
| `backgroundDistortionAmount` | 10000 | **1000** | 10× stronger than Rain Particles Fix's own thunder splashes, so each splash looked like a hazy smear. 1000 matches thunder and vanilla. |

Changed in: `ess/rainstorm_render_ground`, `ess/thunder_render_ground`, `str/shower_render_ground`,
`str/hurricane_render_ground` and `str/drizzle_render_ground`. Thunder and hurricane already used 1000,
so only the fade changed in those two. The previous versions are in `_backup_original_rain_files/pre_mist_fix/`.

**Disable the separate Rain Particles Fix mod now.** Vestigia's splash files are now improved
versions, so the separate mod would undo this fix if it loads after Vestigia.

## visualsettings.dat (RW Grass Sway + Vestigia)
`visualsettings.dat` is the game's global graphics-tuning file, with about 2900 settings: tonemapping,
stars, shadows, puddles, rain particle count, wetness, grass, motion blur and more.

* **Vestigia's** copy is heavily tuned: tonemapping, stars, soft shadows, puddles, and 32768 rain particles.
* **RW Grass Sway's** copy is an almost unchanged vanilla file. Its only real change is the 9
  `grass.Wind*` lines, which make grass react gently to RW's wind.

Replacing one file with the other loses either all of Vestigia's tuning or RW's grass sway.
Both mods now use **your hand-tuned merged file**. It has Vestigia's settings plus RW's 9 grass-wind lines
and RW's fog-volume wind lines, and blended values for drying speed, stars, the sky far clip, puddle ripples,
dirt wash, snow melt, vehicle drying and temperature colour correction. The same file is in Vestigia and
RW Grass Sway, so load order doesn't matter. The originals are in `_backup_original_rain_files/`.

---

# Update 3: rain visibility + rain haze colour

## Rain too visible toward the sky or lights, too faint against the ground
The Rain Particles Fix drops were drawn as 6% their own colour and 94% "bending the background"
(refraction). Bent background only shows where there's brightness behind the drop, like sky or lamps.
A translucency/wrap-lighting glow also made drops light up when you face a light source.

| Setting | Rain / Shower | Thunderstorm / Hurricane | Drizzle |
|---|---|---|---|
| `particleColorPercentage` (drop's own colour) | 0.06 → **0.20** | 0.06 → **0.20** | 0.70 (unchanged) |
| `backgroundDistortionVisibilityPercentage` / `AlphaBooster` | 2.4 → **1.6** | 2.2 → **1.5** | unchanged |
| `translucency` (glow toward lights) | 0.3 → **0.2** | 0.5 → **0.3** | 0.9 → **0.5** |
| `wrapLightingTerm` | unchanged | 0.5 → **0.3** | unchanged |
| `localLightsMultiplier` | 1.2 → **1.0** | 1.2 → **1.0** | unchanged |

## Haze looks too blue in rain (even at 25 °C)
Vestigia's timecycles set the haze/fog fill light (`local_atmosphere_fill_ambient_light_color`) to a deep blue
(0.006, 0.005, 0.19) for almost every weather. Temperature can't warm it, because Vestigia sets
`postfx_weather_color_correction` to 0 in every timecycle. That also means the
`WeatherColorCorrection.Temperature` values in `visualsettings.dat` currently have no effect.

For the **rainy weathers only** (Drizzle, Rain, Shower and Hurricane, including their story variants),
the haze fill colour is now **50% less blue** (moved halfway toward neutral grey), in the GLOBAL region.
The URBAN region was already neutral. At noon it goes from 0.006/0.005/0.188 to 0.036/0.035/0.127. Clear,
cloudy, foggy and snowy weathers keep Vestigia's look, so the haze warms up gradually as the weather turns rainy.

The previous versions of all these files are in `_backup_original_rain_files/pre_visibility_and_haze/`.

---

# Update 4: rain balance between sky and ground
The drops were lit to about the same brightness as an overcast sky, so they disappeared against the clouds
but stood out against the darker ground. Drops now have more of their own colour and are a little darker
than the sky, so they read about the same everywhere. Three presets are in `variants/rain visibility/`
("1 - softer (previous)", "0 - default (balanced)" which is installed, and "2 - stronger").

| | Rain / Shower | Thunderstorm / Hurricane | Drizzle |
|---|---|---|---|
| `particleColorPercentage` | 0.20 → **0.30** | 0.20 → **0.30** | 0.70 → **0.75** |
| `directionalAndAmbientMultiplier` | 0.6 → **0.5** | 1.0 → **0.8** | 1.0 → **0.85** |

---

# Update 5: the 2D "mist plane" is fixed (fog noise)
The moving 2D mist plane that followed you in rainy weather came from Vestigia's **local-atmosphere fog noise**,
not from the rain particles. Vestigia sets `local_atmosphere_voxel_noise_min/max` to **0 / 2** in almost every
weather (vanilla is about 0.43 / 0.75). It also makes the vertical noise move faster, raises the localized fog
wind from 1 to 5, and turns localized fog off. The very wide noise range squeezes the near-camera haze into a
few dense, sharp-edged blobs. We found it by testing against the vanilla timecycles.

**Installed:** these 11 settings now use each weather's own vanilla values in Drizzle, Rain, Shower (and its
3 story variants), Sleet, Hail and Hurricane. The result is even, all-around rain haze. Everything else in
Vestigia is unchanged. Options are in `variants/00 - COMPATIBLE OPTIONS (use these)/15 - fog noise (MIST PLANE FIX)`:
previous, rainy weathers (installed), all weathers. There are also hand-edit instructions for Thunder and Thunderstorm.

# Update 6: drizzle fog plane
After the fog-noise fix switched the game's localized fog back on, Drizzle still showed the plane. Vestigia's
`weather.xml` gives DRIZZLE the Fog switch on (1) and the `localized_density_map_Rain` fog shape. Vanilla uses
Fog 0 and `RainDense`, which Shower already matched. **Installed:** DRIZZLE now uses the vanilla values, in both
`active/ess/weather.xml` and the Rain Sheets add-on's `weather.xml` (option 20 has the revert).
