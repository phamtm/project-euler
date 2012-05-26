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

import prime

def prob12():
	n = 3					# triangle number = n*(n+1)/2
	D[n] = 2				# number of divisors
	sieve = prime.prime_table(1000)	# the prime table
	MIN_DIVISORS = 500
	count = 0

	while count <= MIN_DIVISORS:
		n += 1
		n1 = n
		if (n1%2 ==0):
			n1 /= 2
		D[n1] = 1
		for i in range(0, len(sieve)):
			if sieve[i] == False:
				continue
			if i == 0:
				prime = 2
			else:
				prime = 2 * i + 1
			if (prime*prime) > n1:
				Dn1 *= 2
				break

			exponent = 1
			while n1 % (prime) == 0:
				n1 /= prime
				exponent += 1
			# if a number can be factorized as A = p1^k1 * p2^k2 * p3^k3 ... where
			# p1, p2, p3.. is prime then it has (k1 + 1)*(k2 + 1)*(k3 + 1) ... divisors
			if exponent > 1:
				Dn1 *= exponent
			if n1 == 1:
				break

			count = D[n]*D[n1]
			D[n] = D[n1]

	return int(n*(n-1)/2)

print(prob12())