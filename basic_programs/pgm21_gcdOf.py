# To Find GCD of 2 numbers

# Defining a function that calculates the gcd of 2 numbers
# Euclidean Method
def gcdOf(num1,num2):
	
	while num2:
		num1,num2 = num2,num1%num2

	return num1

# Enter 2 numbers
num1,num2 = int(input("Enter First number:")),int(input("Enter Second number:"))
print("GCD of",num1,num2,'is =',gcdOf(num1,num2))
