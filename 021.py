# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

import math
import time

def prob21(limit):
	cache = []
	miss = [0, 1, 2]
	sieve = prime_table(limit+1)

	# 1. Prime numbers are not amicable numbers
	for i in range(1, len(sieve)):
		if (sieve[i] == True):
			miss.append(2*i+1)

	for i in range(3, limit+1):
		# 2. Find i in cache and miss
		if not (i in cache or i in miss):
			# 3. Compute sum of divisors for i
			p = sum_of_divisors(i)

			if (i != p and i == sum_of_divisors(p)):
				cache.append(i)
				if (p not in cache):
					cache.append(p)
				print("result: ", i, p)
			else:
				if (p != i):
					miss.append(i)
					miss.append(p)
				else:
					miss.append(i)

	return sum(i for i in cache)

# Find the sum of proper divisors of a positive integer
def sum_of_divisors(n):
	sum_divisors = 1
	i = 2
	while (i*i <= n):
		if (n % i == 0):
			sum_divisors += i
			if (i*i != n):
				sum_divisors += int(n/i)
		i += 1
	return sum_divisors

def sum_of_divisors_2(n, sieve):
	sum_divisors = 1
	k = n
	for i in range(0, len(sieve)):
		if (i == 0):
			prime = 2
		else:
			prime = 2*i+1
		exponent = 0
		while (k % prime == 0):
			k /= prime
			exponent += 1
		if (exponent > 0):
			sum_divisors *= int((prime**(exponent+1) - 1)/(prime-1))
		if (k == 1):
			break

	return sum_divisors - n

# using the sieve of eratothenes
def prime_table(limit):
	sievebound = math.floor((limit-1)/2) # last index of sieve
	crosslimit = int(math.floor(math.sqrt(limit)-1)/2)
	sieve = [True for i in range(0, sievebound)]
	for i in range(1, crosslimit):
		# i is not marked, hence prime
		if sieve[i]:
			for m in range(2*i*(i+1), sievebound, 2*i+1):
				sieve[m] = False

	return sieve

s = time.time()
print(prob21(10**4))
exec_time = time.time() - s
print("Exec time: %.3fs" % exec_time)