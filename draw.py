import cv2 as cv
import numpy as np

# Create a blank image: 

height = 500
width = 500
channels = 3 # For a color image, use 3 channels (B, G, R)

blank_image = np.zeros((height, width, channels), np.uint8)

# The line below gives a colored image: 
#blank_image[:] = [255, 1, 59]

# Drawing a rectangle: 
"""
cv.rectangle(blank_image, (0, 0), (100, 250), (255, 0, 0), thickness=2 )

cv.imshow("rectangle", blank_image)
"""
# Drawing a circle
# Draw a circle
center = (250, 250)
radius = 50
color = (200, 100, 100)  # BGR format
thickness = 2
cv.circle(blank_image, center, radius, color, thickness)

# Display the image
cv.imshow("circle", blank_image)
cv.waitKey(0)
cv.destroyAllWindows()
