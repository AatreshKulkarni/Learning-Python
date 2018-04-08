# Function in python

# Syntax:
# def name_of_function(arg1,arg2):
#    '''
#   This is where the function's Document String (docstring) goes
#    '''
    # Do stuff here
    # Return desired result
	
	
# Simple Function Example

def hello():
	print("Hello")
	
# Call the function
hello()


# Addition Function

def add_num(num1,num2):    # Function can take arguments
	return num1 + num2
	
# Call the function
print(add_num(2,4))


# Function to check prime number

# Importing math to use sqrt() method inside funtion
import math

def is_prime(num):
    
    if num % 2 == 0 and num > 2: 	# To check number is even(2 is the only even prime number)
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):	# Logic to calculate prime number
        if num % i == 0:
            return False
    return True
		
# Calling isprime() function
print(is_prime(6))