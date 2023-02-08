import subprocess
import os
try:
    os.mkdir("output")
except OSError as error:
    pass
fileDict = {}

for i in range(34):
    endLoc = os.stat("./overlay9_" + str(i).zfill(4) + ".bin").st_size + int(0x021275E0)
    appends = []

    if (os.path.exists("./" + str(i).zfill(4) + "_textFiles/") == True):
        for root, dirs, files in os.walk("./" + str(i).zfill(4) + "_textFiles/"):
            for file in files:
                if (file.endswith(".BMG") == True):
                    subprocess.run([ "./wbmgt/wbmgt.exe", "encode", os.path.join(root, file.split(".")[0] + ".txt"), "--overwrite",
                        "--encoding", "SHIFTJIS" ])
                    begOffset = int(file.split("_")[0])
                    endOffset = int(file.split("_")[1].split(".")[0])
                    change = os.stat("./" + str(i).zfill(4) + "_textFiles/" + file).st_size - (endOffset - begOffset)
                    if (change != 0):
                        fileDict[begOffset + int(0x021275E0)] = endLoc
                        endLoc = endLoc + os.stat("./" + str(i).zfill(4) + "_textFiles/" + file).st_size
                        appends.append(os.path.join(root, file))
    
    old = open("./overlay9_" + str(i).zfill(4) + ".bin", "rb")
    whole = old.read()
    old.close()
    new = open("./output/overlay9_" + str(i).zfill(4) + ".bin", "wb")
    new.close()
    new = open("./output/overlay9_" + str(i).zfill(4) + ".bin", "ab")

    new.write(whole)
    for file in appends:
        bmg = open(file, "rb")
        new.write(bmg.read())
        bmg.close()
    new.close()
            
        

endLoc = os.stat("./arm9.bin").st_size + int(0x02000000)
appends = []
offsetList = []
for root, dirs, files in os.walk("./arm9TextFiles/"):
    for file in files:
        if (file.endswith(".BMG") == True):
            subprocess.run([ "./wbmgt/wbmgt.exe", "encode", os.path.join(root, file.split(".")[0] + ".txt"), "--overwrite",
                "--encoding", "SHIFTJIS" ])
            begOffset = int(file.split("_")[0])
            endOffset = int(file.split("_")[1].split(".")[0])
            change = os.stat("./arm9TextFiles/" + file).st_size - (endOffset - begOffset)
            if (change != 0):
                fileDict[begOffset + int(0x02000000)] = endLoc
                endLoc = endLoc + os.stat("./arm9TextFiles/" + file).st_size
                appends.append(os.path.join(root, file))

old = open("./arm9.bin", "rb")
whole = old.read()
old.close()
new = open("./output/arm9.bin", "wb")
new.close()
new = open("./output/arm9.bin", "ab")

for i in range(int(0x0932FC), int(0x093459), 4):
    pointed = int.from_bytes(whole[i:(i + 4)], "little")
    if (pointed in fileDict.keys()):
        offsetList.append([ fileDict[pointed], i, i + 4 ])
    else:
        offsetList.append([ pointed, i, i + 4 ])

offsetList.sort(key = lambda a: a[1])
new.write(whole[0:offsetList[0][1]])
new.write(offsetList[0][0].to_bytes(4, "little"))
for j in range(1, len(offsetList)):
    new.write(offsetList[j][0].to_bytes(4, "little"))
new.write(whole[offsetList[-1][2]:])

for file in appends:
    bmg = open(file, "rb")
    new.write(bmg.read())
    bmg.close()
new.close()


old = open("./y9.bin", "rb")
whole = old.read()
old.close()
new = open("./output/y9.bin", "wb")
new.close()
new = open("./output/y9.bin", "ab")

for i in range(34):
    new.write(whole[(i * 32):(8 + i * 32)])
    new.write(os.stat("./output/overlay9_" + str(i).zfill(4) + ".bin").st_size.to_bytes(4, "little"))
    new.write(whole[(12 + i * 32):(32 + i * 32)])
