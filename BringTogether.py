import os
try:
    os.mkdir("output")
except OSError as error:
    pass

# format: (stage, beginning of graphics files, end of graphics files, font)
pointerList = [
    (0x00, 0x4B0, 0xC44, 0x1948),
    (0x00, 0x1D20, 0x1D74, 0x3268),
    (0x00, 0x6E4, 0x6F0, 0x00),
    (0xD44, 23B0, 0xAEF64
for i in range(34):
    new = open("./output/overlay9_" + str(i).zfill(4), "wb")
    new.close()
    new = open("./output/overlay9_" + str(i).zfill(4), "ab")
    