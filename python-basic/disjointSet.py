'''
    Date   : 28/10/2020
    Day    : Wednessday
    Author : Md. Aminul Islam
    Subject: Data Structure
    Topic  : Disjoint Set
    links  : http://www.shafaetsplanet.com/?p=763
'''

element = 5
par = [None] * (element + 1)

def makeset(n):
    par[n] = n

for i in range(1, element+1):
    makeset(i)

print(makeset(i))
