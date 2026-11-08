TROUBLESHOOTING 2 - which timecycle setting makes the mist plane

We know it's in Vestigia's rain timecycles (troubleshooting test A). Shower shows it most; Hurricane
may have it too but hidden by its very thick fog (so fog density is NOT copied from Hurricane). These tests switch groups of Shower/Hurricane differences in ALL rainy timecycles
(Drizzle, Rain, Shower + 3 variants, Sleet). Together the 3 groups cover EVERY difference
(no_rain was already tested with option 14).

HOW: copy all 7 files from ONE test folder to  Vestigia/active/ess  (replace), load the save,
check Shower (and Rain). Then put '0 - current (put back after testing)' back before the next test.
(These are built from the default files - if you installed option 14, it is undone during the test.)

A - fog shadows OFF (test this first)
      fog_shadow_amount and local_atmosphere_fog_shadow_amount -> 0 (Hurricane uses 0).
      Fog shadows are only calculated in a zone around the camera; their edge can show as a
      lit/unlit plane in the fog that moves with you.
B - clouds like Hurricane (fog density unchanged)
      local_atmosphere_cloud_density, local_atmosphere_cloud_horizontal_shape_0_y, local_atmosphere_cloud_horizontal_shape_0_z, local_atmosphere_cloud_horizontal_shape_1_y, local_atmosphere_cloud_horizontal_shape_1_z, local_atmosphere_cloud_horizontal_shape_octave_1_x, local_atmosphere_cloud_horizontal_shape_octave_1_z, local_atmosphere_cloud_map_erosion_0_x, local_atmosphere_cloud_region_mask_1_x, local_atmosphere_cloud_height, local_atmosphere_cloud_height_top, local_atmosphere_cloud_detail_noise_low_x, local_atmosphere_cloud_detail_noise_high_x, local_atmosphere_direct_light_absorption, local_atmosphere_direct_light_absorption_dist, local_atmosphere_direct_light_intensity, local_atmosphere_dir_transmittance_col_mult, local_atmosphere_rainbow_far_mult, local_atmosphere_cloud_shadow_alpha
C - light and sky like Hurricane
      light_dir_col_r, light_dir_col_g, light_dir_col_b, light_dir_mult, light_dir_transmittance_col_mult, indirect_light_multiplier, ambient_sky_intensity, lightanim_wind, sky_scattering_sun_col_r, sky_scattering_sun_col_g, sky_scattering_sun_col_b, sky_scattering_sky_col_r, sky_scattering_sky_col_g, sky_scattering_sky_col_b, sky_scattering_moon_col_r, sky_scattering_moon_col_g, sky_scattering_moon_col_b, sky_scattering_aerosol_height, sky_scattering_aerosol_density_scale, sky_scattering_aerosol_absorption_scale
      (rain will look brighter/differently lit during this test - expected)

Tell Claude which test removes the plane. Then a proper fix (and only that) goes into an option.
