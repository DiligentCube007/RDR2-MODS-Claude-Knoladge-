TROUBLESHOOTING - find which part of Vestigia makes the 2D mist plane

Each test folder has an install.xml that switches OFF one part of Vestigia (the game uses vanilla
files for that part instead). Nothing else changes. Run the tests one at a time:

  1. Copy install.xml from ONE test folder into  lml/Vestigia/  (replace the existing install.xml)
  2. Start the game, load your save, look for the mist plane
  3. Put the ORIGINAL back:  '0 - ORIGINAL install.xml (put this back after testing)/install.xml'
     -> lml/Vestigia/install.xml

A - WITHOUT Vestigia weather timecycles  (most likely - test first)
    All weathers use vanilla lighting/fog/colours (Vestigia's own sunny weathers stay).
    Game will look much more vanilla during this test - that's expected.
B - WITHOUT timecycle_mods        (Vestigia's location/interior/mission light modifiers)
C - WITHOUT rain and snow particle files  (vanilla rain/snow drops and splashes)
D - WITHOUT visualsettings        (vanilla visualsettings.dat)
E - WITHOUT Visual Details module (snow, tessellation, breath, accumulation, snow glints)

Tell Claude which test makes the mist plane disappear - then the fix can be targeted at
exactly that part instead of guessing.
