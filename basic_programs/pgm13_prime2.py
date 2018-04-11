# Print all prime numbers in an interval

# Defining a function printPrime
def printPrime(st_range,en_range):
	
	# Iterate throgh starting number to end number
	for num in range(st_range,en_range):
		if num > 1:
			# Iterate throgh 2 to num-1
			for i in range(2,num): 
				# Any number divides num then break this loop and take next number
				if num % i == 0:
					break
			else:
				print(num)
	
		
		
# Enter a Number
print("Enter range")
st_num,end_num = int(input("Enter starting number: ")),int(input("Enter end number: "))
# Passing arguments through function call
printPrime(st_num,end_num)