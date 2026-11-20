import cv2
import numpy as np

image=cv2.imread("coin.png")

if image is None:
    print("Error")
else:
    output=image.copy()
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray, (9, 9), 2)

    circles=cv2.HoughCircles( blurred,cv2.HOUGH_GRADIENT,dp=1,minDist=50,param1=50,param2=30, minRadius=1,maxRadius=40)
    if circles is not None:
        circles=np.uint16(np.around(circles))
        for i in circles[0, :]:
            center=(i[0], i[1])
            radius=i[2]
            cv2.circle(output, center, radius, (0, 255, 0), 2)
            cv2.circle(output, center, 2, (0, 0, 255), 3)

    cv2.imshow("Detected Circles", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()