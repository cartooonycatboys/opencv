# import cv2
# image=cv2.imread("pickachu.png")
# #cv2.imshow("orgininal image",image)

# #use cvt color function to grey scale the image
# #gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# # Using averaging of pixels method to grayscale the image
# # Without using the library to grayscale the image
# (row,col)=image.shape[:2]

# for i in range(row):
#     for j in range(col):
#         gray_value=int(sum(image[i,j])/3)
#         image[i,j]=[gray_value,gray_value,gray_value]

# cv2.imshow("qwerty",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
img=cv2.imread("pickachu.png")
(height,width)=img.shape[:2]
center=(width//2, height//2)
angle=45
scale=1.0
rotation_matrix=cv2.getRotationMatrix2D(center,angle,scale)
rotated_img=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow("Orginal Image",img)
cv2.imshow("Rotated Image",rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()