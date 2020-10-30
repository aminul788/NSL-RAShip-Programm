'''
    Date         : 29/10/2020
    Day          : Thursday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : List Comprehensions
    Problem link : https://www.hackerrank.com/challenges/list-comprehensions/problem
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    valid_list = [[a,b,c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n]
    print(valid_list)