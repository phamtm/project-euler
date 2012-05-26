# Using 022.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each
# name, multiply this value by its alphabetical position in the
# list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?

def prob22():
	f = open("022.txt", "r")
	names = f.read().replace('"', '').split(',')
	f.close()
	names.sort()
	total_score = 0
	for i in range(0, len(names)):
		score = 0
		for j in names[i]:
			score += ord(j) - 64
		score *= i + 1
		total_score += score
	return total_score

import time
s = time.time()
print(prob22())
print(time.time()-s)


