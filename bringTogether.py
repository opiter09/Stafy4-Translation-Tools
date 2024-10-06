import os
import subprocess

def bring():
    try:
        os.mkdir("output")
    except OSError as error:
        pass
    fileDict = {}
    
    old = open("./input/arm9.bin", "rb")
    whole = old.read()
    old.close()
    new = open("./output/arm9.bin", "wb")
    new.close()
    new = open("./output/arm9.bin", "ab")
    endLoc = os.stat("./input/arm9.bin").st_size + int(0x02000000)
    appends = []
    offsetList = []
    arm9Change = 0
    for root, dirs, files in os.walk("./arm9_textFiles/"):
        for file in files:
            if (file.endswith(".BMG") == True):
                subprocess.run([ "./wbmgt/wbmgt.exe", "encode", os.path.join(root, file.split(".")[0] + ".txt"), "--overwrite",
                    "--encoding", "SHIFTJIS" ])
                begOffset = int(file.split("_")[0])
                endOffset = int(file.split("_")[1].split(".")[0])
                change = os.stat("./arm9_textFiles/" + file).st_size - (endOffset - begOffset)
                # arm9Change = arm9Change + change
                if (change != 0):
                    fileDict[begOffset + int(0x02000000)] = endLoc
                    endLoc = endLoc + os.stat("./arm9_textFiles/" + file).st_size
                    appends.append(os.path.join(root, file))
    for file in appends:
        bmg = open(file, "rb")
        new.write(bmg.read())
        bmg.close()
    new.close()

    for i in range(34):
        endLoc = os.stat("./input/overlay_" + str(i).zfill(4) + ".bin").st_size + int(0x021275E0) + arm9Change
        appends = []
        if (os.path.exists("./" + str(i).zfill(4) + "_textFiles/") == True):
            for root, dirs, files in os.walk("./" + str(i).zfill(4) + "_textFiles/"):
                for file in files:
                    if (file.endswith(".BMG") == True):
                        subprocess.run([ "./wbmgt/wbmgt.exe", "encode", os.path.join(root, file.split(".")[0] + ".txt"),
                            "--overwrite", "--encoding", "SHIFTJIS" ])
                        begOffset = int(file.split("_")[0])
                        endOffset = int(file.split("_")[1].split(".")[0])
                        change = os.stat("./" + str(i).zfill(4) + "_textFiles/" + file).st_size - (endOffset - begOffset)
                        if (change != 0):
                            fileDict[begOffset + int(0x021275E0)] = endLoc
                            endLoc = endLoc + os.stat("./" + str(i).zfill(4) + "_textFiles/" + file).st_size
                            appends.append(os.path.join(root, file))        
        old = open("./input/overlay_" + str(i).zfill(4) + ".bin", "rb")
        whole = old.read()
        old.close()
        new = open("./output/overlay_" + str(i).zfill(4) + ".bin", "wb")
        new.close()
        new = open("./output/overlay_" + str(i).zfill(4) + ".bin", "ab")
        new.write(whole)
        for file in appends:
            bmg = open(file, "rb")
            new.write(bmg.read())
            bmg.close()
        new.close()

    old = open("./input/arm9.bin", "rb")
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
            offsetList.append([ pointed + arm9Change, i, i + 4 ])
    offsetList.sort(key = lambda a: a[1])
    new.write(whole[0:offsetList[0][1]])
    new.write(offsetList[0][0].to_bytes(4, "little"))
    for j in range(1, len(offsetList)):
        new.write(offsetList[j][0].to_bytes(4, "little"))
    new.write(whole[offsetList[-1][2]:])
    new.close()


    old = open("./input/y9.bin", "rb")
    whole = old.read()
    old.close()
    new = open("./output/y9.bin", "wb")
    new.close()
    new = open("./output/y9.bin", "ab")
    for i in range(34):
        new.write(whole[(i * 32):(4 + i * 32)])
        ram = int.from_bytes(whole[(4 + i * 32):(8 + i * 32)], "little")
        new.write((ram + arm9Change).to_bytes(4, "little"))
        new.write(os.stat("./output/overlay_" + str(i).zfill(4) + ".bin").st_size.to_bytes(4, "little"))
        new.write(whole[(12 + i * 32):(32 + i * 32)])
