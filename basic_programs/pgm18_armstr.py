# Find Armstrong number in an interval


def armstrInt(min_num,max_num):
	
	print(f"Armstrong numbers in range {min_num} , {max_num} are:")
	# Checking each number one at time whether it is armstrong are not
	count = 0
	for num in list(range(min_num,max_num+1)):
		# For each number initializing sum to 0
		sum = 0
		# For every iteration assigning num to temp_num 
		temp_num = num
		
		#Find sum of the cube of the each digit
		while temp_num > 0:
			dig = temp_num % 10
			sum = sum + dig ** 3
			temp_num = int(temp_num / 10)
		
		# Here we are checking number is armstrong are not
		if sum == num:
			print(num)
			count += 1
	# If no armstrong numbers present then execute this print
	if count == 0:	
		print("No armstrong numbers present in this range")

# Input range
print("Enter range")
num1,num2 = int(input("Enter min_number: ")),int(input("Enter max_number: "))			
# Function call
armstrInt(num1,num2)