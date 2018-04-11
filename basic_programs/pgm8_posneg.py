# Check if a number is Positive, Negative or 0

# Defining a function 
def toCheckNum(num):
	# print num is Negative
	if num < 0:
		print("Entered number is Negative")
	# print num is Positive
	elif num > 0:
		print("Entered number is Positive")
	# print num is 0
	else:
		print("Entered number is 0")
		

# Input a number
number = int(input("Enter a number: "))
# Function call
toCheckNum(number)
		