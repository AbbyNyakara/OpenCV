import cv2 as cv

# read the image that you want to resize: 

img2 = cv.imread("Photos/cat_large.jpg")

# Resize this image: 
# This helps to reduce the computational strenght required to process the image: 

#resized_img2 = cv.resize(img2, (new_width, new_height))

scale_x = 0.3  # 30% of the original size in x
scale_y = 0.3 

resized_img2 = cv.resize(img2, dsize=None,fx=scale_x, fy=scale_y )

# display the resized image: 

cv.imshow("Resized Image", resized_img2)

cv.waitKey(0)
cv.destroyAllWindows()

