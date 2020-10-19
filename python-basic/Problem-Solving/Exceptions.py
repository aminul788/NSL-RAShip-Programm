'''
    Date         : 16/10/2020
    Day          : Friday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Exceoption
    Problem link : https://www.hackerrank.com/challenges/exceptions/problem
'''


# for i in range(int(input())):
#     try:
#         a,b = map(int,input().split()) 
#         print(a//b)
#     except ZeroDivisionError as e:
#         print("Error Code:", e)
#     except ValueError as e:
#         print("Error Code:", e)


## using base case
for i in range(int(input())):  
    try:
        a,b = map(int,input().split())
        print(a//b)
    except BaseException as e:
        print("Error Code:",e)
    