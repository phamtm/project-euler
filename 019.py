def prob19():
	normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
	leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]

	index = 0
	total = 0

	for year in range(1901, 2001):
		days = []
		if (year%4 == 0 and year%25!= 0) or (year%400 == 0):
			days = leap_year
		else:
			days = normal_year
		for month in range(0, 12):
			index += days[month]
			# Jan 1st 1901 is a Wednesday, therefor Jan 5th 1901 is
			# a Sunday. It follows that every Sundays must be 5 after modulo 7
			if (index%7 == 5):
				total += 1
	return total

import time
s = time.time()
print(prob19())
print(time.time()-s)

