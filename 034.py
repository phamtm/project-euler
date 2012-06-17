def prob34():
	facts = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
	# s - sum of all numbers that satisfy the condition
	s = 0
	for n in range(10, 50000):
		factorial_sum = sum(facts[int(d)] for d in str(n))
		if factorial_sum == n:
			s += n
	return s

import time
s = time.time()
print(prob34())
print(time.time()-s)