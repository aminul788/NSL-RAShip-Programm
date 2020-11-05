'''
    Date         : 05/11/2020
    Day          : Thursday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Eye and Identity
    Problem link : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
''' 

'''If set to the string ‘1.13’ enables 1.13 legacy printing mode. 
This approximates numpy 1.13 print output by including a space 
in the sign position of floats and different behavior for 0d arrays. 
If set to False, disables legacy mode.

So if you're trying to get an output set by previous numpy versions just add:
    
    np.set_printoptions(sign=' ')
    numpy.set_printoptions(legacy='1.13')

need to write before print numpy expressions.'''




import numpy as np

n, m = map(int, input().split(' '))
np.set_printoptions(sign=' ') ##there is error in the test case so we need to add whitespace
arr = np.eye(n,m)

print(arr)