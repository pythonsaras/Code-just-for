import cv2 ,time,pandas
from datetime import datetime


def Motion():
    motion_list=[None,None]
    time=[]
    df=pandas.DataFrame(columns=["start",'end'])
    cap=cv2.VideoCapture(0)
    first_frame=None
    while True:
        check,frame=cap.read()
        motion=0
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.GaussianBlur(gray,(21,21),0)
        if first_frame is None:
            first_frame=gray
            continue
        delta_frame=cv2.absdiff(first_frame,gray)
        threshold_frame=cv2.threshold(delta_frame,50,255,cv2.THRESH_BINARY)[1]
        threshold_frame=cv2.dilate(threshold_frame,None,iterations=2)
        (cntr,_)=cv2.findContours(threshold_frame.copy(),cv2.
            RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for contour in cntr:
            if cv2.contourArea(contour)<1000:
                continue
            motion=1
            (x,y,w,h) =cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(220,255,175),3)
        motion_list.append(motion)
        motion_list=motion_list[-2:]
        if motion_list[-1]==1 and motion_list[-2]==0:
            time.append(datetime.now())
        if motion_list[-1]==0 and motion_list[-2]==1:
            time.append(datetime.now())
        
        cv2.imshow("Motion",frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            if motion==1:
                time.append(datetime.now())
            break
    for i in range(0,len(time),2):
        df=df.append({"start":time[i],"end":time[i+1]},ignore_index=True)
    df.to_csv("time_of_motion.csv")
    cap.release()
    cv2.destroyAllWindows()
Motion()
