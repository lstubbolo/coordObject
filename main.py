from CoordList import *
from CoordObj import *
from Image_Functions import *
#   This file is just for testing the coordObj and coordList objects

tempList = coordList()
tempList.printSet()
print("_____________________")

# tempList.wipeList()

# tempList.addObject(coordObj('topSquare2x2', (100, 100), (300, 300)))

# addCrop(tempList, 'imgGrid.jpg')

showImage(tempList, 'imgGrid.jpg')

# cropSource(tempList, 'imgGrid.jpg')

tempList.printSet()
