# euclid's algorithm for finding greatest common divisor
def gcd(a, b):
	if (b == 0):
		return a
	return gcd(b, a%b)

# find the smallest common divisor of 1, 2,.., 20
def scd(lb, ub):
	result = 1;
	for i in range(lb, ub):
		result *= i / gcd(result, i)

	return result

print(int(scd(1, 21)))