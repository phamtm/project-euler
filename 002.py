# 2. Find the sum of even fibonacci number not greater than x
def sum_even_fib(x):
	prev = 0
	cur = 1
	a_sum = 0
	while (cur <= x):
		if (cur%2 == 0):
			a_sum += cur
		temp = cur
		cur += prev
		prev = temp
	return a_sum

def sum_even_fib_2(x):
	prev = 1
	cur = 1
	next = prev + cur
	a_sum = 0
	while (cur <= x):
		# the third number in the sequence is always an even number
		a_sum += next
		prev = cur + next
		cur = prev + next
		next = prev + cur
	return a_sum

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
	return a_sum

print(sum_even_fib_3(1000))