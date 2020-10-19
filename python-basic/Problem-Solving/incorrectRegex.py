'''
    Date         : 16/10/2020
    Day          : Friday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Incorrect Regex
    Problem link : https://www.hackerrank.com/challenges/incorrect-regex/problem
'''

import re

for i in range(0,int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')