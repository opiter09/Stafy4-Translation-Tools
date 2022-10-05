import os
try:
    os.mkdir("arm9TextFiles")
except OSError as error:
    pass
    
binn = open("arm9.bin", "rb").read()

starts = []
for i in range(os.stat("arm9.bin").st_size):
    if (binn[i:(i + 8)].decode("UTF-8", errors = "backslashreplace") == "MESGbmg1"):
        starts.append(i)
starts.append((os.stat("arm9.bin").st_size - 640068) + 602876)

for i in range(len(starts) - 1):
    new = open("arm9TextFiles/" + str(starts[i]) + "_" + str(starts[i + 1]) + ".BMG", "wb")
    new.write(binn[starts[i]:starts[i + 1]])
    new.close()
