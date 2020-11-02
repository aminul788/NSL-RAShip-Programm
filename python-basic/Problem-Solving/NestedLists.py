'''
    Date         : 02/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Nested Lists
    Problem link : https://www.hackerrank.com/challenges/nested-list/problem
'''

if __name__ == '__main__':

    mark_sheet = []
    for _ in range(int(input())):
        mark_sheet.append([input(), float(input())])

    second_highest = sorted(list(set(marks for name, marks in mark_sheet)))[1]

    print('\n'.join([a for a,b in sorted(mark_sheet) if b == second_highest]))
