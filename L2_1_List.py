#List Datatype
#List is a collection which is ordered and changeable. Allows duplicate members.
#List is written with square brackets.

items = ["apple", "banana", "cherry", 1, 2.5, True]
print(items)
#output: ['apple', 'banana', 'cherry', 1, 2.5, True]

print(items[-1]) #accessing last element of the list using negative indexing
#output: True

print((items[0])) #accessing first element of the list using positive indexing
#output: apple

print(items[1:4]) #accessing a range of elements from the list using slicing
#output: ['banana', 'cherry', 1]

items.insert(2, "orange") #inserting an element at a specific index
print(items)
#output: ['apple', 'banana', 'orange', 'cherry', 1, 2.5, True]

items.append("grape") #adding an element at the end of the list
print(items)
#output: ['apple', 'banana', 'orange', 'cherry', 1, 2.5, True, 'grape']

items[5] = "kiwi" #changing the value of an element at a specific index
print(items)
#output: ['apple', 'banana', 'orange', 'cherry', 1, 'kiwi', True, 'grape']
