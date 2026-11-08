RAIN FOG 25% CLOSER TO VANILLA - only the RAIN weather (w_rain.xml) moves a quarter of the way from
Vestigia's fog toward vanilla. Drizzle, Shower, Thunderstorm etc. are not changed.

Settings moved 25% toward vanilla (per time of day):
  local_atmosphere_fog_density  - how thick the fog is
  local_atmosphere_fog_height   - how high it reaches
  local_atmosphere_fog_falloff  - how slowly it thins out with height
Everything else (incl. the mist plane fix) unchanged.

1 - on installed fix (no wind)
2 - with wind - gentle drift (16-1)   = option 16-1 + this
3 - with wind - strong drift (16-2)   = option 16-2 + this
0 - current (installed) = undo.

HOW: copy w_rain.xml from ONE option folder to  Vestigia/active/ess  (replace).
Using option 16 (wind)? Install option 16 first, then copy w_rain.xml from 19-2 (gentle) or 19-3 (strong).

Fog thickness, average over the day (wilderness):
   w_rain                       vanilla 0.00087   Vestigia 0.00592 (6.8x)   ->  0.00465 (5.4x vanilla)
