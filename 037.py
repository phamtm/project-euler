# find the sum of all (11) primes that are truncatable from left to right and
# right to left

from prime import prime_table

def prob37():
	sieve = prime_table(10**6)
	# the set of truncatable primes
	h = set()
	n = 11
	while len(h) < 11:
		truncatable = True
		l = str(n)
		for i in range (1, len(l) + 1):
			left_num = int(l[:i])
			right_num = int(l[len(l) - i:])
			left_index = (left_num - 1) // 2
			right_index = (right_num - 1) // 2
			# check for prime
			if not (left_num > 1 and right_num > 1 and sieve[left_index] and sieve[right_index]):
				truncatable = False
				break

		# if n is truncatable, add it to h
		if truncatable:
			h.add(n)

		# increase n by 2
		n += 2
		if (l[len(l) - 1] == 3):
			n += 2

	return (sum(i for i in h), h)

import time
s = time.time()
print(prob37())
print("Execution time:", time.time()-s)