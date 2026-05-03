# Inheritance
"""
Inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child or subclass)
 to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass).
 This promotes code reusability and establishes a natural hierarchical relationship between classes.
"""

# Defining a parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Defining a child class that inherits from the parent class
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Creating an instance of the Dog class
my_dog = Dog("Buddy")
# Accessing the inherited attribute and method
print(f"My dog's name is {my_dog.name}.")  # Output: My dog's name is Buddy.
print(f"My dog says: {my_dog.speak()}")  # Output: My dog says: Woof!

# Defining another child class that inherits from the parent class and have another method
class Cat(Animal):
    def speak(self):
        return "Meow!"

    def eats(self):
        return "Drools..."

# Creating an instance of the Cat class
my_cat = Cat("Whiskers")
# Accessing the inherited attribute and methods
print(f"My cat's name is {my_cat.name}.")  # Output: My cat's name is Whiskers.
print(f"My cat says: {my_cat.speak()}")  # Output: My cat says: Meow!
print(f"My cat eats: {my_cat.eats()}")  # Output: My cat eats: Drools...

