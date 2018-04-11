# Check Largest of 3 number

# Definimg a function to check largest of 3 number
def largestOf3(num1,num2,num3):
	if num1 >= num2 and num1 >= num3:
		print("num1 is the largest of 3")
		
	elif num2 >= num3:
		print("num2 is the largest of 3")
		
	else:
		print("num3 is the largest of 3")
		
		
# Input 3 numbers
num1,num2,num3 = int(input("Input num1: ")),int(input("Input num2: ")),int(input("Input num3: "))
# Function call
largestOf3(num1,num2,num3)
		
		
	
	