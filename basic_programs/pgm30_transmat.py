# Transposing a given matrix

# Defining a function that calculates the transpose of a matrix
def transMatrix(matrix):

	# Initializing result matrix
	res_list = [0] * col_size
	

	for i in range(len(res_list)):
		res_list[i] = [0] * row_size

	# Transpose logic
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			res_list[j][i] = matrix[i][j]

	# Printing transpose of a matrix		
	print("Transpose of a matrix:")
	for i in res_list:
		print(i)

## Input size of the matrices
row_size = int(input("Enter row size of the matrix:"))
col_size = int(input("Enter col size of the matrix:"))

# Initializing rows
matrix1 = [0] * row_size
#matrix2 = [0] * row_size

# Initializing columns
for i in range(0,row_size):
	matrix1[i] = [0] * col_size

#for i in range(0,row_size):
#	matrix2[i] = [0] * col_size

# Input numbers of the matrix1
print("Enter numbers of matrix1:")
for i in range(row_size):
	for j in range(col_size):
		matrix1[i][j] = int(input())

print("Given Matrix:")
for i in matrix1:
	print(i)


transMatrix(matrix1)