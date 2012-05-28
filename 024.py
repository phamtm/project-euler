# Find the 1-millionth lexicographic permutation of the digits 0-9

# return the nth lexicographic permutation
from math import factorial, ceil

def prob24(n):
	digits = [0,1,2,3,4,5,6,7,8,9]
	result = []

	for i in range(10):
		max_perm = factorial(len(digits)-1)
		if n < max_perm:
			index = 0
		else:
			index = ceil(n/max_perm) - 1
		result.append(digits[index])
		digits.pop(index)
		if (n%max_perm == 0):
			n = max_perm
		else:
			n %= factorial(len(digits))


	s = ""
	for char in result:
		s += str(char)
	return s

import time
s = time.time()
print(prob24(10**6))
print(time.time()-s)

# from itertools import islice, permutations
# print(''.join(next(islice(permutations(map(str, range(10))), 999999, None))))

