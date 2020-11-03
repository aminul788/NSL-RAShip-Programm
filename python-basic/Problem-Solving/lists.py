'''
    Date         : 03/11/2020
    Day          : Tuesday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Lists
    Problem link : https://www.hackerrank.com/challenges/python-lists/problem
'''

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "(" + ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)
   
    # N = int(input())
    # l = []
    # for _ in range(N):
    #     s = input().split()
    #     cmd = s[0]
    #     args = s[1:]

    #     if cmd == 'insert':
    #         l.insert(int(args[0]),int(args[1]))
    #     elif cmd == 'print':
    #         print(l)
    #     elif s[0] == 'remove':
    #         l.remove(int(args[0]))
    #     elif cmd == 'append':
    #         l.append(int(args[0]))
    #         print(l)
    #     elif  cmd == 'sort':
    #         l.sort()
    #     elif cmd == 'pop':
    #         l.pop()
    #     elif cmd == 'reverse':
    #         l.reverse()