####### Read An image #################
# We use cv2.imread() function to read an image.
# The image should be placed in the current working directory 
# or else we need to provide the absoluate path.

import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('flower.jpg',0)


######## Display an image ############
# To display an image in a window, use cv2.imshow() function.

#Display the image
cv2.imshow('image',img)
#key binding function
cv2.waitKey(0)
#Destroyed all window we created earlier.
cv2.destroyAllWindows()





######## Write an image ##############
# Use the function cv2.imwrite() to save an image.

# First argument is the file name, second argument is the image you want to save.

# cv2.imwrite('messigray.png',img)


import numpy as np
import cv2

#Read the Image
# Load an color image in grayscale
img = cv2.imread('flower.jpg',0)

#Display the image
cv2.imshow('image',img)

#key binding function
k = cv2.waitKey(0)

# wait for ESC key to exit
if k == 27:
   cv2.destroyAllWindows()
# wait for 's' key to save and exit
elif k == ord('s'):
   cv2.imwrite('flower.jpg',img)
   cv2.destroyAllWindows()