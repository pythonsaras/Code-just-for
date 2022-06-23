import cv2,random,time
face_cascade=cv2.CascadeClassifier("F:\\python\\cascade\\haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier("F:\\python\\cascade\\haarcascade_smile.xml")
video=cv2.VideoCapture(0)
num=0
def smile_meter(frame,x1,y1):
    global num
    if num>4000:
        x=str(random.randint(0,100))
        font=cv2.FONT_HERSHEY_SIMPLEX
        color=(255,0,255)
        text=cv2.putText(frame,"Your smile is ",(int(x1)+15,int(y1)-70),font,1,color,4,cv2.LINE_AA)
        text=cv2.putText(frame,x+" %",(int(x1)+50,int(y1)-20),font,1,color,4,cv2.LINE_AA)
        time.sleep(15)
        return num
    
    else:
        x=str(random.randint(0,100))
        font=cv2.FONT_HERSHEY_SIMPLEX
        color=(255,0,255)
        text=cv2.putText(frame,"Smile meter ",(int(x1)+15,int(y1)-70),font,1,color,4,cv2.LINE_AA)
        text=cv2.putText(frame,x+" %",(int(x1)+50,int(y1)-20),font,1,color,4,cv2.LINE_AA)
        num+=5
        return num
        
        
while True:
    _,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.3,5)
    for x,y,w,h in  face:
        cv2.rectangle(frame,(x,y),(x+(w+20),y+(h-300)),(0,255,255),-1)
        smile=smile_cascade.detectMultiScale(gray,1.8,25)
        for x1,y1,w1,h1 in  smile:
            cv2.rectangle(face,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)
            smile_meter(frame,x,y)
    cv2.imshow('Cam Start',frame)
    if cv2.waitKey(10)==ord('q'):
        break
video.release()
cv2.destroyAllWindows