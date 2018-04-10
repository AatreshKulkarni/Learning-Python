# To solve quadratic equation of a number

# Importing math module
import math

# Define a function to solve quadratic equation with 3 arguments
def solQuadEq(num1, num2, num3):
	
	sol1 = (-num2 + (math.sqrt((num2 ** 2) - (4 * num1 * num3))))/(2 * num1)
	sol2 = (-num2 - (math.sqrt((num2 ** 2) - (4 * num1 * num3))))/(2 * num1)
	
	print("First Solution is : ",sol1)
	print("Second solution is: ",sol2)
	
	
# Input 3 constants of quadratic equation
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
# Function call
solQuadEq(num1,num2,num3)