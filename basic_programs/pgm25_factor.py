# Find the factors of a Number

# Defining a function which calculates factors of a number 
def factorsOf(num):
	print("Factors of ",num)
	# Logic to calculate fact
	for i in range(1,num+1):
		if num % i == 0:
			print(i)

# Input a number
num = int(input("Enter a number to calculates its factors:"))
# Function call
factorsOf(num)