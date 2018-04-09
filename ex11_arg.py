# Passing arguments to the Python

# From sys we are importing argv 
from sys import argv

# Assigning arguments passed to the pscript to respective variables
script, first, second, third = argv

# Printing those variables
print("The script is called: ", script)
print("Your first variable is: ",first) 
print("Your second variable is: ",second)
print("Your third variable is: ",third)