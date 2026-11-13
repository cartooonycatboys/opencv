# import cv2
# img=cv2.imread("pickachu.png")
# star_point=(0,0)
# end_point=(250,250)
# color=(0,255,0)
# thickness=9
# img=cv2.line(img,star_point,end_point,color,thickness)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# import cv2
# img=cv2.imread("pickachu.png")
# star_point=(5,5)
# end_point=(220,220)
# color=(255,0,0)
# thickness=2
# img=cv2.rectangle(img,star_point,end_point,color,thickness)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# img=cv2.imread("pickachu.png")
# center_cordinates=(120,50)
# radius=20
# color=(0,0,255)
# thickness=(-1)

# image=cv2.circle(img,center_cordinates,radius,color,thickness)
# cv2.imshow("circle",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
img=cv2.imread("pickachu.png")
font=cv2.FONT_HERSHEY_SIMPLEX
org=(50,50)
fontScale=1
color=(0,0,255)
thickness=2
text=cv2.putText(img,"OpenCV",org,font,fontScale,color,thickness,cv2.LINE_AA)
cv2.imshow("text",img)
cv2.waitKey()
cv2.destroyAllWindows()