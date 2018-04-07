# Decision Making Statements in python 

# if , elif and else are the three decision making statements in pyhton

# Example for if statements
if True:
	print("I'm True")

# Example for if, elif and else
# Variable Declaration
lang = 'Python'

# prints Welcome Python 
if lang == 'Python':
	print("Welcome Python")
elif lang == 'Java':
	print("Welcome Java")
else:
	print("What is your name")


#Example for if and else
a = 10
b = 5

# prints the heighest of a and b
if a > b:
	print(f"Heighest number is {a}")  #Here we are using string formatting f" {var_name}"
else:
	print(f"Heighest number is {b}")