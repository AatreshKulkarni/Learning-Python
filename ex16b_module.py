# Importing a user defined module ex16a_module. Here .py extension not required 
# We can also import like: "from ex16a_module import isEven()"
import ex16a_module

# Now importing predefined module(inbuilt module) random: Used to get random integer
import random

# Printing the containts of user defined imported package
ex16a_module.isEven(10)

# Printing a random number in range 1 to 100 using randrange() in random module
print("Random number is: ",random.randrange(1,100))		#On each run it will print different number
