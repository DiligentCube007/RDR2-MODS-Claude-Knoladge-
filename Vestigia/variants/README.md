# Vestigia variants - start here

**Your download works as-is.** Nothing in this folder is loaded by the game. Everything here is an optional
file you can copy into `Vestigia/active/...` to change one thing.

## How to use any option
1. Open the option's category folder and read its `readme.txt`.
2. Pick **one** option folder and copy its file(s) into the `active` subfolder named in the readme
   (`ess`, `str`, `wea` or `tem`), replacing the file there.
3. To undo, copy the `0 - ...` option back. It's identical to what's installed now.

## `00 - COMPATIBLE OPTIONS (use these)`: made for your current setup
| Folder | What it changes | File | Copy to |
|---|---|---|---|
| 01 - rain visibility | How solid the falling rain looks (softer / balanced* / stronger / pure Rain Particles Fix) | 5 `*_render_drop.xml` | `active/ess` + `active/str` |
| 02 - weather speed (typo fixed) | How long each weather lasts (slowest 4x ... default* ... fastest) | `weatherGraph.xml` | `active/wea` |
| 03 - anti-aliasing (TAA) | Game TAA: current* / legacy / Jester's (sharper, less smearing) | `visualsettings.dat` | `active/ess` |
| 04 - motion blur | current* / high / none | `visualsettings.dat` | `active/ess` |
| 05 - night brightness | current* / dark / very dark / pitch black | `visualsettings.dat` | `active/ess` |
| 06 - pickup glow | current* / disabled | `visualsettings.dat` | `active/ess` |
| 07 - grass texturing | current* / vanilla grass | `visualsettings.dat` | `active/ess` |
| 08 - rain particles (full set) | current* / Rain Particles Fix look + all fixes / original combine (no later tweaks) | 23 rain particle files | `active/ess` + `active/str` |
| 09 - drizzle visibility | current* / more visible (same size and amount) | `drizzle_render_drop.xml` | `active/ess` |
| 10 - heavy rain light glow | current* / less glow toward sun and lamps (Rain, Shower, Thunderstorm, Hurricane) | 4 `*_render_drop.xml` | `active/ess` + `active/str` |
| 11 - rain spawn area (mist test) | current* / larger spawn area (TEST for the vertical mist plane) | 4 `*_emitter_drop.xml` | `active/ess` + `active/str` |
| 12 - ground splash mist (test + fix) | current* / splashes OFF (test) / splashes subtle (fix) | 5 `*_render_ground.xml` | `active/ess` + `active/str` |
| **13 - rain fog (mist plane fix)** | current* / rain fog switch off (vanilla) / + vanilla fog shapes | `weather.xml` | `active/ess` (+ Rain Sheets add-on folder if installed) |
| **14 - rain coverage (MIST PLANE FIX)** | current* / full coverage (recommended) / reduced patchiness | 7 rain `w_*.xml` timecycles | `active/ess` |
| **98 - TROUBLESHOOTING 2 - which timecycle setting (vs vanilla)** | 5 test sets that each put one group of rain timecycle settings back to vanilla | 7 rain `w_*.xml` | `active/ess` (put '0 - current' back after) |
| **99 - TROUBLESHOOTING - find the mist plane** | test install.xml files that switch off one part of Vestigia at a time | `install.xml` | `lml/Vestigia/` (put the original back after) |

\* = installed now.

All `visualsettings.dat` options are **your merged file** (Vestigia + RW grass sway + your tuning) with only
that option's lines changed. They all replace the same file, so to **combine** two (for example TAA and
motion blur), copy one, then edit the lines listed in the other's `lines changed.txt` with Notepad.

Options 01, 08, 09 and 10 share some files. If you combine them, copy 01 or 08 first,
then apply 09 and 10 by hand with their `lines changed.txt` (exact old and new values listed).

## Other folders: Vestigia's own original variants
Kept for reference. Folders with a `!! DO NOT USE` note would undo the fixes or overwrite your merged
`visualsettings.dat`. Use the matching compatible option instead.
Still fine to use as they are: `level of detail`, `temperature settings`, `remove extra weathers`.

## Rain and DLSS
Thin, see-through rain streaks are hard for DLSS. It rebuilds the image from a lower resolution using
previous frames, and rain gives it little motion data, so streaks get smeared or faded, most visibly
against bright sky. If rain looks strange:
- **Without DLSS:** try rain visibility `1 - softer` or `3 - pure Rain Particles Fix`. The default was tuned with DLSS on.
- **With DLSS:** try **DLAA** (full resolution), a higher quality mode, or another DLSS preset or version
  (NVIDIA app DLSS override, DLSSTweaks, or an older DLL in DLSS Swapper).
- **With the game's TAA:** try `03 - anti-aliasing (TAA)/2 - jester's taa`.
