'''
    Date   : 19/10/2020
    Day    : Monday
    Author : Md. Aminul Islam
    Subject: Basic Python
    Topic  : OOP(Class Method)
'''
### Class Method
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
    

square = Rectangle.new_square(5)
print(square.calculate_area())

### Static Method
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @staticmethod
    def validate_tiopping(topping):
        if topping == "pineapple":
            raise ValueError("No Pineapples!") 
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_tiopping(i) for i in ingredients):
    pizza = Pizza(ingredients)
