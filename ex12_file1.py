# Basic File Operation : Opening a file and reading containt of it

# Importing argv from sys package
from sys import argv

# Assigning arguments to respective variables
script, filename = argv

# Opening a file by name filname and assign it to txt variable
txt = open(filename)

print(f"Here is your file {filename}.")
# Reading the containts of txt
print(txt.read())

# Again asking to enter file to be read
print("Type the file name again")
# Taking user input from input method
file_again = input(">")

# Opening that file and assigning to a variable
txt_again = open(file_again)

# Reading the containts of this file
print(txt_again.read())