'''
    Date         : 16/10/2020
    Day          : Friday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Triangle Quest
    Problem link : https://www.hackerrank.com/challenges/python-quest-1/problem
'''

# ## using mathematical logic
for i in range(1,int(input())):
    print((i*(10**i -1)//9)) 

# ## using string
# for i in range(1,int(input())):
#     print(i*str(i))

# ## using loop 
# n = int(input("Enter a number: "))
# for i in range(1,n):
#     num = 1
#     for j in range(1, i+1):
#         print(num, end="")
#         num += 1
#     print("\r") # ending line after each row 



