# Stafy4-Translation-Tools
You MUST put the ROM in the same folder as the exe, or it won't work.

This code is designed to use wbmgt (https://szs.wiimm.de/wbmgt/) to let you easily edit Starfy 4's text,
and then reinsert it back into the ROM with no issues.

To use this, you can simply drag and drop your ROM onto functions.exe. Then, just edit the plain text files
in the X_textFiles folder to change the text, and drag the ROM onto functions.exe again to yield your new
ROM, out.nds.

Also, Moe's first dialogue for the City tutorial can be found in 0009_textFiles' 582164_585268.BMG, starting
at 0x75 (or just the first thing in the text file).

Finally, to download this, if you are confused, press the Green "Code" button in the top right, then choose "Download ZIP".

# Source Codes
- wbmgt: https://github.com/Wiimm/wiimms-szs-tools
- NDSTool: https://github.com/devkitPro/ndstool (this is a later version; the one used here came without a license as part of DSLazy)
