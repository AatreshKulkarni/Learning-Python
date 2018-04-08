# List in Python

# 1. Creating a list

# Creating a list of integers and assigning it to my_list
my_list = [1,2,3]

# List can hold different data types
my_list = [1, 10.0, "hello", True]

# Length of list can be calculated using len() function
print(len(my_list)) 		# Prints 4


# 2. Indexing and slicing

mylist = ['one', 'two', 3, 4, 5]

# Prints element at index 1. (two)
print(mylist[1])

# Grab everything upto index 3(exclude 3rd index element)
print(mylist[:3])

# We can add new element to list as follows but this doesn't change original list
print(mylist + ['new_element'])

# Original list remains same as follows
print(my_list)

# To add element permanently we should reassign
my_list = my_list + ['add new item permanently']
print(my_list)

# We can double the list
print(my_list * 2)


# 3. Basic Methods in List

# Create a new list
list1 = [1,2,3]

# Printing it
print(list1)

# append() : It appends element at the end of the list
print(list1.append(4))

# pop() : By default pops last element from the list.
print(list1.pop())
print(list1.pop(0))		#In this case pops element at index 0

# New list
list2 = ['d', 'e', 'c', 'a', 'b']

# Print it
print(list2)

# reverse() : It reverse's the list elements in alphabetical order here
print(list2.reverse())

# sort() : It sort's the list in ascending order
print(list2.sort())


# 4. Nested Lists

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

print(matrix)

# Prints the first item in the matrix object
print(matrix[0])

# Prints the first item of the first item in the matrix object
print(matrix[0][0])

 
 