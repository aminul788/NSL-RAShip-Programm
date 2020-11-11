'''
    Date         : 11/11/2020
    Day          : Wednessday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Sum and Prod
    Problem link : https://www.hackerrank.com/challenges/np-sum-and-prod/problem
''' 

import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

arr_sum = np.sum(arr, axis = 0)
arr_prod = np.prod(arr_sum)

print(arr_prod)