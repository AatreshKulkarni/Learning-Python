# Calculating sum of n natural numbers: formula Sum = n(n+1)/2

# Defining a function calculates sum of natural numbers
def sumOfNat(num):
	# Logic of the program
	sum = num * (num+1) / 2
	# Printing Sum
	print(f"Sum of {num} natural numbers: ",int(sum))
	
	
# Taking user input
num = int(input("Enter a number upto which sum to be calculated:"))
sumOfNat(num)