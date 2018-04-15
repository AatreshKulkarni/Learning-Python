# Calculating sum of natural numbers using recursion

# Defining a function that recursively calculates sum of natural numbers
def sumNatRec(num):

	if num <= 1:
		return num
	# Recursive call to sumNatRec 
	else:	 
		return num + sumNatRec(num-1) 
	

# Taking user input 
num = int(input("Enter a number: "))
if num < 0:
	print("Enter positive number")
else:
	print(f"Sum of first {num} natural number = ",sumNatRec(num))