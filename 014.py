import time

# def prob14():
# 	max_length = 0
# 	max_num = 0
# 	n = 1
# 	cur_length = 1
# 	d = {1:1}	# store previous results

# 	while n <= 10**6:
# 		k = n
# 		# if sequence of k is recorded in array return
# 		if k in d:
# 			cur_length += d[k]
# 			break
# 		# if k is not recorded, use the Collatz function
# 		else:
# 			if k%2 == 0:
# 				k /= 2
# 			else:
# 				k = 3*k + 1
# 		cur_length += 1

# 		# record the current sequence's length
# 		d[k] = cur_length

# 		if cur_length > max_length:
# 			max_num = n
# 			max_length = cur_length

# 		n += 1
# 	return [max_length, max_num]

def collatz(n, res):
	nn = n

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
print(time.time()-s)
