'''
    Date   : 19/10/2020
    Day    : Monday
    Author : Md. Aminul Islam
    Subject: Basic Python
    Topic  : OOP(Encapsulation/Data Hiding)
'''

### weakly private
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    
    def push(self, value):
        self._hiddenlist.insert(0, value)
    
    def pop(self):
        return self._hiddenlist.pop(-1)
    
    def _show_list(self):
        return self._hiddenlist


queue = Queue([1,2,3])
print(queue._hiddenlist)

queue.push(0)
print(queue._hiddenlist)

queue.pop()
print(queue._hiddenlist)

print(queue._show_list())


### strongly private
class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()

## if we call normally we can't acces the element __egg
# print(s.__egg)

## if we use _ClassName before element then we can access the element 
print(s._Spam__egg)