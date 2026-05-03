# Constructors in class
"""
A Constructor is a special method in a class that is automatically called when an object of the class is created.
It is used to initialize the attributes of the object. In Python, the constructor method is defined
using the __init__() method.
"""

# Defining a class with a constructor
class Calculator:
    def __init__(self, first_number, second_number):
        # This constructor initializes the attributes 'a' and 'b' with the values passed as arguments.
        self.a = first_number
        self.b = second_number

    def add(self):
        # This method returns the sum of 'a' and 'b'.
        return self.a + self.b

    def subtract(self):
        # This method returns the difference of 'a' and 'b'.
        return self.a - self.b

# Creating an instance of the Calculator class with specific values
calc = Calculator(10, 5)
# Calling the add and subtract methods and printing the results
print(f"The sum of {calc.a} and {calc.b} is: {calc.add()}")
#output: The sum of 10 and 5 is: 15
print(f"The difference of {calc.a} and {calc.b} is: {calc.subtract()}")
#output: The difference of 10 and 5 is: 5

# Another instance of the Calculator class with different values
calc2 = Calculator(20, 8)
# Calling the add and subtract methods and printing the results
print(f"The sum of {calc2.a} and {calc2.b} is: {calc2.add()}")
#output: The sum of 20 and 8 is: 28
print(f"The difference of {calc2.a} and {calc2.b} is: {calc2.subtract()}")
#output: The difference of 20 and 8 is: 12
