'''
    Date         : 19/10/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Group(), Groups() & Groupdict()
    Problem link : https://www.hackerrank.com/challenges/re-group-groups/problem
'''

import re

pattern =  r"([a-z0-9])\1"

match = re.search(pattern, input())

print(match.group(1) if match else -1)
