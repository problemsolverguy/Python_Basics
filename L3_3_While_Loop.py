# While loop
"""
A while loop is a control flow statement that allows you to execute a block of code repeatedly as long as
a certain condition is true. The syntax of a while loop in Python is as follows:
"""

# syntax of while loop
"""
while condition:
    # block of code to be executed repeatedly as long as the condition is true
"""

# Example of while loop
count = 0
while count < 5:
    print(count)
    count += 1
#output: 0 1 2 3 4

# Example of while loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Count is greater than or equal to 5.")
#output: 0 1 2 3 4 Count is greater than or equal to 5.

# Example of while loop with break
count = 0
while count < 5:
    print(count)
    if count == 3:
        break
    count += 1
#output: 0 1 2 3

# Example of while loop with continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
#output: 1 2 4 5

# Example of while loop with break and continue
# to Write a program to print all the numbers from 10 to 1 except 7 and break at 4 using while loop with break and continue
count = 10
while count > 0:
    if count == 7:
        count -= 1
        continue
    if count == 4:
        break
    print(count)
    count -= 1
#output: 10 9 8 6 5
