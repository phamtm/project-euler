def prob32():
	h = set()
	for i in range(2,100):
		start = 1234
		if i>9:
			start = 123
		for j in range(start,int(10000/i)+1):
			if is_pandigital(str(i)+str(j)+str(i*j)):
				h.add(i*j)
	return sum(h)

def is_pandigital(s):
	# the string must be 9 char-long and one character each from 1-9
	return len(s) == 9 and not "123456789".strip(s)

import time
s = time.time()
print(prob32())
print(time.time()-s)
