# Second method to find GCD of 2 numbers

def gcdOf(num1,num2):

	if num1 < num2:
		small_num = num1
	else:
		small_num = num2

	for i in range(1,small_num+1):
		if num1 % i == 0 and num2 % i == 0:
			gcd = i
    
	return gcd

# Taking User Input
num1,num2 = int(input("Enter First number:")),int(input("Enter Second number:"))
gcd = gcdOf(num1,num2)
print(f"GCD of {num1} and {num2} is:",gcd)