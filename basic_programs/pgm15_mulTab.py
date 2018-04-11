# Display the table of a given number

# Defining a function which prints the table of a given number
def mulTable(num):
	print(f"Multiplication Table of {num}:")
	for i in range(1,11):
		print(f"{num} * {i} = ",num * i)
		
# Taking input from user
num = int(input("Enter a number to display its table: "))
# Function call
mulTable(num)