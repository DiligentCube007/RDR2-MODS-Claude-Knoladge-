FOG NOISE OFF - smooth volumetric rain haze with no pattern (on top of the mist plane fix, option 15).

The voxel noise is the pattern INSIDE the volumetric fog: it decides how thick the fog is in each 3D cell.
  Vestigia 0..2      -> dense, hard-edged blobs = the 2D planes (fixed by option 15)
  vanilla ~0.43..0.75 -> gentle patches = the even haze installed now
  min = max           -> same thickness everywhere = perfectly smooth fog, no patches or planes at all

1 - noise off (perfectly smooth)
    voxel_noise_min = voxel_noise_max (the middle of the current range). The amount of fog stays the same,
    it just has no pattern. Downside: with no pattern you can't SEE the fog move with the wind.
2 - very faint pattern
    Range narrowed to 30% around the same middle: barely visible patches, a hint of movement.
0 - current (installed) = undo.

Only local_atmosphere_voxel_noise_min / _max change (wilderness region). Nothing else.
HOW: copy all 12 files from ONE option folder to  Vestigia/active/ess  (replace).
Options 16, 17 and 18 change the same files - use only one of them.

Option 1 values:
   w_drizzle                    noise 0.429..0.764  ->  0.530..0.730
   w_rain                       noise 0.200..0.790  ->  0.484..0.601
   w_shower                     noise 0.428..0.747  ->  0.587..0.587
   w_shower_finale2             noise 0.428..0.747  ->  0.587..0.587
   w_shower_guama               noise 0.428..0.747  ->  0.587..0.587
   w_shower_mp_pred             noise 0.428..0.747  ->  0.587..0.587
   w_sleet                      noise 0.500..0.598  ->  0.549..0.549
   w_hail                       noise 0.500..0.598  ->  0.549..0.549
   w_hurricane                  noise 0.442..0.772  ->  0.545..0.607
   w_thunder                    noise 0.500..0.598  ->  0.549..0.549
   w_thunderstorm               noise 0.413..0.738  ->  0.549..0.599
   w_thunderstorm_mp_pred       noise 0.461..0.738  ->  0.549..0.599
   w_thunderstorm_nativeson3    noise 0.413..0.738  ->  0.549..0.599

Option 2 values:
   w_drizzle                    noise 0.429..0.764  ->  0.500..0.735
   w_rain                       noise 0.200..0.790  ->  0.399..0.653
   w_shower                     noise 0.428..0.747  ->  0.540..0.635
   w_shower_finale2             noise 0.428..0.747  ->  0.540..0.635
   w_shower_guama               noise 0.428..0.747  ->  0.540..0.635
   w_shower_mp_pred             noise 0.428..0.747  ->  0.540..0.635
   w_sleet                      noise 0.500..0.598  ->  0.534..0.564
   w_hail                       noise 0.500..0.598  ->  0.534..0.564
   w_hurricane                  noise 0.442..0.772  ->  0.517..0.657
   w_thunder                    noise 0.500..0.598  ->  0.534..0.564
   w_thunderstorm               noise 0.413..0.738  ->  0.511..0.641
   w_thunderstorm_mp_pred       noise 0.461..0.738  ->  0.534..0.641
   w_thunderstorm_nativeson3    noise 0.413..0.738  ->  0.511..0.641

NOTE: Drizzle is NOT included - it has its own fix (option 21, fog structure like vanilla).
