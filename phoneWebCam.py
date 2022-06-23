import requests
import cv2
import numpy as np
import imutils
# Not working 

url="http://192.168.1.8:8080/shot.jpg"

while True:
    img_resp=requests.get(url)
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    img=cv2.imdecode(img_arr,-1)
    img=imutils.resize(img,width=480,height=480)
    cv2.imshow("Cam",img)
    if cv2.waitKey(10000)==ord('q'):
     break 
cv2.release()
cv2.destroyAllWindows()


