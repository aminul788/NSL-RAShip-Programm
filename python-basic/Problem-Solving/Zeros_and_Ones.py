'''
    Date         : 05/11/2020
    Day          : Thursday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Zeros and Ones
    Problem link : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
''' 

import numpy as np

n = tuple(map(int, input().split()))
print (np.zeros(n, dtype = np.int))
print (np.ones(n, dtype = np.int))