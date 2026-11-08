RAIN COVERAGE - fix for the 2D "mist plane" / rain curtain that follows you in rainy weather.

CAUSE (found with the troubleshooting tests - test A = Vestigia's weather timecycles):
Vestigia's rain timecycles set 'no_rain' to 0.3-0.9 in the wilderness (GLOBAL region). That makes
rain PATCHY: the game leaves rain-free gaps inside a rainy weather, and the soft edges of those rain
cells are drawn as hazy curtains - the vertical, round-ish 2D planes you see. Vanilla rain and
Hurricane use 0 (no gaps) - that is why Hurricane never shows it and Shower (up to 0.8) shows it most.
It also explains the Rampage trainer seeming to not switch weather: you can land in a dry gap.

1 - full coverage (recommended)
      no_rain = 0 for Drizzle, Rain, Shower (+3 story variants), Sleet. Rain everywhere, like vanilla.
2 - reduced patchiness
      no_rain at 25% of Vestigia's values: fewer/smaller gaps. Try this if you like some patchy rain;
      the curtains may still appear, just less often.
0 - current (installed) = undo.

HOW TO USE: copy all files from ONE option folder to  Vestigia/active/ess  (replace).
Or edit by hand with 'lines changed.txt' (one line per file).

Only the wilderness (GLOBAL) value is changed; everything else in these timecycles (colours, fog,
clouds, the less-blue haze fix) stays the same.
NOT INCLUDED: w_thunder.xml and w_thunderstorm.xml are not in the repo (not uploaded). If you see
the plane in Thunderstorm, upload those two files and they can get the same fix.
