# How many routes are there through a 20x20 grid from top-left to bottom-right corner
# use BFS
def prob15(size):
	# store the visited nodes
	visited = [None for i in range(0, size + 2)]

	while(visited[size + 1, size + 1] != 1)

		# reset the visited array
		visited = [None for i in range(0, size + 2)]

# return a list of adjacent unvisited nodes
def get_adjacent_nodes(x, y, visited):
	possible_adjacent_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
	adj_list = []
	for i in range(0, 4):
		if possible_adjacent_list[i][0] >= 0 and possible_adjacent_list[i][1] >= 0:
			adj_list.append(possible_adjacent_list[i])
	return adj_list

print(prob15(20))