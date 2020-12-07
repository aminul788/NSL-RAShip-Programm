'''
    Date   : 07/12/2020
    Day    : Monday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Deep Learning
    Links  : https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
    Topic  : OpenCV
        1. Converting an image to grayscale
        2. Edge detection
        3. Thresholding a grayscale image
        4. Detecting, counting, and drawing contours
        5. Conducting Erosions and Dilations
        6. Masking and bitwise operations
'''

# import the necessary packages
import argparse
import imutils
import cv2

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())

# load the input image (whose path was supplied via command line
# arguments) and display the image to our screen
# image = cv2.imread(args["image"])
image = cv2.imread("tetris_blocks.png")     
cv2.imshow("Image", image)
cv2.waitKey(0)

## 1. CONVERTING AN IMAGE TO GRAYSCALE
# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)


## 2. EDGE DETECTION
# applying edge detection we can find the outlines of objects in
# images
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

## 3. THRESHOLDING A GRAYSCALE IMAGE
# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

## 4. DETECTING, COUNTING, AND DRAWING CONTOURS 
# find contours (i.e., outlines) of the foreground objects in the 
# thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

# loop over the contours
for c in cnts:
    # draw each contour on the output image with a 3px thick purple
    # outline, then display the output contours one at a time
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

# draw the total number of contours found in purple
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
    (240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)


## 5. CONDUCTING EROSIONS AND DILATIONS
# we apply erosions to reduce the size of foreground objects
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

# similarly, dilations can increase the size of the ground objects
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

## 6. MASKING AND BITWISE OPERATIONS
# a typical operation we may want to apply is to take our mask and
# apply a bitwise AND to our input image, keeping only the masked
# regions
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)