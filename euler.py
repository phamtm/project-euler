import math
import time

# 1. find the sum of numbers that are smaller than
# 1000 and divisible by 3 and 5
def sum_mod3_mod5(maximum):
	print(sum_divisible_by(3, maximum) + sum_divisible_by(5, maximum) - sum_divisible_by(15, maximum))

def sum_divisible_by(x, maximum):
	p = maximum/x
	return x*p*(p+1)/2

# 4. Find the largest palindrome number that is the
# product of two 3-digit numbers
def largest_palindrome():
	max_palindrome = 0
	i = 999
	while (i >= 100):
		j = 999
		while (j >= i):
			num = i*j
			if num > max_palindrome:
				if is_palindrome(str(num)):
					max_palindrome = num
			j -= 1
		i -= 1
	print(max_palindrome)

# check if a string is a palindrome
def is_palindrome(x):
	for i in range(0, (int)(len(x)/2)):
		if x[i] != x[len(x) - i - 1]:
			return False
	return True


# 6. Find the difference between square of sum and sum of
# squares of the first n numbers
def square_difference(n):
	sum_square = n*(n+1)*(2*n+1)/6
	square_sum = (n*(n+1)/2)**2
	return square_sum - sum_square

# 7. Find the 10001st prime
def find_prime(n):
	count = 1
	nth_prime = 2
	num = 3
	while count < n:
		if is_prime(num):
			count += 1
			nth_prime = num
		num += 2
	return nth_prime

# 9. Find the Pythagorean triplet that a+b+c = sum
def pythagore_triplet(sum):
	a = 1
	while a < sum - 2:
		b = a
		while b < sum - a - 1:
			c = 1000 - a - b
			if (a*a + b*b == c*c):
				print(a, b, c)
			b += 1
		a += 1
	return -1

# 10. Find the sum of all the primes below 2 million
def prime_sum(limit):
	# 1. initialize array of size limit
	crosslimit = (int)(math.sqrt(limit))
	sieve = [False for i in range(2,limit)]

	n = 4
	while (n <= limit):
		sieve[n] = True
		n += 2

	# 2. Mark composite numbers as True
	n = 3
	while (n <= crosslimit):
		if (sieve[n] == False):
			print(False)
			m = n*n
			while (m <= limit):
				sieve[m] = True
				m += 2*n
		n += 2

	# 3. Calculate sum by adding all unmarked index
	a_sum = 0
	for i in range(2,limit):
		if (sieve[i] == False):
			a_sum += i
	print(sum)

#
# MAIN FUNCTION CALL
#
s = time.time()
print(int(largest_prime_factor(123)))
print(time.time() - s)
