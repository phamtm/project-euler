import time

def collatz(n, res):
	while True:
	    if n not in cache:
		    if n % 2 == 0:
		        cache[n] = 1 + collatz(n/2, cache)
		    else:
		        cache[n] = 1 + collatz(3*n + 1, cache)
	    return cache[n]

s = time.time()
cache = {1: 1}
for i in range(1, 10**6 + 1):
	collatz(i, cache)
max_path = 1
max_num = 1
for i in range(1,10**6):
	max_path = max(cache[i], max_path)
print("Max path is: " + str(max_path))
print(time.time()-s)
