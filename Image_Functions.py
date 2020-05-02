import os
import cv2
from time import sleep
from CoordList import coordList
SCREEN_DIMS = {'width': 800, 'height': 480}


#   CRASHES ON MAC DO NOT RUN
#   returns the absolute path to the local path provided
def getFullPath(fileName):
    #   gets the directory of the file
    directory = os.path.dirname(__file__)

    #   set path to json file-> append file name to directory
    filePath = os.path.join(directory, fileName)

    return filePath


#   kills all cv2 windows

#   CRASHES ON MAC DO NOT RUN
#   attempts to display the image at the provided path
def showImage(imgPath, cropObjs):
    print("print displaying image... Warning, this may crash all your shit...")
    imgPath = getFullPath(imgPath)

    if (not os.path.exists(imgPath)):
        print("No Source Image, Fool! Run takeSource!")
        return

    else:
        image = cv2.imread(imgPath)
        windowName = "Source Image"

        def closeWin(event, x, y, flags, param):
            print("\tClosing Image")
            sleep(1)
            #cv2.destroyWindow(windowName)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
        cv2.startWindowThread()

        cv2.setMouseCallback(windowName, closeWin)
        #cv2.resizeWindow(windowName, SCREEN_DIMS['width'], SCREEN_DIMS['height'])

        #   add rectangles to the window
        for obj in cropObjs:
            cv2.rectangle(image, obj.topL, obj.botR, (0, 255, 0), 3)


        cv2.imshow(windowName, image)
        cv2.waitKey(1)


