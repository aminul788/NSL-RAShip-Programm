'''
    Date  : 23/10/2020
    Day   : Friday
    Author: Md. Aminul Islam
    Topic : Data Structure: Stack  
'''

class Stack:

    def __init__(self, max_size):   # initialize a stack of max_size
        self.top_pointer = -1       # keep track of top element using this
        self.stack = [None for x in range(max_size)]     # create a list of max size

    def push(self, new_element):
        self.top_pointer = self.top_pointer + 1         #Move the pointer
        self.stack[self.top_pointer] = new_element      #Add the new_element to the top
    
    def pop(self):
        last_element = self.stack[self.top_pointer]
        self.top_pointer = self.top_pointer - 1         #MOVE the pointer
        return last_element                             #POP the last element
    
    def peek(self):
        return self.stack[self.top_pointer]
    
    def is_empty(self):
        return top.pointer == -1




