# Functions
"""
Functions are reusable blocks of code that perform a specific task. They allow you to break down your code into smaller,
more manageable pieces, and can be called multiple times throughout your program.
"""

# Defining a function
def greet():
    # This function prints a greeting message.
    print("Hello, welcome to Python programming!")
# Calling the function
greet()

# Function with parameters
def greet_person(name):
    # This function takes a name as a parameter and prints a personalized greeting.
    print(f"Hello, {name}! Welcome to Python programming!")
# Calling the function with an argument
greet_person("Alice")

# Function with return value
def add_numbers(a, b):
    # This function takes two numbers as parameters and returns their sum.
    return a + b
# Calling the function and storing the result
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")

# Function with default parameters
def greet_with_default(name="Guest"):
    # This function takes a name as a parameter and prints a personalized greeting.
    # If no name is provided, it defaults to "Guest".
    print(f"Hello, {name}! Welcome to Python programming!")
# Calling the function without an argument
greet_with_default()
# Calling the function with an argument
greet_with_default("Bob")

# Function with variable number of arguments
def greet_multiple(*names):
    # This function takes a variable number of names as parameters and prints a greeting for each.
    for name in names:
        print(f"Hello, {name}! Welcome to Python programming!")
# Calling the function with multiple arguments
greet_multiple("Alice", "Bob", "Charlie")

# Function with keyword arguments
def greet_with_keyword(name, greeting):
    # This function takes a name and a greeting as parameters and prints a personalized greeting.
    print(f"{greeting}, {name}! Welcome to Python programming!")
# Calling the function with keyword arguments
greet_with_keyword(name="Alice", greeting="Hi")
greet_with_keyword(greeting="Hello", name="Bob")

# Example of using a function to determine the time of day based on user input
user  = 10
# Morning: 5-12, Afternoon: 12-18, Night: 18-22
if user in range(5,12):
    print("Good Morning")
elif user in range(12,18):
    print("Good Afternoon")
elif user in range(18,22):
    print("Good Night")
else:
    print("Good Night")
