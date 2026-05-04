# File Read and Write
"""
A file is a named location on disk to store related information. It is used to permanently store data in a non-volatile
memory (like hard disk). In Python, you can read from and write to files using built-in functions.
"""

file = open("example.txt", "w")  # Open a file for writing (creates the file if it doesn't exist)
file.write("Hello, World!\n")  # Write a line to the file
file.write("Welcome to Python programming.\n")  # Write another line to the file
file.close()  # Close the file

file = open("example.txt", "r")  # Open the file for reading
content = file.read()  # Read the entire content of the file
print(content)  # Output: Hello, World!\nWelcome to Python programming.\n
file.close()  # Close the file

# read and readline methods
file = open("example.txt", "r")  # Open the file for reading
line1 = file.readline()  # Read the first line
line2 = file.readline()  # Read the second line
print(line1)  # Output: Hello, World!
print(line2)  # Output: Welcome to Python programming.
file.close()  # Close the file

# Using with statement to handle files (automatically closes the file)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!\nWelcome to Python programming.\n
