# Numbers in Python. 
# Basically There are two types of Numbers 1.Intergers(int), 2.Float(float) 

# Integers 	Example
# Even and odd numbers upto 50

for num in range(0,51):
	# Prints even numbers upto 50
	if num % 2 == 0:
		print("Even: ",num)
		
	else:
		print("Odd: ",num)

		
# Floating Point number example
# Area and circumference of a circle. Radius given

# Defining Radius
radius = 5  

# Area of the Circle 
import math                               # Importing math package to use pi value
area = math.pi * radius ** 2			  # Here ** refers to power of operation
print("Area of the Circle: ",area)		  # Printing Area of the circle, Answer will be in Floating Point

# Circumference of the Circle
circumference = 2 * math.pi * radius					# Calculating Circumference of the circle
print("Circumference of the Circle: ",circumference)	#Printing Circumference of the circle, Result will be in floating point