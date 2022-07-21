import numpy as np
import mediapipe as mp
import cv2
import time

class HandDetection():
  def __init__(self,static_image_mode=False,
               max_num_hands=2,
               model_complexity=1,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5) :
    self.static_image_mode=static_image_mode
    self.max_num_hands=max_num_hands
    self.model_complexity=model_complexity
    self.min_detection_confidence=min_detection_confidence
    self.min_tracking_confidence=min_tracking_confidence
    self.mpHand=mp.solutions.hands
    self.hands=self.mpHand.Hands()
    self.mpDraw=mp.solutions.drawing_utils

  def hand(self,img,draw=True):
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=self.hands.process(imgRGB)
    # print(results.multi_han)d_landmarks
    if results.multi_hand_landmarks:
      for handlms in results.multi_hand_landmarks:
        for id ,lm in enumerate(handlms.landmark):
          h,w,c =img.shape
          cx,cy=int(lm.x*w),int(lm.y*h)
          
          cv2.circle(img,(cx,cy),2,(255,255,0),cv2.FILLED)
          if draw:
            self.mpDraw.draw_landmarks(img,handlms,self.mpHand.HAND_CONNECTIONS)
    return img
def main():
  pTime=0
  cap=cv2.VideoCapture(0)
  detect=HandDetection()
  while True:
    sucess,img=cap.read()
    img=detect.hand(img)
    cTime=time.time() 
    fps=1/(cTime-pTime) 
    pTime=cTime 
    cv2.putText(img,f'FPS:{int(fps)}',(20,70),
        cv2.FONT_HERSHEY_PLAIN,3,(255,125,13),2)
    cv2.imshow("img",img)
    # if cv2.waitKey(1)==ord('q'):
    #   break 
    cv2.waitKey(1)
  cap.release()
  cv2.destroyAllWindows()
if __name__=="__main__":
  main()