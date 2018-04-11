# Convert kilometer to mile. 1mi = 1.6km 

# Defining a function to convert mile to km
def kiloToMile(kilo):
	mile = kilo / 1.6
	print(f"{kilo}km in mile = {mile}mi")
	
# Input value in km
kilo = int(input("Input value in km: " ))
# Function call 
kiloToMile(kilo)