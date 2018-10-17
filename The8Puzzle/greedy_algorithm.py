"""
This approach alone is bad,
although it drives the search
in the right direction, it tends
to get stuck at a local optima
(We need something else to stop this)
"""

import manhattan_distance as md
from Puzzle8Node import Puzzle8Node

def greedy(start, goal):
	current_score = md.manhattan_distance(start.state, goal.state)
	done = False
	current = start
	print(current)
	while not done:
		if current.state == goal.state:
			done = True
		else:
			children = current.get_children()
			children_scores = []
			for child in children:
				score = md.manhattan_distance(child.state, goal.state)
				children_scores.append(score)

			best = min(children_scores)
			index = 0
			for score in children_scores:
				if score == best:
					break
				index +=1
			if best < current_score:
				current = children[index]
			else:
				done = True
		print(current)
	return current

def main():
	start = Puzzle8Node("2 1438675")
	goal = Puzzle8Node("2314 8675")

	print(greedy(start, goal))

if __name__ == "__main__":
	main()