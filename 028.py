from math import ceil
def prob28(r):
	diag_sum = 1
	start = 1
	for r in range(1, ceil((r+1)/2)):
		diag_sum += 4*start+20*r
		start += 8*r
	return diag_sum

import time
s = time.time()
print(prob28(1001))
print(time.time()-s)