import bringTogether
import textExtract

import os
import subprocess
import sys

rom = sys.argv[1]
if (os.path.exists("./NDS_UNPACK/") == False):
    subprocess.run([ "dslazy.bat", "UNPACK", sys.argv[1] ])
    try:
        os.mkdir("input")
    except OSError as error:
        pass
    os.rename("./NDS_UNPACK/arm9.bin", "./input/arm9.bin")
    os.rename("./NDS_UNPACK/y9.bin", "./input/y9.bin")
    for root, dirs, files in os.walk("./NDS_UNPACK/overlay/"):
        for file in files:
            os.rename(os.path.join(root, file), "./input/" + file)
    textExtract.extract()
else:
    bringTogether.bring()
    for root, dirs, files in os.walk("./output/"):
        for file in files:
            if ("overlay" in file):
                try:
                    os.remove("./NDS_UNPACK/overlay/" + file)
                except:
                    pass
                os.rename(os.path.join(root, file), "./NDS_UNPACK/overlay/" + file)
            else:
                try:
                    os.remove("./NDS_UNPACK/" + file)
                except:
                    pass
                os.rename(os.path.join(root, file), "./NDS_UNPACK/" + file)
    subprocess.run([ "dslazy.bat", "PACK", "out.nds" ])