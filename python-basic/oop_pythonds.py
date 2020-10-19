'''
    Date   : 19/10/2020
    Day    : Monday
    Author : Md. Aminul Islam
    Subject: Basic Python
    Topic  : OOP(Pythonds)
    links  : https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
'''

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)


myf = Fraction(3,5)
myf.show()