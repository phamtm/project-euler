# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
# Lesson: type casting is VERY COSTLY

def prob16(base, exponent):
	return sum(int(digit) for digit in str(base**exponent))


	# product = "1"
	# for i in range(0, exponent):
	# 	carry = 0
	# 	temp = ""
	# 	for i in range(len(product)-1, -1, -1):
	# 		a_sum = base * int(product[i]) + carry
	# 		digit = a_sum % 10
	# 		carry = int((a_sum - digit) / 10)
	# 		temp = str(digit) + temp
	# 	if carry != 0:
	# 		temp = str(carry) + temp
	# 	product = temp

	# sum_digits = 0
	# for i in range(0, len(product)):
	# 	sum_digits += int(product[i])
	# return sum_digits

# print(prob16(2, 1000))
import math
print(math.factorial(100))