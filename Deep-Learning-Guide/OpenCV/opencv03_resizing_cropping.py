'''
    Date   : 10/12/2020
    Day    : Thursday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Deep Learning
    Links  : https://www.youtube.com/watch?v=WQeoO7MI0Bs
    GitHub : https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects
    Topic  : OpenCV (Chapter-03): Resizing and Cropping
'''
import cv2 
import numpy as np

img = cv2.imread("resources/lambo.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]    # [height, width]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)