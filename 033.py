# Unorthodox fraction canceling method
def prob33():
	g = set()
	for i in range(10, 100):
		for j in range(i+1, 100):
			num1 = i%10
			den1 = j%10
			num2 = i//10
			den2 = j//10
			if (num1 == den1 != 0 and den2!= 0 and i/j == num2/den2):
				g.add(lowest_term(num2, den2))
			elif (num1 == den2 != 0 and den1!= 0 and i/j == num2/den1):
				g.add(lowest_term(num2, den1))
			elif (num2 == den1 != 0 and den2!= 0 and i/j == num1/den2):
				g.add(lowest_term(num1, den2))
			elif (num2 == den2 != 0 and den1!= 0 and i/j == num2/den1):
				g.add(lowest_term(num2, den1))

	# find the numerator and denomitator of the products of those fraction
	num = den = 1
	for i in g:
		num *= i[0]
		den *= i[1]

	# return the denominator in the lowest common term
	return (den//gcd(num, den))

def lowest_term(i, j):
	g = gcd(i,j)
	return(i//g, j//g)

def gcd(i, j):
	if i == 0:
		return j
	return gcd(j%i, i)

import time
s = time.time()
print(prob33())
print(time.time()-s)