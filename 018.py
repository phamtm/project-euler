# Find the maximum total from top to bottom of the triangle below:

def prob18_67():
	'''
	Use dynamic programming to solve this problem
	'''
	f = open("067.txt", "r")
	line = f.readline()
	triangle = []
	while(line):
		line_ar = line.split()
		triangle.append(line_ar)
		line = f.readline()
	f.close()

	# dictionary to store previous value
	D = {}
	return max_sum_triangle(0, 0, D, triangle)

def max_sum_triangle(i, j, D, triangle):
	if ((i, j) in D):
		return D[(i, j)]
	if (i == len(triangle) - 1):
		D[(i, j)] = int(triangle[i][j])
		return D[(i, j)]
	D[i, j] = int(triangle[i][j]) + max(max_sum_triangle(i+1, j, D, triangle), max_sum_triangle(i+1, j+1, D, triangle))
	return D[i, j]

import time
s = time.time()
print(prob18_67())
print(time.time()-s)
