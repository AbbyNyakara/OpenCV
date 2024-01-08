# For identifying the parts where the image brightness changes rapidly. 

import cv2 as cv

img = cv.imread("Photos/park.jpg")

# Edge cascade: 
edge_image = cv.Canny(img, 124, 133)

cv.imshow("Edge cascade", edge_image)

cv.waitKey(0)
cv.destroyAllWindows()