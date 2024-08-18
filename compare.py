import os
import pathlib
byteArr = []
roms = []
sizes = []
workingDir = input("What is the current working directory? ")
if os.path.isfile("../" + workingDir + "/compare.py") or os.path.isfile("../" + workingDir + "/compare.exe"):
    print("")
else:
    raise Exception("Directory not found!")
roms.append(input("Input file: "))
roms.append(input("Input file: "))
romCount = 0
linesWritten = 0
byteArr.append([])
byteArr.append([])
matching = True
byteLoc = 0
romNum = 0
matchingBytes = 0
byteLoc_file = open("byteloc.dat", "w")
matchingByte_file = open("bytes.dat", "w")
for files in range(len(roms)):
    print(roms[files])
    for byte in pathlib.Path(roms[files]).read_bytes():
        byteArr[files].append(byte)
for arrs in range(len(byteArr)):
    sizes.append(len(byteArr[arrs]))
print(sizes)
for sizes in range(len(byteArr)):
    for thugs in range(len(byteArr)):
        if len(byteArr[sizes]) <= len(byteArr[thugs]):
            sizeCheck = len(byteArr[sizes])
        elif len(byteArr[sizes]) > len(byteArr[thugs]):
            sizeCheck = len(byteArr[thugs])
    break
logfile = open("log.dat", "w")
bytesWritten = 0
while byteLoc < sizeCheck:
    matching = True
    romNum = 0
    for romNum in range(len(byteArr)):
        if romNum + 1 < len(byteArr):
            if byteArr[romNum][byteLoc] != byteArr[romNum + 1][byteLoc]:
                matching = False
                break
        else:
            continue
    if matching == True:
        print("Byte " + str(hex(byteLoc)) + " matches on all files!")
        if bytesWritten == 0:
            logfile.write("Byte " + str(hex(byteLoc)) + " matches on all files!")
        else:
            logfile.write("\n" + "Byte " + str(hex(byteLoc)) + " matches on all files!")
        if matchingBytes == 0:
            byteLoc_file.write(str(byteLoc))
            matchingByte_file.write(str(byteArr[0][byteLoc]))
        else:
            byteLoc_file.write("\n" + str(byteLoc))
            matchingByte_file.write("\n" + str(byteArr[0][byteLoc]))
        matchingBytes += 1
    elif matching == False:
        print("Byte " + str(hex(byteLoc)) + " does not match on all files!")
        if bytesWritten == 0:
            logfile.write("Byte " + str(hex(byteLoc)) + " does not match on all files!")
            bytesWritten += 1
        else:
            logfile.write("\n" + "Byte " + str(hex(byteLoc)) + " does not match on all files!")
    byteLoc += 1
    print(str(matchingBytes) + "/" + str(byteLoc) + " bytes match!")
logfile.close()
matchingByte_file.close()
byteLoc_file.close()
