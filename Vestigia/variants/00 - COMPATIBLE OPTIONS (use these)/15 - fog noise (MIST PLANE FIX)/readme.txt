FOG NOISE - THE fix for the 2D "mist plane" (found with troubleshooting test B, confirmed by Hail)

CAUSE: Vestigia changes the local-atmosphere fog noise in almost every weather:
  local_atmosphere_voxel_noise_min/max   vanilla ~0.43 / ~0.75   ->  Vestigia 0 / 2
  (plus faster vertical noise movement, wind 1 -> 5, localized fog off)
The 0..2 noise range turns the near-camera rain/fog haze into a few dense, sharp-edged 2D blobs
that move with you. Vanilla's narrow range spreads the haze evenly all around you and the fields -
softer and much more 'rainy'. This fix puts these 11 settings back to each weather's own vanilla
values; everything else in Vestigia (colours, lighting, clouds, haze colour fix) stays the same.

1 - rainy weathers (INSTALLED)
      Drizzle, Rain, Shower (+3 story variants), Sleet, Hail, Hurricane.
2 - all weathers
      Also Clouds, Overcast, Overcast Dark, Fog, Misty, Snow, Blizzard, High Pressure etc.
      Same even-spread haze everywhere. Copy all files of this folder to Vestigia/active/ess.
0 - previous (Vestigia fog noise) = undo (all weathers).

HOW: copy all files from ONE option folder to  Vestigia/active/ess  (replace).
THUNDER / THUNDERSTORM: see 'THUNDER and THUNDERSTORM - hand edit.txt'.

Option 1 changes:
    w_drizzle.xml: 9 settings
  w_hail.xml: 9 settings
  w_hurricane.xml: 9 settings
  w_rain.xml: 8 settings
  w_shower.xml: 9 settings
  w_shower_finale2.xml: 9 settings
  w_shower_guama.xml: 10 settings
  w_shower_mp_pred.xml: 9 settings
  w_sleet.xml: 9 settings
