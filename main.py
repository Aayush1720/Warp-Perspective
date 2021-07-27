import cv2
import numpy as np

img = cv2.imread("download.jpg")
width,height = 250,350
pts1 = np.float32([[161,24],[242,56],[108,151],[186,180]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
while True:
    cv2.imshow("Result", imgOutput)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break