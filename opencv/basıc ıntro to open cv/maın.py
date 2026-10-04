# import cv2
# import os
# saved_directory="C:/Users/90544/Desktop/JetLearn/opencv/basic intro to open cv"
# #img=cv2.imread("qwerty.png")
# img=cv2.imread("qwerty.png",0)

# #cv2.IMREAD_COLOR (1) => Specify to load the image in color
# #cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
# #cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

# cv2.imshow("Pikachu Image", img)
# cv2.imwrite("Pikachu in black and white.png",img)
# print("succesfuly saved")
# cv2.waitKey(delay=5000)
# cv2.destroyAllWindows()
import cv2
img=cv2.imread("qwerty.png",1)
B, G, R=cv2.split(img)
cv2.imshow("original", img)
cv2.waitKey(delay=5000)
cv2.imshow("Blue Saturation Image",B)
cv2.waitKey(delay=5000)
cv2.imshow("Green Saturation Image",G)
cv2.waitKey(delay=5000)
cv2.imshow("Red Saturation Image",R)
cv2.waitKey(delay=5000)
cv2.destroyWindow("original")
cv2.destroyWindow("Blue Saturation Image")
cv2.destroyWindow("Red Saturation Image")
cv2.destroyWindow("Green Saturation Image")