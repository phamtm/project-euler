# find the greatest product on a straight line
def prob11():
	offset = 4
	my_max = 0
	size = count_lines()
	matrix = [[None for col in range(size[1])] for row in range(size[0])]
	row = 0
	index1 = index2 = 0

	# read in the matrix
	f = open("011.txt", "r")
	line = f.readline()
	while (row < size[0]):
		split_ar = line.rsplit()
		for i in range (0, size[1]):
			matrix[row][i] = int(split_ar[i])
		row += 1
		line = f.readline()
	f.close()

	# find max
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			row_prod = col_prod = lrd_prod = rld_prod = 0
			if (i <= size[0] - offset):
				col_prod = matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j]
				if (j <= size[1] - offset):
					lrd_prod = matrix[i][j] * matrix[i + 1][j + 1] * matrix[i + 2][j + 2] * matrix[i + 3][j + 3]
			if (j <= size[1] - offset):
				row_prod = matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3]
			if (i >= offset - 1 and j <= size[1] - offset):
				rld_prod = matrix[i][j] * matrix[i - 1][j + 1] * matrix[i - 2][j + 2] * matrix[i - 3][j + 3]
			if my_max < max(row_prod, col_prod, lrd_prod, rld_prod):
				index1 = i
				index2 = j
			my_max = max(row_prod, col_prod, lrd_prod, rld_prod, my_max)
	return [my_max, index1, index2]

# return the dimension of the array
def count_lines():
	f = open("011.txt", "r")
	num_rows = 0
	num_cols = -1
	line = f.readline()
	while (line):
		if (num_cols == -1):
			num_cols = len(line.rsplit())
		num_rows += 1
		line = f.readline()
	f.close()
	result = [num_rows, num_cols]
	return result

print(prob11())
