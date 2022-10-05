import os

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
    for i in range(os.stat("overlay9_" + str(j).zfill(4) + ".bin").st_size):
        if (len(starts) > 0) and (i > starts[-1]) and (int.from_bytes(binn[(i - 7):(i - 2)], "little") == 6597086878208):
            starts.append(i)
            break
        elif (len(starts) > 0) and (i > starts[-1]) and (int.from_bytes(binn[(i - 16):i], "little") == 0):
            check = 0
            for k in range(i, (os.stat("overlay9_" + str(j).zfill(4) + ".bin").st_size)):
                if (binn[k:(k + 4)].decode("UTF-8", errors = "backslashreplace") == "DAT1"):
                    check = 1
            if (check == 0):
                starts.append(i)
                break

    for i in range(len(starts) - 1):
        new = open(str(j).zfill(4) + "_textFiles/" + str(starts[i]) + "_" + str(starts[i + 1]) + ".BMG", "wb")
        new.write(binn[starts[i]:starts[i + 1]])
        new.close()
    
    if (len(os.listdir("./" + str(j).zfill(4) + "_textFiles")) == 0):
        os.rmdir(str(j).zfill(4) + "_textFiles")
