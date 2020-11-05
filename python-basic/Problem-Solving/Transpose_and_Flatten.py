'''
    Date         : 05/11/2020
    Day          : Thursday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Transpose and Flatten
    Problem link : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problemTranspose and Flatten
''' 
import numpy as np


N, M = map(int,input().split())

arr = np.array([input().strip().split() for _ in range(N)], int)

## another way
# a = []
# for i in range(N):
#     row = input().split()
#     a.append(row)
# arr = np.array(a, int)
    

print(np.transpose(arr))
print(arr.flatten())
