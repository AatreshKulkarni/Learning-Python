# Generating a random number within given range

# Defining a function which generates a random number using "random" mudule
import random
def randNumGen(min_num,max_num):
	return random.randrange(1,100)
	
	
# Input min and max range
min_num,max_num = int(input("Enter min:")),int(input("Enter max:"))
# Function call
rand_num = randNumGen(min_num,max_num)
print("Random number within range 1 to 100 is: ",rand_num)