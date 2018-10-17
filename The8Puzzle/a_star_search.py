import manhattan_distance as md
from Puzzle8Node import Puzzle8Node

def a_star_search(start, goal):
	start.score = md.manhattan_distance(start.state, goal.state)
	openlist = [start]
	visited = set()
	num_searches = 0
	while len(openlist) > 0:
		next = openlist.pop(0)
		num_searches += 1
		if next.state == goal.state:
			return next, num_searches
		else:
			visited.add(next)
			children = next.get_children()
			children_scores = []
			for child in children:
				if child not in visited and child not in openlist:
					child.score = md.manhattan_distance(child.state, goal.state) + child.depth
					openlist.append(child)
			openlist.sort(key=lambda x : x.score)
	return num_searches, None

def main():
	start = Puzzle8Node("12345678 ")
	goal = Puzzle8Node("2314567 8")

	print(a_star_search(start, goal))

if __name__ == "__main__":
	main()