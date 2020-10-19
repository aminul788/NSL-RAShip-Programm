'''
    Date   : 19/10/2020
    Day    : Monday
    Author : Md. Aminul Islam
    Subject: Basic Python
    Topic  : OOP(Inheritance)
'''

## super class
class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def attack(self):
        print("I am attacking....")


## sub class of Monster
class Fogthing(Monster):
    def make_sound(self):
        print('Grrrrrrrrrr\n')

class Mournsnake(Monster):
    def make_sound(self):
        print('Hisssssshhhhhhh\n')

# fogthing = Fogthing("Fogthing", "Yellow")
# fogthing.attack()
# fogthing.make_sound()

# mournsnake = Mournsnake("Mournsnake", "Red")
# mournsnake.attack()
# mournsnake.make_sound()


### multiple inheritance
class A:
    def where(self):
        print("I am from class A")

class B:
    def where(self):
        print("I am from class B")

class C(A, B):
    pass


an_instance_of_c = C()
an_instance_of_c.where()
print(C.mro())