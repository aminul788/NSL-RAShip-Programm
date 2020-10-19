'''
    Date         : 19/10/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Classes: Dealing with Complex Numbers
    Problem link : https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
    Solve-2      : Using a built in class complex
'''

'''
Description of the solve:
---------------------------------------------------------------------------
It's a cheat and maybe a little joke. complex is built in to Python. 
So this just implements a class Complex by implementing each operation 
using the same operation in complex!

There is one bit of usefulness here. class Complex(complex) That says
that the new class Complex is a subclass of complex. So all Complex 
objects is a complex. It looks like that gives them __init__ automatically
    without any work.
'''

import math

class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex(complex.__truediv__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))

    def __str__(self):
        return '{0.real:.2f}{0.imag:+.2f}i'.format(self+0) 
    ## They state it in the spec: If real part is zero and imag is non-zero, print: 0.00-x.xxi
    ## so I use .format(self+0)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
