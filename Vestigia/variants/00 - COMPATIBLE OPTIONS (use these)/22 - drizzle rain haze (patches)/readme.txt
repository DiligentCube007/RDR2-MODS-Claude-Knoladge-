DRIZZLE RAIN HAZE - the soft patches around the field and player in Drizzle (after option 21-2).

With option 21-2 Drizzle uses vanilla's rain haze (local_atmosphere_rain_threshold / _density_falloff),
which Vestigia had switched off. In vanilla Drizzle it is only active at 4 of the 13 times of day,
so the patches mostly appear around those hours.

1 - weaker rain haze
    Threshold raised halfway to 1 wherever the haze is active -> less of it, smaller/fewer patches.
   GLOBAL threshold 0 0 0 0 0 0.2 0.5 0.2996 0 0.5 0 0 0
          ->        0.00 0.00 0.00 0.00 0.00 0.60 0.75 0.65 0.00 0.75 0.00 0.00 0.00
   URBAN  threshold 1 1 1 1 1 1 1 0 1 0.5977 1 1 1
          ->        1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.00 1.00 0.80 1.00 1.00 1.00
2 - no rain haze
    Threshold and falloff back to Vestigia's values (haze off) - all other Drizzle fixes stay.
    If the patches disappear completely, the rain haze was their source.
0 - current (installed) = undo (vanilla rain haze).

Only these 2 settings change (both regions). Everything else = installed Drizzle (option 21-2).
HOW: copy w_drizzle.xml from ONE option folder to  Vestigia/active/ess  (replace).
