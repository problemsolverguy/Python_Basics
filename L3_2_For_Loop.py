# For Loop

for i in range(10):
    print(i)
#output: 0 1 2 3 4 5 6 7 8 9

for i in range(1, 11):
    print(i)
#output: 1 2 3 4 5 6 7 8 9 10

for i in range(1, 11, 2):
    print(i)
#output: 1 3 5 7 9

for i in range(10, 0, -1):
    print(i)
#output: 10 9 8 7 6 5 4 3 2 1

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
#output: 2 4 6 8 10

for i in range(1, 11):
    if i % 2 != 0:
        print(i)
#output: 1 3 5 7 9
for i in range(1, 11):
    if i % 2 == 0:
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))
#output: 1 is odd, 2 is even, 3 is odd, 4 is even, 5 is odd, 6 is even, 7 is odd, 8 is even, 9 is odd, 10 is even
