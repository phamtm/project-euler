def prob30(power):
	result = 0
	for n in range(10, (power+1)*10**power):
		sum_digits = 0
		k = n
		while k > 0:
			sum_digits += (k%10)**power
			k = k//10
		if (sum_digits == n):
			result += sum_digits
	return result

import time
s = time.time()
print(prob30(5))
print(time.time()-s)
