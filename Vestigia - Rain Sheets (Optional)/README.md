# Vestigia - Rain Sheets (Optional)

Turns on the **wind-blown rain sheet / gust effect** in **Thunderstorm** and **Hurricane**.
Vestigia switches it off by default.

- **ON:** put this folder in `lml/` and make sure it loads **after (below) Vestigia** in the LML load order.
- **OFF:** remove or disable this folder.

Sheets use Vestigia's sheet particle files (the Rain Particles Fix versions in `Vestigia/active/ess/`).
If you prefer RW's sheet look, also enable `Sauvy - RW Sheet` and load it after Vestigia.

This `weather.xml` is a copy of Vestigia's with only 3 changes: a new `THUNDER_SHEET` particle entry,
and `SheetSettingName` set to it for THUNDERSTORM and HURRICANE. If you ever edit Vestigia's
`weather.xml`, copy the change here too.

Note: no vanilla `weather.xml` was available, so the `THUNDER_SHEET` entry was rebuilt from Vestigia's
`THUNDER_DROP` entry. If the game misbehaves with this enabled, remove the folder (that fully undoes it).
