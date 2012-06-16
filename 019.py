def prob19():
	n_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
	l_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]

	index = 0
	total = 0
	for year in range(1901, 2001):
		days = []
		if (year%4 == 0 and year%25!= 0) or (year%400 == 0):
			days = l_year
		else:
			days = n_year
		for month in range(0, 12):
			index += days[month]
			if (index%7 == 0):
				total += 1
	return total

print(prob19())
