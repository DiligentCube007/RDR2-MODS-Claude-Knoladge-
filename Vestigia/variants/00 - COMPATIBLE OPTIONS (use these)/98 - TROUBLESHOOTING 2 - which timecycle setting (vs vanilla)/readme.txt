TROUBLESHOOTING 2 - which timecycle setting makes the mist plane (compared with VANILLA)

Built from your vanilla timecycles (Vestigia/timecycle vanila). Each test puts ONE group of settings
back to the vanilla value of that same weather, in all rainy timecycles (Drizzle, Rain, Shower +3
variants, Sleet). Everything else stays Vestigia.

HOW: copy all 7 files from ONE test folder to  Vestigia/active/ess  (replace), load the save,
check Shower (and Rain). Put '0 - current (put back after testing)' back before the next test.

A - fog volumes like vanilla  (test this first)
    Vestigia draws the game's placed mist/dust/smoke fog volumes at 100% (vanilla: mist 15%,
    dust 0%, smoke 10%) and lights them much more. Fog volumes are box/ellipsoid shaped.
    Settings: local_atmosphere_fog_volume_mist_density_mult, local_atmosphere_fog_volume_dust_density_mult, local_atmosphere_fog_volume_smoke_density_mult, local_atmosphere_fog_volume_pollution_density_mult, local_atmosphere_fog_volume_waterfall_density_mult, local_atmosphere_fog_volume_snow_density_mult, fog_volume_light_range, fog_volume_light_fade, fog_volume_exterior_light_intensity, fog_volume_light_size, fog_volume_interior_light_intensity
B - fog noise and localized fog like vanilla
    Vestigia's fog noise range is 0..2 (vanilla ~0.43..0.75) = very patchy, sharp-edged fog blobs.
    Settings: local_atmosphere_voxel_noise_min, local_atmosphere_voxel_noise_max, local_atmosphere_voxel_noise_scale_mult_z, local_atmosphere_voxel_detail_wind_vertical_speed, local_atmosphere_voxel_distribution_blend, local_atmosphere_localized_fog_density_mult, local_atmosphere_localized_fog_density_mult_raymarch, local_atmosphere_localized_fog_noise_bounds_x, local_atmosphere_localized_fog_noise_bounds_y, local_atmosphere_localized_fog_wind_velocity, local_atmosphere_localized_fog_height_offset
C - fog shadows like vanilla
    Settings: fog_shadow_amount, local_atmosphere_fog_shadow_amount, fog_shadow_falloff, fog_shadow_base_height
D - rain haze like vanilla
    Settings: local_atmosphere_rain_threshold, local_atmosphere_rain_density_falloff
E - all of A+B+C+D together (quick check)
    If even E doesn't remove the plane, the cause is in the lighting/sky/cloud settings instead.

Tell Claude which test removes the plane.
