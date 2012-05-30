# Find the fibonacci term that has at least d-digits:

from math import ceil, log10, sqrt
def prob25(d):
	'''
	F(n) is the integer closest to Phi**n/sqrt(5)
	To calculate the number of digits: d = floor(log(x)) + 1
	Substitute x with Fn, and Fn with Phi**n/sqrt(5) we have
	d - 1 = log(Phi**n/sqrt5)
	d - 1 = nlog(Phi) - log(5)/2
	n = ceil((d-1+log(5)/2)/log(Phi)) since n is an integer
	'''

	phi = (sqrt(5)+1)/2
	return ceil((d - 1 + log10(5)/2) / log10(phi))

print(prob25(1000))
print(1/11)
