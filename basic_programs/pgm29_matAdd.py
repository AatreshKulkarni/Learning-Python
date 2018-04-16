# Addition of 2 matrices

# Defining a function that adds two matrix
def matAdd(matrix1,matrix2):

	# Initializing result matrix
	res_list = [0] * row_size
	

	for i in range(len(res_list)):
		res_list[i] = [0] * col_size
	
	# Iteration through rows
	for i in range(0,len(matrix1)):
		# Itaration through column
		for j in range(0,len(matrix1[0])):
			# Adding Matrices
			res_list[i][j] = matrix1[i][j] + matrix2[i][j]

	# Printing Sum of 2 matrices		
	print("Addition result of 2 matrices:")		
	print(res_list)
	
	

# Input size of the matrices
row_size = int(input("Enter row size of the matrix:"))
col_size = int(input("Enter col size of the matrix:"))

# Initializing rows
matrix1 = [0] * row_size
matrix2 = [0] * row_size

# Initializing columns
for i in range(0,row_size):
	matrix1[i] = [0] * col_size

for i in range(0,row_size):
	matrix2[i] = [0] * col_size

# Input numbers of the matrix1
print("Enter numbers of matrix1:")
for i in range(row_size):
	for j in range(col_size):
		matrix1[i][j] = int(input())
print(matrix1)

# Input numbers of matrix2
print("Enter numbers of matrix2:")
for i in range(row_size):
	for j in range(col_size):
		matrix2[i][j] = int(input())
print(matrix2)

# Function call
matAdd(matrix1,matrix2)