'''
    Date         : 02/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Merge the Tools!
    Problem link : https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

def merge_the_tools(string, k):
    n = len(string)

    for i in range(0, n, k):
        s = ""
        for j in string[i:i+k]:
            if j in s:
                continue
            else:
                s += j
        print(s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

