# Classes in Python

"""
A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created
from the class will have. An object is an instance of a class, and it can have its own unique values for the
attributes defined in the class.
"""

# Defining a simple class, class variable and class method
class Person:
    name = "John Doe"  # Class variable

    def greet(self):
        # This method prints a greeting message using the class variable 'name'.
        print(f"Hello, my name is {self.name}!")

# Creating an instance of the Person class
person1 = Person()
# Calling the greet method on the instance
person1.greet()
print(person1.name)
