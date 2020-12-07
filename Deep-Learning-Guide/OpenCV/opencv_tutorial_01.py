'''
    Date   : 07/12/2020
    Day    : Monday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Deep Learning
    Links  : https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
    Topic  : OpenCV
        1. Loading and displaying an image
        2. Accessing individual pixels
        3. Array Clicing and Cropping
        4. Resizing images
        5. Rotating an image
        6. Smoothing an image
        7. Drawing on an image
        8. Writing on an image
'''

# import the necessary packages
import imutils
import cv2

## LOADING AND DISPALING AN IMAGE
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("jp.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# display the image to our screen --we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

## ACCESSING INDIVIDUAL PIXLES
# access the RGB pixels located at x=50, y=100, keep in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

## ARRAY CLICING AND CROPING
# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=253, y=11 at ending at x=360,y=130
roi = image[11:130, 253:360]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

## RESIZING IMAGES
# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resizing width
# to be 300px but compute the new height based on the aspect ration
r = 300 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resized", resized)
cv2.waitKey(0)

# manually computing the aspect ratio can be a pain so let's us the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

## ROTATING AN IMAGE
# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# OpenCV dosen't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

## SMOOTHING AN IMAGE
# apply a GaussianBlur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

## DDROWING ON AN IMAGE
# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (253, 11), (360, 130), (0, 0, 255), 2)
cv2.imshow("Recatangle", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300, y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output =  image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

## WRITING ON AN IMAGE
# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25),
    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)