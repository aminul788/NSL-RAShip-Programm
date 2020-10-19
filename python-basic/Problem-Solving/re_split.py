'''
    Date         : 19/10/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Re.split()
    Problem link : https://www.hackerrank.com/challenges/re-split/problem
'''
import re

regex_pattern = r"[,.]"

print("\n".join(re.split(regex_pattern, input())))