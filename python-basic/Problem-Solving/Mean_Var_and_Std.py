'''
    Date         : 09/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Mean, Var, and Std
    Problem link : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
''' 

import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

np.set_printoptions(legacy='1.13')
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.std(arr))
