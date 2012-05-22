# 3. Find the largest prime factor
def largest_prime_factor(x):
	# Special case: x = 1
	if is_prime(x) or x == 1:
		return x
	factor = -1
	temp = 2
	# Factor x once
	while (temp < x):
		if (x%temp == 0):
			factor = temp
			break
		temp += 1

	return max(largest_prime_factor(x/factor), largest_prime_factor(factor))

def is_prime(x):
	if (x == 2) or (x == 3):
		return True
	elif (x%2 == 0) or (x > 3 and x%3 == 0):
		return False
	else:
		i = 3
		while (i*i <= x): #O(sqrt(n))
			if (x%i == 0):
				return False
			i += 2
		return True

print(int(largest_prime_factor(1355224)))