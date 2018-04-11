# To check leap year

#  Define a method which checks whether given year is leap year or not
def checkLeap(year):
	# Year evenly divisible by 400 is a leap year
	if year % 400 == 0:
		print("Leap year")
	# Year evenly divisible by 100 other than multiples of 400 are not leap years
	elif year % 100 == 0:
		print("Not a leap year")
	# Year evenly divisible by 4 except centuries are divisible by 4
	elif year % 4 == 0:
		print("Leap Year")
	# Print not a lea year	
	else:
		print("Not a Leap year")
		
		
		
# Input a year
year = int(input("Enter a year: "))
# Function call
checkLeap(year)