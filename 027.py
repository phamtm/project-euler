import prime

def prob27():
	sieve = prime.prime_table(10**4)
	D = {}
	for a in range(-999, 999, 2):
		for b in range(a + 2, 1000):
			if  (a*a - 4*b >= 0):
				continue
			num_primes = 0
			for n in range(0, b):
				temp = n*n + a*n + b
				if (temp < 2):
					break
				elif (temp == 2):
					num_primes += 1
				else:
					if (temp%2 == 1 and sieve[int((temp-1)/2)]):
						num_primes += 1
					else:
						D[(a,b)] = num_primes
						break
	max_primes = 0
	max_term = (0, 0)
	for i,j in D:
		if (D[(i,j)] > max_primes):
			max_primes = D[(i, j)]
			max_term = (i, j)

	return [max_term]

import time
s = time.time()
print(prob27())
print(time.time()-s)