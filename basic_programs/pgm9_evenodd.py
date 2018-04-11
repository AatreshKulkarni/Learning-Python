# Check if number is even or odd

# Defining a function to check even or odd
def checkEvenOrOdd(num):
	# even
	if num % 2 == 0:
		print("Number is even")
	# odd
	else:
		print("Number is odd")
	
	
	
# Input a number
num = int(input("Enter a number to check even or odd: "))
# Function call
checkEvenOrOdd(num)
