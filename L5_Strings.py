# String Operations

# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")  # Output: Full Name: John Doe

# Repetition
greeting = "Hello! "* 3
print(greeting)  # Output: Hello! Hello! Hello!

# Slicing
text = "Python Programming"
print(text[0:6])  # Output: Python
print(text[7:18])  # Output: Programming

# String Methods
# Uppercase
print(text.upper())  # Output: PYTHON PROGRAMMING
# Lowercase
print(text.lower())  # Output: python programming
# Replace
print(text.replace("Python", "Java"))  # Output: Java Programming
# Split
print(text.split())  # Output: ['Python', 'Programming']
# Join
words = ["Python", "Programming"]
joined_text = " ".join(words)
print(joined_text)  # Output: Python Programming

# String Formatting
name = "Alice"
age = 30
# Using f-string
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.
# Using format method
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Alice and I am 30 years old.

# String Length and Count
print(len(text))  # Output: 18
print(text.count("o"))  # Output: 2

# String Membership
print("Python" in text)  # Output: True
print("Java" in text)  # Output: False

# String Stripping
text_with_spaces = "   Hello, World!   "
print(text_with_spaces.strip())  # Output: Hello, World!

# String Indexing
print(text[0])  # Output: P
print(text[-1])  # Output: g

# String Immutability
# Strings in Python are immutable, which means that once a string is created, it cannot be changed.
# However, you can create a new string based on the original string.
original_string = "Hello"
new_string = original_string + " World"
print(original_string)  # Output: Hello
print(new_string)  # Output: Hello World
