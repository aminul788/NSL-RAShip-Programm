# Python Program illustrating  
# numpy.sum() method  
       
import numpy as np  
       
# 2D array   
arr = [[14, 17, 12, 33, 44],    
       [15, 6, 27, 8, 19],   
       [23, 2, 54, 1, 4,]]   
   
print("\nSum of arr : ", np.sum(arr))  
print("Sum of arr(axis = 0/row) : ", np.sum(arr, axis = 0))  
print("Sum of arr(axis = 1/colum) : ", np.sum(arr, axis = 1)) 
  
print("\nSum of arr (keepdimension is True): \n", 
      np.sum(arr, axis = 1, keepdims = True))