GROUND SPLASH MIST - test for the 2D mist plane near the ground in rainy weather.

The rain ground-splash particles spawn in a box ~0-27 m in front of you that moves with you.
Their settings are extreme: image-bending boost x100, and (Rain/Shower/Drizzle) a depth-of-field
output of x36 that can make the game blur the splashes into a soft white cloud.

HOW TO USE: copy files of ONE option. Files directly in it -> Vestigia/active/ess,
files in its str/ subfolder -> Vestigia/active/str. Or edit by hand with 'lines changed.txt'.

1 - splashes OFF (test)
    Makes the ground splashes invisible (rain still falls, puddle ripples stay).
    -> Mist gone?  Then the splashes are the cause: use option 2 (or stay on 1 if you don't miss them).
    -> Mist still there?  Not the splashes. Put '0 - current' back and tell Claude.

2 - splashes subtle (fix candidate)
    Keeps the splashes but removes what can turn them into a mist:
    bending boost 100 -> 15, depth-of-field output 36 -> 1, near-camera growth 6x -> 1.5x.

0 - current (installed) = undo.
Uses different files from options 01, 09, 10, 11. Option 08 overwrites these files.
