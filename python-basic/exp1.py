# n = 1

# my_num = [n,2,3]

# things = ["Numbers", 0, my_num, 4.56]

# print(things)



# for i in range(10,100,10):
# 	if i == 30:
# 		continue
# 	if i == 80:
# 		break

# 	print(i)

# print("for loop with break and continue")


# def my_fun(x = None):
# 	if x:
# 		return x * x
# 	else:
# 		return x
# a = input("enter a number: ")

# b = int(a)

# print(my_fun())
# print(my_fun(b))


# import numpy as np
# import cv2
# # Load an color image in grayscale
# img = cv2.imread('flower.jpg',1)


# ######## Display an image ############
# # To display an image in a window, use cv2.imshow() function.

# #Display the image
# cv2.imshow('image',img)
# #key binding function
# cv2.waitKey(0)
# #Destroyed all window we created earlier.
# cv2.destroyAllWindows()


import cv2 
import numpy as np 
import matplotlib.pyplot as plt  
# % matplotlib qt 
# This is a magic command to display in an external window 
  
image = cv2.imread("flower.jpg", 1) 
# Loading the image 
  
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1) 
bigger = cv2.resize(image, (1000, 1000)) 
  
# stretch_near = cv2.resize(image, (780, 540),  
#                interpolation = cv2.INTER_NEAREST) 
  
  
Titles =["Original", "Half", "Bigger"] 
images =[image, half, bigger] 
count = 3
  
for i in range(count): 
    plt.subplot(2, 2, i + 1) 
    plt.title(Titles[i]) 
    plt.imshow(images[i]) 
  
plt.show()