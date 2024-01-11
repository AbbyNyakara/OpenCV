import cv2 as cv

#some examples of color spaces include: RGB, Grayscale etc

img = cv.imread("Photos/park.jpg")
#cv.imshow("Park", img)

# Convert the image to grayscale: 
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Conversting BGR TO HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow("HSV", hsv_img)

cv.waitKey(0)
cv.destroyAllWindows()