from Tree import CustomTree

def breadth_first_search(tree, start, goal):
	"""
	Carries out breadth first search on the tree that is build from the graph
	@tree: The custom tree
	@start: The label of node you start searching from (Initial State)
	@goal: The label of the node you are searching for (Goal State)
	"""

	goal = tree.find(goal)
	todo = [tree.find(start)]
	visited = []

	while len(todo) > 0:
		next = todo.pop(0)
		if next == goal:
			return goal
		else:
			visited.append(next)
			children = [child for child in next.get_children() if child not in visited and child not in todo]
			print(next, children)
			todo += children
		print("\t", todo, visited)
	
	return None


def main():
	t_dict = {
		'A': [c for c in 'BCD'],
		'B': [c for c in 'EF'],
		'C': [c for c in 'GH'],
		'D': [c for c in 'IJ'],
		'E': [c for c in 'KL'],
		'F': [c for c in 'LM'],
		'G': [c for c in 'N'],
		'H': [c for c in 'OP'],
		'I': [c for c in 'PQ'],
		'J': [c for c in 'R'],
		'K': [c for c in 'S'],
		'L': [c for c in 'T'],
		'P': [c for c in 'U'],
	}

	tree = CustomTree('A', t_dict)

	breadth_first_search(tree, "A", "H")

if __name__=="__main__":
	main()


