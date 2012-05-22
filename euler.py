import math
import time

# 1. find the sum of numbers that are smaller than
# 1000 and divisible by 3 and 5
def sum_mod3_mod5(maximum):
	print(sum_divisible_by(3, maximum) + sum_divisible_by(5, maximum) - sum_divisible_by(15, maximum))

def sum_divisible_by(x, maximum):
	p = maximum/x
	return x*p*(p+1)/2

# 2. Find the sum of even fibonacci number not greater than x
def sum_even_fib(x):
	prev  = 0
	cur   = 1
	a_sum = 0
	while (cur <= x):
		if (cur%2 == 0):
			a_sum += cur
		temp = cur
		cur += prev
		prev = temp
	print(a_sum)

def sum_even_fib_2(x):
	prev  = 1
	cur   = 1
	next  = prev + cur
	a_sum = 0
	while (cur <= x):
		# the third number in the sequence is always an even number
		a_sum += next
		prev  = cur + next
		cur   = prev + next
		next  = prev + cur
	print(a_sum)

def sum_even_fib_3(x):
	prev  = 2
	cur   = 8
	a_sum = prev
	while (cur <= x):
		a_sum += cur
		# For the sequence 2,8,34,144, E(n) = 4*E(n-1) + E(n-2)
		temp  = cur
		cur   = 4*cur + prev
		prev  = temp
		print(cur, temp)
	print(a_sum)

# 3. Find the largest prime factor
def largest_prime_factor(x):
	# Special case: x = 1
	if is_prime(x) or x == 1:
		return x
	factor = -1
	temp = 2
	# Factor x once
	while (temp < x):
		if (x%temp == 0):
			factor = temp
			break
		temp += 1

	return max(largest_prime_factor(x/factor), largest_prime_factor(factor))

def is_prime(x):
	if (x == 2) or (x == 3):
		return True
	elif (x%2 == 0) or (x > 3 and x%3 == 0):
		return False
	else:
		i = 3
		while (i*i <= x): #O(sqrt(n))
			if (x%i == 0):
				return False
			i += 2
		return True

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
prime_sum(2*10**6)
print(time.time() - s)
# main function call
# num_runs = 0
# total_time = 0
# for x in range(1,10):
# 	s = time.time()
# 	pythagore_triplet(1000)
# 	total_time += time.time() - s
# 	num_runs += 1
# print (total_time/num_runs)