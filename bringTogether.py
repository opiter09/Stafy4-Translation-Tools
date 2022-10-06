import subprocess
import os
try:
    os.mkdir("output")
except OSError as error:
    pass

globalSum = 0

file = open("./overlay_pointers/arm9_TABLE.po", "rt")
lines = file.read().split("\n")
file.close()
offsetList = []
for j in range(len(lines) - 1):
    if lines[j + 1].startswith("msgid") and (len(lines[j + 1]) > 14) and ("<" not in lines[j + 1]) and ("@" not in lines[j + 1]) and ("ï" not in lines[j + 1]):
        if len(lines[j].split(",")) > 1:
            print(j)
        for substring in lines[j].split(";"):
            offsetList.append([ int(substring.split("(")[1].split(")")[0], 16), int(substring.split("<- ")[1].split(" ")[0], 16),
                int(substring.split("<- ")[1].split(" ")[0], 16) + 4 ])   
offsetList.sort(key = lambda a: a[0])

starter = 0
for root, dirs, files in os.walk("./arm9TextFiles/"):
    for file in files:
        if (file.endswith(".BMG") == True):
            subprocess.run([ "./wbmgt/wbmgt.exe", "encode", os.path.join(root, file), "--overwrite", "--encoding", "SHIFTJIS" ])
            begOffset = int(file.split("_")[0])
            endOffset = int(file.split("_")[1].split(".")[0])
            change = os.stat("./arm9TextFiles/" + file).st_size - (endOffset - begOffset)
            if (change != 0):
                print("arm9: " + file)
            for j in range(starter, len(offsetList)):
                if (offsetList[j][0] > begOffset):
                    offsetList.insert(j, [ -1, begOffset, endOffset ])
                    globalSum = globalSum + change
                    starter = j + 1
                    break
                elif (j == len(offsetList) - 1):
                    offsetList.append([ -1, begOffset, endOffset ])
                    globalSum = globalSum + change
                    starter = -1
                else:
                    offsetList[j][0] = offsetList[j][0] + globalSum
if (starter != -1):
    for j in range(starter, len(offsetList)):
        if (offsetList[j][0] != -1):
            offsetList[j][0] = offsetList[j][0] + globalSum

offsetList.sort(key = lambda a: a[1])
old = open("./arm9.bin", "rb")
whole = old.read()
old.close()
new = open("./output/arm9.bin", "wb")
new.close()
new = open("./output/arm9.bin", "ab")

if (len(offsetList) > 0):
    new.write(whole[0:offsetList[0][1]])
    new.write(offsetList[0][0].to_bytes(4, "little"))
    for j in range(1, len(offsetList)):
        if (offsetList[j][0] != -1):
            new.write(whole[offsetList[j - 1][2]:offsetList[j][1]])
            new.write(offsetList[j][0].to_bytes(4, "little"))
        else:
            temp = open("./arm9TextFiles/" + str(offsetList[j][1]) + "_" + str(offsetList[j][2]) + ".BMG", "rb")
            new.write(whole[offsetList[j - 1][2]:offsetList[j][1]])
            new.write(temp.read())
            temp.close()
    new.write(whole[offsetList[-1][2]:])
    new.close()
else:
    new.write(whole)
    new.close()



for i in range(34):
    globalSum = 0

    file = open("./overlay_pointers/overlay_" + str(i).zfill(4) + "_TABLE.po", "rt")
    lines = file.read().split("\n")
    file.close()
    offsetList = []
    for j in range(len(lines) - 1):
        if lines[j + 1].startswith("msgid") and (len(lines[j + 1]) > 14) and ("<" not in lines[j + 1]) and ("@" not in lines[j + 1]) and ("ï" not in lines[j + 1]):
            # if len(lines[j].split(",")) > 1:
                # print(i)
            for substring in lines[j].split(";"):
                offsetList.append([ int(substring.split("(")[1].split(")")[0], 16), int(substring.split("<- ")[1].split(" ")[0], 16),
                    int(substring.split("<- ")[1].split(" ")[0], 16) + 4 ])   
    offsetList.sort(key = lambda a: a[0])

    starter = 0
    if (os.path.exists("./" + str(i).zfill(4) + "_textFiles/") == True):
        for root, dirs, files in os.walk("./" + str(i).zfill(4) + "_textFiles/"):
            for file in files:
                if (file.endswith(".BMG") == True):
                    subprocess.run([ "./wbmgt/wbmgt.exe", "encode", os.path.join(root, file), "--overwrite", "--encoding", "SHIFTJIS" ])
                    begOffset = int(file.split("_")[0])
                    endOffset = int(file.split("_")[1].split(".")[0])
                    change = os.stat("./" + str(i).zfill(4) + "_textFiles/" + file).st_size - (endOffset - begOffset)
                    if (change != 0):
                        print("overlay " + str(i) + ": " + file + "  change = " + str(change))
                    for j in range(starter, len(offsetList)):
                        if (offsetList[j][0] > begOffset):
                            offsetList.insert(j, [ -1, begOffset, endOffset ])
                            globalSum = globalSum + change
                            starter = j + 1
                            break
                        elif (j == len(offsetList) - 1):
                            offsetList.append([ -1, begOffset, endOffset ])
                            globalSum = globalSum + change
                            starter = -1
                        else:
                            offsetList[j][0] = offsetList[j][0] + globalSum
        if (starter != -1):
            for j in range(starter, len(offsetList)):
                if (offsetList[j][0] != -1):
                    offsetList[j][0] = offsetList[j][0] + globalSum
    
    offsetList.sort(key = lambda a: a[1])
    old = open("./overlay9_" + str(i).zfill(4) + ".bin", "rb")
    whole = old.read()
    old.close()
    new = open("./output/overlay9_" + str(i).zfill(4) + ".bin", "wb")
    new.close()
    new = open("./output/overlay9_" + str(i).zfill(4) + ".bin", "ab")

    if (len(offsetList) > 0):
        new.write(whole[0:offsetList[0][1]])
        new.write(offsetList[0][0].to_bytes(4, "little"))
        for j in range(1, len(offsetList)):
            if (offsetList[j][0] != -1):
                new.write(whole[offsetList[j - 1][2]:offsetList[j][1]])
                new.write(offsetList[j][0].to_bytes(4, "little"))
            else:
                temp = open("./" + str(i).zfill(4) + "_textFiles/" + str(offsetList[j][1]) + "_" + str(offsetList[j][2]) + ".BMG", "rb")
                new.write(whole[offsetList[j - 1][2]:offsetList[j][1]])
                new.write(temp.read())
                temp.close()
        new.write(whole[offsetList[-1][2]:])
        new.close()
    else:
        new.write(whole)
        new.close()
            
        
    
    