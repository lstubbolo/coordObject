import os
import cv2

SCREEN_DIMS = {'width': 800, 'height': 480}

#   returns the absolute path to the local path provided
def getFullPath(fileName):
    #   gets the directory of the file
    directory = os.path.dirname(__file__)

    #   set path to json file-> append file name to directory
    filePath = os.path.join(directory, fileName)

    return filePath


#   attempts to display the image at the provided path
def showImage(imgPath = getFullPath('source.jpg')):

    print("print displaying image... Warning, this may crash all your shit...")

    def closeWin(event, x, y, flags, param):
        print("\tClosing Image")
        cv2.destroyAllWindows()

    if(not os.path.exists(imgPath)):
        print("No Source Image, Fool! Run takeSource!")
        return

    else:
        image = cv2.imread(imgPath)
        windowName = "Source Image"

        cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
        cv2.resizeWindow(windowName, SCREEN_DIMS['width'], SCREEN_DIMS['height'])
        cv2.imshow(windowName, image)

        cv2.setMouseCallback(windowName, closeWin)
        cv2.waitKey(0)



