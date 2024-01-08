import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# Convert to grayscale: 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale park", gray)


# Save the grayscale image
#cv.imwrite('grayscale_park.jpg', gray)

cv.waitKey(0)
cv.destroyAllWindows()