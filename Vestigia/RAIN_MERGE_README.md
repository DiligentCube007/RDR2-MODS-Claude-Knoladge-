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
