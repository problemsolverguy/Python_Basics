# Tuple
"""
A tuple is an ordered collection of items that is immutable, meaning that once a tuple is created, its elements
cannot be changed. Tuples are defined using parentheses () and can contain elements of different data types.
"""
from distutils.ccompiler import new_compiler

items = ("apple", "banana", "cherry", 1, 2.5, True)
print(items)
#output: ('apple', 'banana', 'cherry', 1, 2.5, True)

print(items[-1]) #accessing last element of the tuple using negative indexing
#output: True

print((items[0])) #accessing first element of the tuple using positive indexing
#output: apple

print(items[1:4]) #accessing a range of elements from the tuple using slicing
#output: ('banana', 'cherry', 1)

#items.insert(2, "orange") #inserting an element at a specific index - this will give an error as tuple is immutable

# Dictionaries
"""
A dictionary is an unordered collection of key-value pairs that is mutable,
meaning that you can change the values associated with the keys.
Dictionaries are defined using curly braces {} and each key is separated from its value by a colon :.
"""

person = {"name": "John", "age": 30, "city": "New York"}
print(person)
#output: {'name': 'John', 'age': 30, 'city': 'New York'}

print(person["name"]) #accessing value using key
#output: John

person["age"] = 31 #changing the value associated with a key
print(person)
#output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair to the dictionary
person["country"] = "USA"
print(person)
#output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair from the dictionary
del person["city"]
print(person)
#output: {'name': 'John', 'age': 31, 'country': 'USA'}

# Creating a dictionary at runtime
# key = input("Enter the key: ")
# value = input("Enter the value: ")
# my_dict = {key: value}
# print(my_dict)

new_dict = {}

#adding key-value pairs to the dictionary
new_dict["name"] = "Alice"
new_dict["age"] = 25
new_dict["city"] = "Los Angeles"
print(new_dict)
#output: {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
