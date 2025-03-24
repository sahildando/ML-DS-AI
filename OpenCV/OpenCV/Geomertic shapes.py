import numpy as np
import cv2

# Read the image in grayscale mode
img = cv2.imread('HappyFish.jpg', 1)


# Draw a red line from top-left to bottom-right
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# Show the image with the line
cv2.imshow('image', img)

# Wait for any key to be pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
