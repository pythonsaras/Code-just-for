import  cv2
import numpy as np
import math
import os
import webbrowser as wb

print("Enter full wensite for :")
print(" Fingers")
fingers2=input()
print(" Fingers")
fingers3=input()
print(" Fingers")
fingers4=input()

tabs=0
count=0
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    rot,img=cap.read()
    cv2.rectangle(img,(400,400),(100,100),(0,255,0),0)
    crop_img=img[100:400,100,400]
    grey=cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
    value=(35,35)
    blurred=cv2.GaussianBlur(grey,value,0)
    _,thresh1=cv2.threshold(blurred,127,255,
                            cv2,cv2.THRESH_BINARY_INV*cv2.THRESH_OTSU)
    cv2.imshow("thresholded",thresh1)
    
    (version,_,_)=cv2.__version__.split('.')
    if version==3:
        image,contours,hierachy=cv2.findContours(thresh1.copy(),\
            cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    elif version==2:
            image,contours,hierachy=cv2.findContours(thresh1.copy(),cv2.RETR_TREE,\
                            cv2.CHAIN_APPROX_NONE)

                 
    cnt=max(contours,key=lambda x:cv2.contourArea(x))
    x,y,w,h=cv2.boundingRect(cnt)
    cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
    hull=cv2.convexHull(cnt)
    drawing=np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[cnt],0,(0,0,255),0)
    hull=cv2.convexHull(cnt,returnPoints=False)
    
