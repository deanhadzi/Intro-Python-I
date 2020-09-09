"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

filename = 'src/foo.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents) 

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

filename = 'src/bar.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')
    file_object.write('I love learing new things in Python.')

with open(filename) as file_object:
    contents = file_object.read()

print(contents) 
