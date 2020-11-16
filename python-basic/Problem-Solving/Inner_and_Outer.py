'''
    Date         : 16/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Inner and Outer
    Problem link : https://www.hackerrank.com/challenges/np-inner-and-outer/problem
''' 

import numpy as np

arr1 = np.array([input().split()], int)

arr2 = np.array([input().split()], int)

print(np.inner(arr1, arr2)[0][0])
print(np.outer(arr1, arr2))