# Read a file and print its content line by line

# create an object of file
file = open("example.txt")

file.readline()  # read the first line of the file
file.readline()  # read the second line of the file

file.close()  # close the file after reading

file = open("example.txt")  # open the file again for reading

# read the file line by line using a loop
for line in file:
    print(line)  # print each line of the file

file.close()  # close the file after reading

file = open("example.txt")  # open the file again for reading

# read the entire content of the file at once
content = file.read()
print(content)  # print the entire content of the file

file.close()  # close the file after reading

file = open("example.txt")  # open the file again for reading

#read the file and store it in a list
file.seek(0)  # move the file pointer back to the beginning of the file
lines = file.readlines()  # read the file and store it in a list
print(lines)  # print the list of lines

# read the file and store it in a list using a loop
file.seek(0)  # move the file pointer back to the beginning of the file
lines = []
for line in file.readlines():  # read the file line by line
    print("Using for loop, File contents are : " + line)  # print the list of lines

# close the file after any operation
file.close()
