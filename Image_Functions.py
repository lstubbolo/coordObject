import os
import cv2
from time import sleep

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
def showImage(imgPath):
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

        cv2.imshow(windowName, image)
        cv2.waitKey(1)

#   CRASHES ON MAC DO NOT RUN
# calls the show image for every item in the list
def displayCropped(cropList):
    for img in cropList:
        showImage(img)

def displaySafe(imgPath):
    def closeWin(event, x, y, flags, param):
        if not(event == 0):
            print('Event: ', event)
            print(event)
            print()

        if not (flags == 0):
            print("flags")
            print(flags)
            print()

        if not (param == None):
            print("param")
            print(param)
            print()

        # cv2.destroyWindow(windowName)
        #cv2.destroyWindow("Source Image")


    imgPath = getFullPath(imgPath)

    image = cv2.imread(imgPath)
    windowName = "Source Image"

    cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(windowName, closeWin)

    cv2.imshow(windowName, image)
    cv2.waitKey(0)