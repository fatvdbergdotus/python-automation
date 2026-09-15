more_content = """
This is some additional content
that will be written to the text file."""

# write to a text file
with open("textfile.txt", "w") as file:
    file.write("Hello, world!")
    file.write(more_content)

# read from the text file
with open("textfile.txt", "r") as file:
    content = file.read()
    print(content)

# remove last character from text file
# alternatively you can open the file for read first and then for writing
with open("textfile.txt", "r+") as file:
    # read the current content of the file
    content = file.read()
    # move the file pointer to the beginning of the file
    file.seek(0)
    # write the content back without the last character
    file.write(content[:-1])
    # truncate the file to the new length
    file.truncate()

# read from the text file (after removing the last character)
with open("textfile.txt", "r") as file:
    content = file.read()
    print(content)