# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def prob13():
	sum_str = ""
	array = []
	f = open("013.txt", "r")
	for line in f:
		array.append(line.strip())
	f.close()

	carry = 0
	for i in range(11, -1, -1):
		temp_sum = carry

		for string in array:
			temp_sum += int(string[i])

		# save for next calculation
		carry = int((temp_sum - temp_sum %10) / 10)
		temp_sum = temp_sum%10
		sum_str = str(temp_sum) + sum_str

	if carry != 0:
		sum_str = str(carry) + sum_str
	return sum_str[0:10]

print(prob13())
