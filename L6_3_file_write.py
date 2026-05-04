#Open a file in read mode and reverse its content before writing to a new file

# Open the original file for reading
with open("example.txt", "r") as original_file:
    # Read the entire content of the original file
    content = original_file.read()

    # Reverse the order of the content
    reversed_content = reversed(content)

# Open a new file for writing the reversed content
with open("reversed_example.txt", "w") as reversed_file:
    # Write the reversed content to the new file
    for char in reversed_content:
        reversed_file.write(char)

# Open the new file to verify the reversed content
with open("reversed_example.txt", "r") as reversed_file:
    # Read and print the content of the new file
    reversed_content_from_file = reversed_file.read()
    print(reversed_content_from_file)  # Output will be the reversed content of example.txt
