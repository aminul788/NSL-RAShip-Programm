'''
    Date         : 03/11/2020
    Day          : Tuesday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : What's Your Name?
    Problem link : https://www.hackerrank.com/challenges/whats-your-name/problem
'''

def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)