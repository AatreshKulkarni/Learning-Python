# To find the square root of a number

# Method 1
# Defining a function
def sqRootOf(num):
	squared_num = num ** 0.5
	print(f"Square root of {num} is: ",squared_num)		# Calculating and printing square root
	
# Taking input from the user and assgning it to variable
number = int(input("Enter a number to square it: "))
# Function call
sqRootOf(number)	




# Method 2
# Importing math module to use sqrt method
import math 

# Defining a function which calculates square root of the number
def sqrtOf(num):
	return math.sqrt(num)
	
# Taking input
number = int(input("Enter a number: "))
# Calling sqrtOf()
squared_num = sqrtOf(number) 
print(f"Square root of {number} is: ",squared_num)