''' 
    Date         : 04/11/2020
    Day          : Wednessday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Shape and Reshape
    Problem link : https://www.hackerrank.com/challenges/np-shape-reshape/problem
'''

import numpy as np

arr = np.array(input().split())
newarr = arr.reshape(3, 3)
newarr = newarr.astype('i')
print(newarr)


# a=np.array(list(map(int,input().split())))
# a.shape=(3,3)
# print(a)