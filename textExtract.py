import os
import subprocess


try:
    os.mkdir("arm9TextFiles")
except OSError as error:
    pass
    
binn = open("arm9.bin", "rb").read()

starts = []
for i in range(os.stat("arm9.bin").st_size):
    if (binn[i:(i + 8)].decode("UTF-8", errors = "backslashreplace") == "MESGbmg1"):
        starts.append(i)

for i in range(len(starts)):
    size = int.from_bytes(binn[(starts[i] + 8):(starts[i] + 12)], "big")
    filePath = "./arm9TextFiles/" + str(starts[i]) + "_" + str(starts[i] + size) + ".BMG"
    new = open(filePath, "wb")
    new.write(binn[starts[i]:(starts[i] + size)])
    new.close()
    subprocess.run([ "./wbmgt/wbmgt.exe", "decode", filePath, "--x-escapes", "--overwrite" ])


for j in range(34):
    try:
        os.mkdir(str(j).zfill(4) + "_textFiles")
    except OSError as error:
        pass
        
    binn = open("overlay9_" + str(j).zfill(4) + ".bin", "rb").read()

    starts = []
    for i in range(os.stat("overlay9_" + str(j).zfill(4) + ".bin").st_size):
        if (binn[i:(i + 8)].decode("UTF-8", errors = "backslashreplace") == "MESGbmg1"):
            starts.append(i)

    for i in range(len(starts)):
        size = int.from_bytes(binn[(starts[i] + 8):(starts[i] + 12)], "big")
        filePath = "./" + str(j).zfill(4) + "_textFiles/" + str(starts[i]) + "_" + str(starts[i] + size) + ".BMG"
        new = open(filePath, "wb")
        new.write(binn[starts[i]:(starts[i] + size)])
        new.close()
        subprocess.run([ "./wbmgt/wbmgt.exe", "decode", filePath, "--x-escapes", "--overwrite" ])
    
    if (len(os.listdir("./" + str(j).zfill(4) + "_textFiles")) == 0):
        os.rmdir(str(j).zfill(4) + "_textFiles")