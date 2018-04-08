# Strings in Python

# 1.Creating string and Printing Strings

print('Hello World')	# using single quotes

print("Hello World")	# using double quotes


# We have to use double quotes and single correctly to avoid error

print("Hi I'm Aatresh") 

print('My favourite sport is "Cricket"')

# To find the length of the string: 'len()' method
print(len('Hello'))			# prints length of 'hello': 5


# 2. String Indexing
# We use [] after object in python to call its index
# Assign as 's' as a string 

s = 'Hello World'

# Checking
s

# Printing s object
print(s)

print(s[0]) 			# Shows the first letter  

print(s[-1]) 			# Shows the last letter

print(s[1:])			# Grabing everything from index 1 to end

print(s[::2])			# Grab evrything from index 0 to end in step size 2


# 3. String Properties

# We can't change the element of the string
# s[0] = 'x'	#This will give an error

# But we can concatenate 2 strings
print(s + " What's up?")	# But this will not change the actually string single

s = s + " What's Up?"   # But this will change the actual string 's'

print(s)			#Prints Hello World What's up?

# We can use the multiplication symbol to create repetition!
letter = 'z'

print(letter * 10)

# 3.Basic built in String methods 

s = 'Hello World'

# Upper case a string
print(s.upper())

# Lower case
print(s.lower())

# Splits the string at blank space(This is the default)  
print(s.split())

# Splits by a specific element(doesn't include the element that was split on)
print(s.split('W'))

# 4. Print Formatting
print('E Sala Cup Namde: {}'.format('This is the RCB fans slogan today'))