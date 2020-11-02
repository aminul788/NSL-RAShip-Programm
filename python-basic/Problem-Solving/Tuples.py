'''
    Date         : 30/10/2020
    Day          : Friday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Tuples
    Problem link : https://www.hackerrank.com/challenges/python-tuples/problem
'''

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))