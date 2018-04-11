# Factorial of a number

# Method 1

def factOf(num):
	fact = 1
	if num < 0:
		print("Factorial can't be calculate")
	elif num == 0:
		print("Factorial of 0: ",fact)
	else:
		for i in range(1,num+1):
			fact = fact * i
			
		print("Factorial of {} is {}.".format(num,fact))

# Taking user input		
num = int(input("Enter a number: "))
factOf(num)
			
	
# Method 2 : Recursion

# Defining a function that calculates factorial using recursion
def factRec(num):
	fact = 1
	if num == 1:
		return num
	else:
		# Recursive function calling
		return num * factRec(num - 1)

# Taking user input
num = int(input("Enter a number: "))		

print("This is using recursion")

if num < 0:
	print("Factorial does not exist for negative number ")
elif num == 0:
	print("Factorial of o is: ",fact)
else:
	print(f"Factorial of {num} is {factRec(num)}")
		
		
		
		
		

	