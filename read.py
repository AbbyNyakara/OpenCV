import cv2 as cv

# Reading images: 

img = cv.imread("Photos/cat_large.jpg")
cv.imshow("Cat", img)

cv.waitKey(0)



# Reading videos:
# Create a VideoCapture Object: Use the cv2.
# VideoCapture class to create a video capture object.
# You need to specify the path to your video file.
# If you want to capture video from a webcam, you pass an integer (usually 0 or -1 for the default camera).
cap = cv.VideoCapture("Videos/dog.mp4")

# Check if camera is opened: 

if not cap.isOpened():
    print("Unable to open the video")
    exit()

# Read the Video: 
# Use a loop to read the video frame by frame.
# The read() method returns a boolean
# (True if the frame is read correctly) and the frame itself.

#While True- creates an infinite loop

while True:
    isTrue, frame = cap.read()
    if not isTrue:
        print("Cant retrieve the frame. Exiting...")
        break


#Display Each Frame: Use cv2.imshow() to display each frame.
#You can add a delay with cv2.waitKey() and check for a specific key
#press to break the loop (commonly the 'q' key is used for quitting).
#Display the Frame:
    cv.imshow('Frame', frame)

    # Press Q on keyboard to exit
    # A way to exit out of the while loop 
    #cv2.waitKey(25) is a function that waits for a specified amount of time (in this case, 25 milliseconds) for a key event.
    if cv.waitKey(25) & 0xFF==ord('q'):
        break


#When everything is done, release the videocapture image:
cap.release()

# Closes all the frames
cv.destroyAllWindows()