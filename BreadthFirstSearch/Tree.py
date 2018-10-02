from Node import Node as Node

class CustomTree:
	"""
	A custom tree class that uses a dictionary to build a tree
	@root_name: Name of root node
	@t_dict: Dictionary from which tree will be built 
	"""
	
	def __init__(self, root_name, t_dict):
		self.root = Node(root_name, [])
		self.add(self.root, t_dict) # This will build the entire tree


	def add(self, node, t_dict):
		# Recursively build the tree from the given dictionary
		if node.name in t_dict.keys():
			children_names = t_dict[node.name]

			children = []

			for index, name in enumerate(children_names):
				node_in_tree = self.find(name)
				children.append(node_in_tree if node_in_tree != None else Node(name, []))

			node.children = children

			for child in node.children:
				self.add(child, t_dict)


	def r_find(self, node, search_name):
		# Recursively search the tree for a given node name (search_name)
		if node.name == search_name:
			return node
		else:
			for next_node in node.children:
				ret = self.r_find(next_node, search_name)
				if ret != None:
					return ret
			return None

	def find(self, search_name):
		#call recursive find
		return self.r_find(self.root, search_name)


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

if __name__=="__main__":
	main()