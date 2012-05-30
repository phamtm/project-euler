# Find the value of d  1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.
def prob26():
	'''
	http://mathworld.wolfram.com/DecimalExpansion.html
	'''
	max_cycle = 0
	max_term = 1

	for n in range(1, 1000):
		cache = {}
		i = 0
		while True:
			mod = (10**i) % n
			if (mod in cache):
				s = cache[mod]
				t = i - s
				if (t > max_cycle):
					max_cycle = t
					max_term = n
				break
			else:
				cache[mod] = i
			i += 1

	return max_term

import time
s = time.time()
print(prob26())
print(time.time()-s)

