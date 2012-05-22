# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

def prob12():
	n = 2
	num = 1
	while True:
		num = n*(n+1)/2
		num_divs = count_num_of_divisors(num)
		if num_divs >= 500:
			break
	return num

# if a number can be factorized as A = p1^k1 * p2^k2 * p3^k3 ... where
# p1, p2, p3.. is prime then it has k1 + 1 + k2 + 1 + k3 + 1 + ... divisors
def count_num_of_divisors(num):


print(prob12())