'''
    Date   : 10/12/2020
    Day    : Thursday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Deep Learning
    Links  : https://www.youtube.com/watch?v=WQeoO7MI0Bs
    GitHub : https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects
    Topic  : OpenCV (Chapter-05): Joining Images
'''
import cv2
import numpy as np

img = cv2.imread("resources/messi.jpeg")


imgHor = np.hstack((img,img,img))
imgVer = np.vstack((img,img))


cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)