# Converting Decimal to Binary using recursion 

# Defining a function that converts Decimal number to Binary number
def dectobin(num):
	if num > 1:
		# Recursive function call
		dectobin(num // 2)

	# Printing binary equivalent of decimal
	print(num % 2,end = '')

# Taking user input
decnum = int(input("Enter a decimal number:"))
dectobin(decnum)