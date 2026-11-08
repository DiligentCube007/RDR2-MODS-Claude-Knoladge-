# Vestigia - Rain Sheets (Optional)

Turns on the **wind-blown rain sheet / gust effect** in **Thunderstorm**, the same as the vanilla game.
Vestigia switches it off by default.

- **ON:** put this folder in `lml/` and make sure it loads **after (below) Vestigia** in the LML load order.
- **OFF:** remove or disable this folder.

Sheets use Vestigia's sheet particle files (the Rain Particles Fix versions in `Vestigia/active/ess/`).
If you prefer RW's sheet look, also enable `Sauvy - RW Sheet` and load it after Vestigia.

This `weather.xml` is a copy of Vestigia's with only 2 changes: the vanilla `THUNDER_SHEET` particle entry
(copied exactly from the game's original `weather.xml`), and `SheetSettingName` set to it for THUNDERSTORM,
as in vanilla. If you ever edit Vestigia's
`weather.xml`, copy the change here too.

Vanilla values: `SYSTEM_TYPE_SHEET`, wind influence 0.02, gravity -35, start threshold 0.3 (sheets only
appear once the rain is heavy enough). Remove the folder to fully undo it.
