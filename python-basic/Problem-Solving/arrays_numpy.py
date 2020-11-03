'''
    Date         : 03/11/2020
    Day          : Tuesday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Arrays (numpy)
    Problem link : https://www.hackerrank.com/challenges/np-arrays/problem
'''
import numpy

def arrays(arr):
    arr = numpy.array(arr, float)
    return numpy.flipud(arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)