DRIZZLE FOG CLOSER TO SHOWER - target = the Shower you use: option 17-C (volumetric only + wind).
Drizzle looked foggier than Shower because, after the vanilla fix (option 21),
its fog sits in a low dense layer (fog height 0..500 vs Shower 500..5000), its localized fog around you is
2-3x Shower's (0.1-0.3 vs Shower 17-C: 0 - flat layer off, volumetric near-camera fog 0.4-0.6 instead), and it has rain haze (Shower: none).

These options move Drizzle's fog AMOUNT settings toward Shower's, in wilderness + towns:
  local_atmosphere_fog_density, _fog_height, _fog_falloff        overall fog, how high it reaches, how it thins
  local_atmosphere_localized_fog_density_mult (+ _raymarch)      fog around you / near the camera
  local_atmosphere_rain_density_falloff (+ _threshold at 100%)  rain haze (Shower has none): 50% = half strength, 100% = off
  localized fog wind / voxel wind / large-scale wind              fog drift with the wind, like your Shower (17-C)
Drizzle's fog SHAPE (noise, fog volumes, clouds) is not touched - the 2D plane fixes stay.

Pick the one that matches the Drizzle you use now:
  1 - 50% toward shower (on 21-1)        4 - like shower (on 21-1)
  2 - 50% toward shower (on 23-1)        5 - like shower (on 23-1)
  3 - 50% toward shower (on 23-2)        6 - like shower (on 23-2)
  0 - current (installed) = the installed Drizzle (21-2). To go back to 21-1 / 23-x, copy it from option 21 / 23.

HOW: copy w_drizzle.xml from ONE option folder to  Vestigia/active/ess  (replace).
Each folder has 'lines changed.txt' with the exact before/after values.
