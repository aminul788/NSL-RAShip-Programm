'''
    Date         : 19/10/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Classes: Dealing with Complex Numbers
    Problem link : https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
    Solve-1      : Using own logic
'''

from math import pow
class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self, no):
        a = self.real + no.real
        b = self.imaginary + no.imaginary
        return Complex(a,b)
        
    def __sub__(self, no):
        a = self.real - no.real
        b = self.imaginary - no.imaginary
        return Complex(a,b)
        
    
    def __mul__(self, no):
        a = self.real*no.real-self.imaginary*no.imaginary
        b = no.imaginary*self.real+self.imaginary*no.real
        return Complex(a,b)
        
    def __truediv__(self, no):
        x = no.real**2+no.imaginary**2
        a = (self.real*no.real+self.imaginary*no.imaginary)/x
        b = (-no.imaginary*self.real+self.imaginary*no.real)/x
        return Complex(a,b)
        
    def mod(self):
        a = pow(self.real**2+self.imaginary**2, 0.5)
        b = 0
        return Complex(a,b)
            

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')