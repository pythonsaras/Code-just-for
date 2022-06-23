import numpy as np
import mediapipe as mp
import cv2
import time


cap=cv2.VideoCapture("chand_wala_mukhda_leke_chalo.mp4")

pTime=0
while True:
  sucess,img=cap.read() 
  cTime=time.time() 
  fps=1/(cTime-pTime) 
  pTime=cTime 
  cv2.putText(img,f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,125,13),2)
  cv2.imshow("img",img)
  if cv2.waitKey(10000)==ord('q'):
    break 
cap.release()
cv2.destroyAllWindows()
