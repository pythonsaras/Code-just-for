# import  cv2
# import matplotlib.pyplot as plt
# import cvlib
# from cvlib.object_detection import draw_bbox
# from cvlib import detect_common_objects

# img=cv2.imread("CAR.jpg")
# bbox ,label,conf=detect_common_objects(img,0.5)
# output=draw_bbox(img,bbox,label,conf)
# plt.imshow(output)
# plt.show()
# print("Number of cars is "+ str(label.count('car')))
import cvlib as cv
from cvlib.object_detection import draw_bbox
img="CAR.jpg"
bbox, label, conf = cv.detect_common_objects(img)

output_image = draw_bbox(img, bbox, label, conf)