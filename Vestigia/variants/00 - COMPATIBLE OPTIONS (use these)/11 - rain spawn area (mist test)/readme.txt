RAIN SPAWN AREA (TEST for the vertical "mist" plane that follows you in the wilderness)
Heavy rain only exists inside a box that moves with the camera: 10 m wide, 8 m deep, 15 m tall,
6 m in front of you. Because the drops bend the image behind them, the edge of that box can look
like a vertical round-ish haze plane. This option makes the box about 2x bigger, so its edge is
further away and blends in.

IT IS A TEST: the game has a fixed number of rain drops, so a bigger box = rain a bit sparser.
If the mist plane disappears, tell Claude and the density can be balanced properly.
If nothing changes, put '0 - current' back - the mist comes from somewhere else.

OPTION A - copy files (easiest):
  Pick ONE option folder. Files directly in it -> Vestigia/active/ess (replace),
  files in its str/ subfolder -> Vestigia/active/str (replace).
  '0 - current (installed)' puts back what you have now.

OPTION B - edit by hand (use this if you already picked another rain preset in 01 or 08,
  so you keep that preset and only add this change):
  Open '1 - larger spawn area (test)/lines changed.txt'. For each file listed, open it in Notepad,
  find the setting and change the number to the new value. Save.

Affects: Drizzle, Rain, Shower, Thunderstorm, Hurricane emitters (5 files, not the look files).
Optional: raise rain.NumberParticles in visualsettings.dat (see 'lines changed.txt') to keep rain dense.
Compatible with every option in 01, 09 and 10 (different files). Overwritten only by 08.
