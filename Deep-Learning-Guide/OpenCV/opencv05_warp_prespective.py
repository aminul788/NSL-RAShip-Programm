'''
    Date   : 10/12/2020
    Day    : Thursday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Deep Learning
    Links  : https://www.youtube.com/watch?v=WQeoO7MI0Bs
    GitHub : https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects
    Topic  : OpenCV (Chapter-05): Warp Prespective
'''
import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[400,78],[547,124],[339,286],[488,330]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)