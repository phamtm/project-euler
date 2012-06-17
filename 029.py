def prob29():
	h=set()
	for a in range(2,101):
		for b in range(2,101):
			h.add(a**b)
	return len(h)

import time
s = time.time()
print(prob29())
print(time.time()-s)
