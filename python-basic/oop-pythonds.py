'''
    Date  : 20/10/2020
    Day   : Tuesday
    Author: Md. Aminul Islam
    Topic : Object Oriented Programming: pythonds 
'''

def gcd(m,n):
    while m % n != 0:
        temp = m
        m = n
        n = temp % n
    return n

class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)


    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum // common, newden // common)
    
    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    
    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum
    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >  secondnum

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum ==  secondnum
    

# f1 = Fraction(1,4)
# f2 = Fraction(1,2)
# f3 = f1 + f2
# print(f3)

x = Fraction(1,2)
y = Fraction(2,3)
print('add:', x+y)
print('sub:', x-y)
print('mul:', x*y)
print('div', x/y)
print('is equal', x == y)
print(x, '>', y, ':', x>y)
print(x, '<', y,':', x<y)

