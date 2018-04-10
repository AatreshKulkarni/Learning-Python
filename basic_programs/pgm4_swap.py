# Swapping the containts of 2 variables

# Defining a swap function which swaps the variable( Using temp variable)
def swap(num1,num2):
	temp = num1
	num1 = num2
	num2 = temp
	return num1,num2
	
	
# Input 2 numbers
num1,num2 = int(input("Enter num1:")),int(input("Enter num2:"))
print(f"Before swapping:\n num1={num1}\n num2={num2}")
# Fuction call and returning values
swapped_num1,swapped_num2 = swap(num1,num2)
print(f"After Swapping:\n num1={swapped_num1}\n num2={swapped_num2}")