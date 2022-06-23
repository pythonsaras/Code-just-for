import cv2
from cv2 import VideoCapture
cap=VideoCapture(0)
cascade="F:\\python\\cascade\\haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(cascade)
while True:
    success,img=cap.read()
    faces=faceCascade.detectMultiScale(img,1.2,4)
    for (x,y,w,h) in faces:
        RIO=img[y:y+h,x:x+w]
        blur=cv2.GaussianBlur(RIO,(91,91),0)
        img[y:y+w,x:x+h]=blur
    if faces==():
        cv2.putText(img,"no face here",(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cv2.imshow("Face blur",img)
    if cv2.waitKey(1)& 0xff==ord('q'):
       break
cap.release()
cv2.destroyAllWindows()
        


