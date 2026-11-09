WIND-DRIVEN FOG - makes the rain haze drift with the wind (on top of the mist plane fix, option 15).

The 2D plane was caused by EXTREME fog noise contrast (0..2), not by wind. With the noise back to vanilla
(option 15), the haze is even. These options make that even haze move with the wind:
  local_atmosphere_localized_fog_wind_velocity      how fast the localized fog drifts with the wind
  local_atmosphere_voxel_wind_velocity_scale        how fast the fog noise (its texture) is blown along
  local_atmosphere_large_scale_wind_velocity_scale  how fast big-scale fog variation is blown along

1 - gentle drift (try first)
   local_atmosphere_localized_fog_wind_velocity: x2
   local_atmosphere_voxel_wind_velocity_scale: x1.5
   local_atmosphere_large_scale_wind_velocity_scale: x1.5
2 - strong drift + wisps
   local_atmosphere_localized_fog_wind_velocity: x3
   local_atmosphere_voxel_wind_velocity_scale: x2
   local_atmosphere_large_scale_wind_velocity_scale: x2
   voxel noise range 1.4x wider around its centre (shower: 0.428..0.747 -> 0.364..0.810; Vestigia original was 0..2)
    The slightly wider noise range makes the drifting fog more visible as wisps/patches.
    If you see the 2D blobs coming back, go back to option 1.
0 - current (installed) = undo.

Applies to: Rain, Shower (+3 variants), Sleet, Hail, Hurricane, Thunder, Thunderstorm (+2 variants).
HOW: copy all 12 files from ONE option folder to  Vestigia/active/ess  (replace).
These files already include the mist plane fix (option 15) - nothing else is changed.

NOTE: Drizzle is NOT included - it has its own fix (option 21, fog structure like vanilla).
