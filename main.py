from CoordList import *
from CoordObj import *
from Image_Functions import *
#   This file is just for testing the coordObj and coordList objects

tempList = coordList()
tempList.printSet()


temp = -1
print("_____________________")

# tempList.printSet()

cropped = {'crop1.jpg', 'crop2.jpg', 'crop3.jpg'}

for entry in tempList:
    print(entry.topL, entry.botR)

showImage('kittens.jpg', tempList)
