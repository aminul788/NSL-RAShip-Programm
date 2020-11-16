'''
    Date         : 16/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Dot and Cross
    Problem link : https://www.hackerrank.com/challenges/np-dot-and-cross/problem
''' 

import numpy as np

n = int(input())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

ans = np.dot(a,b)

print(ans)