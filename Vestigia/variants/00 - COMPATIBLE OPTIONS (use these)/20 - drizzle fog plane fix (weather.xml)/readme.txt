DRIZZLE FOG PLANE FIX (weather.xml)

After the fog noise fix (option 15) brought the game's localized fog back, Drizzle still showed the 2D
plane because Vestigia's weather.xml gives DRIZZLE the Fog switch ON (<Fog value="1.000000"/>) and a
different fog shape (localized_density_map_Rain). Vanilla Drizzle: Fog 0 + localized_density_map_RainDense.
Shower already uses the vanilla values - that's why Shower is fine after option 15.

1 - drizzle like vanilla (INSTALLED)   DRIZZLE: Fog 1 -> 0, LocalizedDensityMap Rain -> RainDense
0 - previous (Vestigia drizzle)         undo

HOW: each option has two weather.xml files:
  'for Vestigia (active-ess)'  -> Vestigia/active/ess/weather.xml
  'for Rain Sheets add-on'     -> lml/Vestigia - Rain Sheets (Optional)/weather.xml  (only if you use the add-on)
Only the DRIZZLE section changes (2 lines). Everything else in weather.xml is identical.
Note: Rain, Thunderstorm and Hurricane also have Fog = 1 in Vestigia (vanilla 0). If you see the
plane there too, the same change can be made for them.
