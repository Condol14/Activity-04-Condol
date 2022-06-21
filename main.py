import cv2 as cv
filePath='primo.jpg'
windowTitle = 'Omen'
readCvImage = cv.imread(filePath, 1)
cv.imshow(windowTitle, readCvImage)
cv.waitKey(0)
cv.destroyAllWindows()