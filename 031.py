def prob31(amount):
	coins = [1,2,5,10,20,50,100,200]
	num_coins = 200
	num_combinations = 0
	cache = {}
	return get_combinations(20, 200, coins, num_combinations, cache)

def get_combinations(amount, num_coins, coins, num_combinations, cache):
	if num_coins == 0:
		if amount != 0:
			return
		else:
