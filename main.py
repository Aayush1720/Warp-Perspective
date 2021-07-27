import cv2
import numpy as np

img = cv2.imread("3d.jpg")
width,height = 400,150
pts1 = np.float32([[202,54],[976,362],[55,185],[869,539]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
while True:
    cv2.imshow("Result", imgOutput)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break