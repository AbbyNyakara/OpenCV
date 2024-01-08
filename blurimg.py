import cv2 as cv

img = cv.imread("Photos/park.jpg")

blur_img = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Blurred Image", blur_img)

cv.waitKey(0)
cv.destroyAllWindows()