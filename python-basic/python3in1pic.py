'''
    Date  : 21/10/2020
    Day   : Wednessday
    Author: Md. Aminul Islam
    Topic : Python-3 in one picture Code
'''

class Animal:
    """Animal Class documentation"""
    
    def __init__(self, can_fly = False):
        # print("Calling __init__() when instantiation")
        self.can_fly = can_fly
    
    def fly(self):
        if self.can_fly:
            print("I can fly!")
        else:
            print("I can't fly!")

class Dog(Animal):
    """This is a dog"""

    def bark(self):
        print("Woof!")


d = Dog()
d.fly()
d.bark()
