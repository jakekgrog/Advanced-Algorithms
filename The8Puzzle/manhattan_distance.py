"""
/* This greedy algorithm uses the manhattan
/* distance as the heuristic
/* to help solve the 8 puzzle
"""

from Puzzle8Node import Puzzle8Node

def getXY(index):
	index = int(index)
	x = index % 3
	y = index // 3
	return x, y

def get_singular_md(start_index, goal_index):
	start_x, start_y = getXY(start_index)
	goal_x, goal_y = getXY(goal_index)
	return abs(start_x-goal_x) + abs(start_y - goal_y)

def manhattan_distance(start, goal):
	distance = 0
	for i in range(0, len(start)):
		index = goal.index(start[i])
		if start[i] != " ":
			singular_distance = get_singular_md(i, index)
			distance += singular_distance
	return distance


def main():
	print(manhattan_distance("1234567 8", "23145678 "))

if __name__=="__main__":
	main()
