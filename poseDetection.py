import re
import numpy as np
import mediapipe as mp
import cv2
import time
class poseDetector():
  def __init__(self,
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    enable_segmentation=False,
    smooth_segmentation=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5):
    self.static_image_mode=static_image_mode
    self.model_complexity=model_complexity
    self.smooth_landmarks=smooth_landmarks
    self.enable_segmentation=enable_segmentation
    self.smooth_segmentation=smooth_segmentation
    self.min_detection_confidence=min_detection_confidence
    self.min_tracking_confidence=min_tracking_confidence
    
    self.mpPose=mp.solutions.pose
    self.pose=self.mpPose.Pose(self.static_image_mode,
              self.model_complexity,
              self.smooth_landmarks,
              self.enable_segmentation,
              self.smooth_segmentation,
              self.min_detection_confidence,
              self.min_tracking_confidence)
    self.mpDraw=mp.solutions.drawing_utils

  def findPose(self,img,draw=True):
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=self.pose.process(imgRGB)
    # print(results.multi_han)d_landmarks
    
    if results.pose_landmarks:
      for id ,lm in enumerate(results.pose_landmarks.landmark):
        h,w,c =img.shape
        cx,cy=int(lm.x*w),int(lm.y*h)
        
        cv2.circle(img,(cx,cy),10,(255,255,0),cv2.FILLED)
      if draw:  
        self.mpDraw.draw_landmarks(img,results.pose_landmarks,
        self.mpPose.POSE_CONNECTIONS)
    return img  

def main():
  pTime=0
  cap=cv2.VideoCapture("E://python//random code//Chal hat behan ki lodi_ Dil Mera hai tod gayi----_new hariyanvi song_breakup song masup----(720P_HD).mp4")
  detector=poseDetector()
  while True:
    sucess,img=cap.read()
    img=detector.findPose(img) 
    cTime=time.time() 
    fps=1/(cTime-pTime) 
    pTime=cTime 
    cv2.putText(img,f'FPS:{int(fps)}',(20,70),
        cv2.FONT_HERSHEY_PLAIN,3,(255,125,13),2)
    cv2.imshow("img",img)
    cv2.waitKey(1)
  cap.release()
  cv2.destroyAllWindows()


if __name__=="__main__":
  main()
