'''
    Date         : 09/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Min and Max
    Problem link : https://www.hackerrank.com/challenges/np-min-and-max/problem
''' 

import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

arr_min = np.min(arr, axis = 1)
arr_max = np.max(arr_min)

print(arr_max)