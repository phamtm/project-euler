import time
s = time.time()
p = 0
for n in range(0, 10**6):
	l = str(n)
	if (l == l[::-1]):
		binary = bin(n)[2:]
		if (binary == binary[::-1]):
			p += n
print(p)
print(time.time()-s)