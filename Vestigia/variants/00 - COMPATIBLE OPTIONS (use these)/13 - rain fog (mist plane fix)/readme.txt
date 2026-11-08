RAIN FOG - fix for the 2D "mist plane" that follows you in rainy weather.

CAUSE: Vestigia's weather.xml turns ON the Fog switch (<Fog value="1.000000"/>) for DRIZZLE, RAIN,
THUNDERSTORM and HURRICANE. In the vanilla game it is 0 for every weather except FOG. This switch
activates the localized fog volume that is centered on the player - in rain it shows as a small,
dense mist patch that moves with you. Vanilla uses the same system but spread out and fainter.
Vestigia also swapped some weathers to denser fog shapes (LocalizedDensityMap).

OPTIONS
1 - rain fog switch off (vanilla)
      Fog switch back to 0 for Drizzle, Rain, Thunderstorm, Hurricane. Try this first.
2 - rain fog switch off + vanilla fog shapes
      Also puts back the vanilla fog shape for Drizzle, Clouds, Overcast, Overcast Dark, Thunder.
0 - current (installed) = undo.

HOW TO USE - each option has TWO versions of weather.xml. Use the one that matches your setup:
  'for Vestigia (active-ess)'  -> copy weather.xml to  Vestigia/active/ess   (replace)
  'for Rain Sheets add-on'     -> ONLY if the Rain Sheets add-on is installed: ALSO copy this one to
                                  lml/Vestigia - Rain Sheets (Optional)/  (replace)
  (The add-on has its own copy of weather.xml and loads after Vestigia, so it must get the fix too.)
Or edit by hand: 'lines changed.txt' lists every change.

Expect: rain looks a bit less foggy overall (closer to vanilla), the moving mist patch should be gone.
The rest of Vestigia's look (colours, clouds, timecycles) is unchanged.
