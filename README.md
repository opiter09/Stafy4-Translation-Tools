# Stafy4-Translation-Tools
This code is designed to use wbmgt (https://szs.wiimm.de/wbmgt/) to let you easily edit Starfy 4's text,
and then reinsert it back into the ROM with no issues.

To use this, split apart the ROM with CrystalTile (https://www.romhacking.net/utilities/818/) or equivalent.
You'll need arm9.bin, arm9ovltable.bin, and all the overlays--put them into this very folder.

You also need Python (3+). Once you have it run, textExtract.bat (or CLI the py file) to split apart
everything. When you are done, simply use bringTogether.bat.

From there, you will need to insert all the files back into the ROM. For batch stuff like this, I use
jNDSTool (https://github.com/JackHack96/jNdstool). Do note that it has a bit of a different folder set up
than what Crystaltile gives you:
- everything except FSI.CT must go inside a "data" folder
- FSCI.CT must be renamed to "overlay," and the non-overlay files must be taken out of it and put "next
  to it" (in the same folder as it and data)
- ndsheader.bin must renamned to header.bin

Moe's first dialogue for the City tutorial can be found in 0009_textFiles' 582164_585268.BMG, starting
at 0x75 (or just the first thing in the text file)