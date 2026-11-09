# CLAUDE.md

This repo holds the user's RDR2 mod setup: Vestigia, with Rain Particles Fix merged in, plus Realistic Weather. A long
debugging and tuning project was done on branch `claude/great-clarke-0hc562`.

**Read `HANDOFF.md` first.** It covers the full history, the reasoning behind each change, the current state, the open
issues and the user's preferences.

Key rules:
- Develop on `claude/great-clarke-0hc562`. Run `git pull` first, because the user uploads files via the GitHub web UI.
- New changes go into option folders under `Vestigia/variants/00 - COMPATIBLE OPTIONS (use these)/`. Each has a
  `0 - current (installed)` copy, a `readme.txt` and a `lines changed.txt`. Only change `Vestigia/active/` for
  confirmed fixes, and say so.
- Timecycle files have 2 independent regions (GLOBAL = wilderness, URBAN = towns), each with 13 time columns.
  Vanilla references are in `Vestigia/timecycle vanila/` and `Vestigia/vanilla reference/weather.xml`.
- Any `weather.xml` change must also go into `Vestigia - Rain Sheets (Optional)/weather.xml`.
- Run `python3 tools/audit.py` after changes. Helpers for editing timecycles are in `tools/tc_lib.py`.
- Files are CRLF, and some are UTF-8 with BOM. Keep both.
- Debug visual problems by bisecting and comparing against vanilla, not by guessing (see HANDOFF section 9).
