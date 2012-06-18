from prime import prime_table

def prob35(limit):
	# there are 13 circular primes below 1,000,000
	num_cprimes = 13
	sieve = prime_table(limit)

	for n in range(111, limit - 1, 2):
		l = str(n)
		if not any(d in ("0","2","4","5","6","8") for d in l):
			num_digits = len(l)
			is_cprime = True
			for i in range(0, num_digits):
				# shift the string 1 digit to the left
				l = l[1:] + l[:1]
				# index in the prime table
				index = (int(l) - 1) // 2
				if (sieve[index] == False):
					is_cprime = False
					break;
			if is_cprime:
				# h.add(n)
				num_cprimes += 1

	return num_cprimes

import time
s = time.time()
print(prob35(10**6))
print(time.time() - s)