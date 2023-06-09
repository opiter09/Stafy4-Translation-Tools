# Stafy4-Translation-Tools
This code is designed to use wbmgt (https://szs.wiimm.de/wbmgt/) to let you easily edit Starfy 4's text,
and then reinsert it back into the ROM with no issues.

To use this, split apart the ROM with DSLazy specifically (https://www.romhacking.net/utilities/793/).
You'll need arm9.bin, y9.bin, and all the overlays--put them into this very folder.

You also need Python (3+). Once you have it run, textExtract.bat (or CLI the py file) to split apart
everything. When you are done, simply use bringTogether.bat.

From there, you will need to insert all the files back into the ROM. Thankfully, DSLazy also does this,
so just put the new files (in the "output" folder) where you got them from in NDS_UNPACK, and then repack.

Moe's first dialogue for the City tutorial can be found in 0009_textFiles' 582164_585268.BMG, starting
at 0x75 (or just the first thing in the text file).

NOTE: Since wbmgt is licensed under the GPL, I legally must inform you that it's source code can be found
at https://github.com/Wiimm/wiimms-szs-tools
