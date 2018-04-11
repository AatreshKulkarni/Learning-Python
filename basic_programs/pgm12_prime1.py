# Check given number is prime or not

# Defining a function isPrime
def isPrime(num):
	# THis is for if given number is 2
	if num == 2:
		print("Only even Prime number")
	# This is to elemenate all even numbers and numbers less than 2
	elif num < 2 or num % 2 == 0:
		print("Not a prime number")
	# Here Actual prime number logic goes
	else:
		# Difining a count variable initialized to zero
		count = 0
		# Iterate from 3 to num with step size 2(step size 2:eleminates even number)
		for i in range(3,num + 1,2):
			# If num evenly divisible by any value then increment count by 1
			if num % i == 0:
				count+=1
	
		# After all iteration if count = 1, itmeans num has only 1 and itself as its factors
		if count == 1:
			print("Prime number")
		else:
			print("Not a Prime Number.")
		
		
		
		
# Enter a Number
num = int(input("Enter a number: "))
# Passing arguments through function callable
isPrime(num)