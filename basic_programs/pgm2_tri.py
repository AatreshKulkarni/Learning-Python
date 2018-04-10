# To find Area of triangle

# Defining a function which calculates area of triangle
def areaOfTri(base,height):
	# Calculating area
	area = 1/2 * base * height
	print("Area of triangle is : ",area)
	
	
# Input height and base of the triangle
base = int(input("Enter the value of base: "))
height = int(input("Enter the value of height: "))

# Function call
areaOfTri(base,height)