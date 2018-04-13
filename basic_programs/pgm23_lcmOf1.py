# To find lcm of 2 numbers

# Defing a function that calculates the lcm of 2 numbers
def lcmOf(num1,num2):
	# Checking which is the highest number and assigning it to a varoable
	if num1>num2:
		high_num = num1
	else:
		high_num = num2

	# Infinite loop until lcm of 2 numbers found
	while True:
		if high_num % num1 == 0 and high_num % num2 == 0:
			# Returning lcm value
			return high_num
		# Incrementing variable by 1 in each iteration
		high_num +=1

# Taking user input
print("Enter two numbers to calculate lcm:")
num1,num2 = int(input("Enter first number:")),int(input("Enter second number:"))
# Function call and printing returned lcm value
print("LCM of",num1,num2,"is =",lcmOf(num1,num2))