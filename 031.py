def prob31(target):
	coins = [1,2,5,10,20,50,100,200]
	ways = [1]+[0]*target

	for coin in coins:
		for i in range(coin, target+1):
			ways[i] += ways[i-coin]

	return ways[target]

print(prob31(200))

