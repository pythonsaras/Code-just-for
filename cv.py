from matplotlib.pyplot import gray
import numpy as np
import cv2
from cv2 import VideoCapture


cap=VideoCapture("F:\python\Car Drift Racing.mp4")
def rescaleFrame(frame,scale=0.70):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

def changeRes(width,height):
    cap.set(3,width)
    cap.set(4,height)

# blank=np.zeros((500,500,3))
# # cv2.imshow("black",blank)
# blank[:]=0,255,255
# # cv2.rectangle(blank,(0,0),(250,200),(0,0,255))
# # cv2.circle(blank,(250,250),200,(10,20,200),3)
# # cv2.line(blank,(200,200),(400,400),(30,20,40),5)



def drawText(frame,text):

    cv2.putText(frame,text,(200,200),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,240),6)
# # drawText(blank,"hello")

# cv2.imshow("black",blank)
# cv2.waitKey(0)


while True:
    _,frame=cap.read()
    frame_r=rescaleFrame(frame,0.90)
    gray=cv2.cvtColor(frame_r,cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame",gray)
    blur=cv2.GaussianBlur(gray,(7,7),cv2.BORDER_DEFAULT)
    cv2.imshow("blur",blur)
    if cv2.waitKey(1000) or 0xFF==ord("q"):
        break 
# cap.release()
cv2.destroyAllWindows()