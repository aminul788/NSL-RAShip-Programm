'''
    Date  : 16/10/2020
    Day   : Friday
    Author: Md. Aminul Islam
    Topic : Object Oriented Programming  
'''

## The blueprint to create monsters
class Monsters:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack





## Create some real monsters
foghting = Monsters("Black", 5)
mournsnake = Monsters("Yellow", 4)
tangleface = Monsters("Red", 3)


#Check whether those monsters got different existence in memory or not
print('I have ' +str(foghting.heads) + ' heads and i\'m  ' + foghting.color)
print('I also have ' +str(mournsnake.heads) + ' heads and i\'m  ' + mournsnake.color)
print('I got ' +str(tangleface.heads) + ' heads and i\'m  ' + tangleface.color)