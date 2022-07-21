import numpy as np
import mediapipe as mp
import cv2
import time

class Face_Detection():
  def __init__(self,min_detection_confidence=0.5):
    self.min_detection_confidence=min_detection_confidence
    
    self.mpface=mp.solutions.face_detection
    self.faces=self.mpface.FaceDetection()
    self.mpDraw=mp.solutions.drawing_utils

  def face(self,img,draw=True):
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    self.results=self.faces.process(imgRGB)
    # print(results.multi_han)d_landmarks
    bboxs=[]
    if self.results.detections:
        for id ,detection in enumerate(self.results.detections):
            bboxC=detection.location_data.relative_bounding_box
            ih,iw,ic=img.shape
            bbox=int(bboxC.xmin*iw),int(bboxC.ymin*ih),\
                int(bboxC.width*iw),int(bboxC.height*ih)
            cv2.rectangle(img,bbox,(255,0,244),2)
            cv2.putText(img,f'{int(detection.score[0]*100)}%',(bbox[0],bbox[1]-20),
                cv2.FONT_HERSHEY_PLAIN,3,(255,125,13),2)
            bboxs.append([id,bbox,detection.score])
    return bboxs,img
def main():
  pTime=0
  cap=cv2.VideoCapture(0)
#   cap=cv2.VideoCapture("E://python//random code//Chal hat behan ki lodi_ Dil Mera hai tod gayi----_new hariyanvi song_breakup song masup----(720P_HD).mp4")
  detect=Face_Detection()
  while True:
    sucess,img=cap.read()
    _,img=detect.face(img)
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