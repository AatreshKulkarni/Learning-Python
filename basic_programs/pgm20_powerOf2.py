# Python program to print powers of 2 for given range

# Defining a function that calculates power of 2
def powersOf2(num):
	for i in range(0,num+1):
		# Calculating the power here
		power_of_two = 2 ** i
		# Printing it
		print(f"2 to the power {i} is",power_of_two)
		

# Input a number
num = int(input("Enter a number upto which you want print power of two: "))		
# Function call
powersOf2(num)
