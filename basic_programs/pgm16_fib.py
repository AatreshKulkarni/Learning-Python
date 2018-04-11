# Print sequeance of fibonacci number upto given range

# Defining a function to generate fibonacci sequence
def fib(num):
	fib1 = 0
	fib2 = 1
	
	print(f"Fibonacci sequeance of {num} numbers:")
	if num == 1:
		print(fib1)
	elif num == 2:
		print(fib1,fib2)
	else:
		print(fib1)
		print(fib2)
		for i in range(3,num+1):
			fib3 = fib1 + fib2
			print(fib3)
			fib1,fib2 = fib2,fib3
		

num = int(input("Enter a number to generate fibonacci: "))		
fib(num)		