import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def FindFace(img):
    

while True:
    _, img = cap.read()
    cv2.imshow("Output", img)
    cv2.waitKey(1)
