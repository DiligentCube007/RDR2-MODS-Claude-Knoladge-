DRIZZLE FOG STRUCTURE LIKE VANILLA - removes the remaining 2D fog plane in Drizzle.

Troubleshooting test A showed: with vanilla timecycles there is no plane. Colours can't make shapes, so
these options put every fog-SHAPE setting of Drizzle back to vanilla, in BOTH regions (wilderness + towns),
and keep all of Vestigia's colours and lighting (incl. the less-blue haze).

1 - fog structure vanilla (keeps Vestigia clouds)
    fog height/falloff, fog volumes (mist/dust/smoke), rain haze, fog shadows, fog noise, localized fog,
    all fog wind/movement settings, no_rain.   (44 settings)
2 - fog + cloud structure vanilla (INSTALLED)
    1 + the cloud layer shape/height/noise/shadows (the low cloud layer can also cut through the
    ground haze).   (120 settings)
3 - full vanilla drizzle (guaranteed)
    The complete vanilla w_drizzle.xml - like troubleshooting test A, for Drizzle only.
    Use this if 2 still shows the plane. Drizzle then looks vanilla (colours too).
0 - previous = undo.

NOTE: option 16 (wind drift) does not apply to Drizzle with these options (its wind settings are vanilla
here). Make sure option 20 (Drizzle in weather.xml) is installed too.
HOW: copy w_drizzle.xml from ONE option folder to  Vestigia/active/ess  (replace).
