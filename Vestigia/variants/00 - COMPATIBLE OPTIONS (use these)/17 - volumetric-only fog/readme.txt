VOLUMETRIC-ONLY FOG - rain haze from real 3D (volumetric) fog only, no flat layer.

RDR2 builds rain haze from several layers. 'localized_fog_density_mult' is most likely a cheaper, flatter
layer; '..._raymarch' and 'local_atmosphere_fog_density' are calculated through 3D space (depth, light,
shadow, wind). These options switch the flat layer off and give its share to the volumetric fog, so the
amount of haze stays about the same. Built on top of the mist plane fix (option 15).
NOTE: which layer is flat vs volumetric is inferred from the setting names - compare in game.

Example values (Shower):
A - volumetric only (try first)
   local_atmosphere_localized_fog_density_mult: 0.05..0.1 -> 0   (flat layer off)
   local_atmosphere_localized_fog_density_mult_raymarch: 0.2996..0.5 -> 0.400..0.600   (volumetric near-camera fog takes over)
   local_atmosphere_fog_density: x1.1   (overall volumetric fog)
B - volumetric only + thicker
   local_atmosphere_localized_fog_density_mult: 0.05..0.1 -> 0   (flat layer off)
   local_atmosphere_localized_fog_density_mult_raymarch: 0.2996..0.5 -> 0.599..0.900   (volumetric near-camera fog takes over)
   local_atmosphere_fog_density: x1.4   (overall volumetric fog)
   voxel noise range x1.2 wider around its centre: 0.428..0.747 -> 0.396..0.778  (Vestigia original 0..2)
C - volumetric only + wind   (A + the gentle wind drift from option 16)
   local_atmosphere_localized_fog_density_mult: 0.05..0.1 -> 0   (flat layer off)
   local_atmosphere_localized_fog_density_mult_raymarch: 0.2996..0.5 -> 0.400..0.600   (volumetric near-camera fog takes over)
   local_atmosphere_fog_density: x1.1   (overall volumetric fog)
   local_atmosphere_localized_fog_wind_velocity: x2
   local_atmosphere_voxel_wind_velocity_scale: x1.5
   local_atmosphere_large_scale_wind_velocity_scale: x1.5
0 - current (installed) = undo.

Applies to: Rain, Shower (+3 variants), Sleet, Hail, Hurricane, Thunder, Thunderstorm (+2 variants).
HOW: copy all 12 files from ONE option folder to  Vestigia/active/ess  (replace).
Options 16 and 17 change the same files - use one of them (C already includes the wind).

IMPORTANT - in-game graphics settings: volumetric fog is calculated at the resolution of
'Near Volumetric Resolution' / 'Far Volumetric Resolution' / 'Volumetric Lighting Quality'.
On Low/Medium the 3D cells are big and fog can look blocky. Near Volumetric Resolution = Ultra
gives the best result (costs some FPS).

NOTE: Drizzle is NOT included - it has its own fix (option 21, fog structure like vanilla).
