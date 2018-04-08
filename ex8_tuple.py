# Tuple in Python

# 1. Constructing Tuple

# Create a tuple
t = (1,2,3)

# Prints tuple
print(t)

# length of the tuple using len()
print(len(t))

# Tuple Can also contain different data types
t = (1,'two',True,1)

# Indexing
print(t[0])

# Slicing 
print(t[1:])


# 2. Basic tuple methods

# index() : returns the index value of the element
print(t.index('two'))

# count() : returns the number of occurences of the element
print(t.count(1))


# 3. Immutability

# tuples can't grow in size and we can't change the values inside tuple.
# Hence following two will produce an error

# t[0] = 'change'		# TypeError

# t.append('nope')	# AttributeError