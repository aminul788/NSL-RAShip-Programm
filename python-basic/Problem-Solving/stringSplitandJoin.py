''' 
    Date         : 02/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : String Split and Join
    Problem link : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
'''

def split_and_join(line):
    line = line.split(" ")
    return  "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)