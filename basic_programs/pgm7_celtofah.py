# Convert Celsius to Fahrenheit : f = c * 9/5 + 32

def celtofah(temp_in_cel):
	# Formula to convert celsius to fahrenheit
	temp_in_fah = temp_in_cel * (9/5) + 32
	print(f"{temp_in_cel}celsius in fahrenheit = {temp_in_fah}")
	

# Taking input from user
temp_in_celsius = int(input("Enter temp in celsius: "))	
# Function call
celtofah(temp_in_celsius)
