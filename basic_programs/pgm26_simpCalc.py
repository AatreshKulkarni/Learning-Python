# Simple calculator

# Addition
def add(num1,num2):
	return num1 + num2

# Subtraction
def sub(num1,num2):
	return num1 - num2

# Multiplication
def mul(num1,num2):
	return num1 * num2

# Division
def div(num1,num2):
	return num1 / num2

ch = 1
# Taking input from the user
while ch == 1:
	print("Addition press 1")
	print("Subraction press 2")
	print("Multiplication press 3")
	print("Division press 4")

	choice = int(input())

	print("Enter 2 numbers")
	num1,num2 = int(input("Enter num1:")),int(input("Enter num2:"))

	# Calls add func
	if choice == 1:
		print(f"Addition of {num1} & {num2} is",add(num1,num2))
	# Calls sub func
	elif choice == 2:
		print(f"Subraction of {num1} & {num2} is",sub(num1,num2))
	# Calls mul func
	elif choice == 3:
		print(f"Multiplication of {num1} & {num2} is",mul(num1,num2))
	# Calls div func
	elif choice == 4:
		# Asking num2 until num2 not equal to 0
		while num2 == 0:
			num2 = int(input("Enter num2 other than zero"))
		print(f"Division of {num1} & {num2} is",int(div(num1,num2)))
	else:
		print("Invalid input")
	# Asking user Does he/she wants to continue calculation 	
	ch = int(input("Do you want to continue Press Yes:1 No:0? :"))

