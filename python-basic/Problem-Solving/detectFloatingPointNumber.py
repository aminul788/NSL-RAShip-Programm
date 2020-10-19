'''
    Date         : 19/10/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Detect Floating Point Number
    Problem link : https://www.hackerrank.com/challenges/introduction-to-regex/problem
''' 

import re

for i in range(0,int(input())):
    # print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]*$', input())))
    print(bool(re.match("^[+-]?\d*\.\d+$", input())))

    
