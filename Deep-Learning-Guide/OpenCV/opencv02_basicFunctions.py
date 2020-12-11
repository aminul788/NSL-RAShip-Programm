'''
    Date   : 10/12/2020
    Day    : Thursday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Deep Learning
    Links  : https://www.youtube.com/watch?v=WQeoO7MI0Bs
    GitHub : https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects
    Topic  : OpenCV (Chapter-02): Basic Functions
'''

import cv2
import numpy as np

img = cv2.imread("resources/messi.jpeg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)