import os
try:
    os.mkdir("output")
except OSError as error:
    pass

globalSum = 0
for i in range(34):
    file = open("./overlay_pointers/overlay_" + str(i).zfill(4) + "_TABLE.po", "rt")
    lines = file.read().split("\n")
    file.close()
    offsetList = []
    for j in range(len(lines) - 1):
        if lines[j + 1].startswith("msgid") and (len(lines[j + 1]) > 14) and ("<" not in lines[j + 1]):
             offsetList.append(int(lines[j].split("<- ")[1].split(" ")[0]))   
    offsetList.sort()

    if (os.path.exists("./" + str(i).zfill(4) + "_textFiles/") == True):
        for root, dirs, files in os.walk("./" + str(i).zfill(4) + "_textFiles/"):
            for file in files:
                oldOffset = int(file.split("_")[0])
                change = os.stat(os.path.join(root, file)).st_size - (int(file.split("_")[1]) - int(file.split("_")[0]))
                for j in range(len(offsetList):
                    if (j > oldOffset):
                        offsetList.insert(j, -1)
                        offsetList.insert(j + 1, change)
                        break


    new = open("./output/overlay9_" + str(i).zfill(4), "wb")
    new.close()
    new = open("./output/overlay9_" + str(i).zfill(4), "ab")
    