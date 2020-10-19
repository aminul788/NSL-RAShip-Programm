'''
    Date   : 19/10/2020
    Day    : Monday
    Author : Md. Aminul Islam
    Subject: Basic Python
    Topic  : OOP(Operator Overloading)
'''

# class MyNUm():
#     def __init__(self, value):
#         self.value = value
    
#     def __add__(self, other):
#         return (self.value * 2) + (other.value * 2)


# a = MyNUm(2)
# b = MyNUm(3)

# c = a + b
# print(c)

class MyInt():
    def __init__(self, value):
        self.__value = value
    
    def __int__(self):
        return self.__value
    
    def __add__(self, other):
        return self.__value + int(other) * int(other)

    def __iadd__(self, other):
        return self.__value + int(other) * int(other)

a = MyInt(2)
b = MyInt(3)

c = a + b
print(c)

d = MyInt(2)
d += MyInt(3)
print(d)