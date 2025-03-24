import cv2

img = cv2.imread('lean.jpg', 1)
print(img)

cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite('sahil_lena.png', img)
"Changing file name function"

"cv2.imread_color - (1) loads a color image"
"cv2.imread-grayscale (0)loads image in grayscale"
"cv2.imread_unchanged (-1) loads image as such including alpha channel"
