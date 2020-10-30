'''
    Date         : 29/10/2020
    Day          : Thursday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Find the Runner-Up Score! 
    Problem link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    ## solve-1: using general concept
    # arr = list(arr)
    # z = max(arr)
    # while max(arr) == z:
    #     arr.remove(max(arr))
    # print(max(arr))

    ## solve-2: using set 
    ## we need to sort because of negative value as set can not sort it
    print(sorted(list(set(arr)))[-2])
