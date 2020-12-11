'''
    Date   : 10/12/2020
    Day    : Thursday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Deep Learning
    Links  : https://www.youtube.com/watch?v=WQeoO7MI0Bs
    GitHub : https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects
    Topic  : OpenCV (Chapter-01)
        1. Display an image
        2. Import a video
        3. Uses of Webcam
'''

import cv2
print("package imported")

# Display an image
img = cv2.imread("resources/lena.png")

cv2.imshow("Output", img)
cv2.waitKey(0)

# Import a video
cap = cv2.VideoCapture("resources/testVideo.mp4") 

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# # Uses of Webcam
# cap = cv2.VideoCapture(0) ## 0 is the id of camera. here 0 is default id of webcame
# cap.set(3, 640)     ## width,(3 is the id of width, 640 is size)
# cap.set(4, 480)     ## height,(4 is the id of height, 480 is size)
# cap.set(10, 100)    ## set the brightness,(10 is the id)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
