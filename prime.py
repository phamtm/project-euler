import math

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