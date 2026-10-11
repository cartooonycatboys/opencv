import cv2 
import numpy as np
image1=cv2.imread("boy.png")
#image2=cv2.imread("pickachu.png")
#0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
#weightedsum=cv2.addWeighted(image1,0.5,image2,0.4,0)
#cv2.imshow("wightedimage",weightedsum)

#sub=cv2.subtract(image1,image2)
#cv2.imshow("substracted Image",sub)
image=cv2.imread("pickachu.png",1)
kernel=np.ones((5,5),np.uint8)
image=cv2.erode(image,kernel)
cv2.imshow("Eroded Image", image)
# resized=cv2.resize(image1,(500,250))
# cv2.imshow("reduceImage",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
