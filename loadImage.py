import cv2

img = cv2.imread("/image.jpg", 1)
cv2.imshow("Image", img)
cv2.destroyAllWindows()
