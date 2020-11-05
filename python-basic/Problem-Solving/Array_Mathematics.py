'''
    Date         : 05/11/2020
    Day          : Thursday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Array Mathematics
    Problem link : https://www.hackerrank.com/challenges/np-array-mathematics/problem?h_r=next-challenge&h_v=zen
'''

import numpy as np

n, m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b).astype(int))
print(np.mod(a,b).astype(int))
print(np.power(a,b).astype(int))

