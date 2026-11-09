DRIZZLE PATCHES SOFTER - for option 21-1 (fog structure vanilla, keeps Vestigia clouds).
Makes the soft patches around the field/player more transparent and blend into the surrounding fog.
All files keep 21-1 (Vestigia clouds). Changes apply to wilderness + towns.

1 - a bit softer
   fog noise range x0.6 (narrower): 0.429..0.764 -> 0.469..0.740
   rain haze threshold 25% toward 1 where active: 0.5 -> 0.62 (higher = fainter)
2 - much softer
   fog noise range x0.3 (narrower): 0.429..0.764 -> 0.500..0.735
   rain haze threshold 50% toward 1 where active: 0.5 -> 0.75 (higher = fainter)
   overall fog density x1.15 (fills in around the patches)
3 - rain haze off (noise unchanged)
   rain haze threshold + falloff = Vestigia values (rain haze off)
    Use this to see if the patches come from the rain haze: if they vanish, they did.
0 - 21-1 as is = undo.

HOW: copy w_drizzle.xml from ONE option folder to  Vestigia/active/ess  (replace).
(Option 22 is built on 21-2 - with 21-1 use this option 23 instead.)
