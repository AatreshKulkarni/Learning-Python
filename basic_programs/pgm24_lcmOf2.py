# Method 2: Calculating lcm using lcm(n1,n2) = (n1 * n2) / gcd(n1,n2)

# Defining a function that calculates the lcm
def lcmOf(num1,num2):
	
	temp_num1 = num1
	temp_num2 = num2
	# Calculating gcd to calculate lcm
	while num2:
		num1,num2 = num2,num1%num2

	# This is gcd of 2 numbers
	gcd = num1
	# Calculating lcm using gcd value
	lcm = int((temp_num1 * temp_num2) / gcd)
	
	# Returning lcm
	return lcm

# Enter 2 numbers
print("Enter 2 numbers to calculate lcm:")
num1,num2 = int(input("Enter First number:")),int(input("Enter Second number:"))
print("LCM of",num1,"and",num2,'is =',lcmOf(num1,num2))