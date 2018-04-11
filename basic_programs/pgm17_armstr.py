# To check Armstrong number (Def : Sum of the cube of each digit must be eqaul to same number)

# Defining a function to check whether a given number is armstrong or not
def isArmstrong(num):
	sum = 0
	temp_num = num
	#Find sum of the cube of the each digit
	while temp_num > 0:
		digit = (temp_num % 10)
		sum = sum + (digit ** 3)
		temp_num = int(temp_num / 10)
	
	# Display the result
	if sum == num:
		print(f"{num} is armstrong")
	else:
		print(f"{num} is not armstrong")
		

# Take user input
num = int(input("Enter a number: "))
# Function call
isArmstrong(num)