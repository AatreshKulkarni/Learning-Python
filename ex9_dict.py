# Dictionaries in Python
# Dictionary contains 'key' and 'value' pair


# 1. Constructing a Dictionary

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

print(my_dict)		# Prints dictionary my_dict

# Call values by their key
print(my_dict['key2'])

# Dictionaries are flexible to hold any datatypes

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Let's print items from the dictionary
print(my_dict['key3'])

# We Can call an index on that value
print(my_dict['key3'][0])

# We Can then even call methods on that value
print(my_dict['key3'][0].upper())


# We can create dictionary through assignment
# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

# Print dictionary d
print(d)


# 2. Nesting with dictionary

# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# We can Keep calling the keys
print(d['key1']['nestkey']['subnestkey'])


# 3. Few dictionary methods

# Create a simple dictionary
d = {'key1':1,'key2':2,'key3':3}

# keys() : Method to return a list of all keys 
print(d.keys())

# values() : Method to grab all values
print(d.values())

# Method to return tuples of all items  
print(d.items())