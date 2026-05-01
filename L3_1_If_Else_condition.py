# If Else Condition
"""
If condition is used to execute a block of code if a specified condition is true.
If else condition is used to execute a block of code if a specified condition is true,
and another block of code if the condition is false.
"""

# syntax of if condition
"""
if condition:
    # block of code to be executed if the condition is true
"""

# syntax of if else condition
"""
if condition:
    # block of code to be executed if the condition is true
else:
    # block of code to be executed if the condition is false
"""

# Example of if condition
age = 18
if age >= 18:
    print("You are eligible to vote.")
#output: You are eligible to vote.

# Example of if else condition
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#output: You are not eligible to vote.

# Example of if else condition with multiple conditions
age = 65
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
#output: You are a senior citizen.
