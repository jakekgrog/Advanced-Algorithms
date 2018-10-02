

class Node:
	def __init__(self, name, children):
		self.name = name
		self.children = children

	def get_children(self):
		return self.children

	def __str__(self):
		return self.name

	def __repr__(self):
		return str(self)

