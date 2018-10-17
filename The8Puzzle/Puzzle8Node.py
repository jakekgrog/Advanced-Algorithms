class Move:
	def __init__(self, row, col):
		self.row = row
		self.col = col
	def __str__(self):
		return "({0}, {1})".format(self.row, self.col)

class Node:
	def __init__(self, state, children):
		self.state = state
		self.children = children

	def __str__(self):
		return self.state
      
	def __repr__(self):
		return str(self)

	def get_children(self):
		return self.children

	def __eq__(self, other):
		"""Override the default Equals behavior"""
		if isinstance(other, self.__class__):
			return self.state == other.state
		return NotImplemented

	def __ne__(self, other):
		"""Define a non-equality test"""
		if isinstance(other, self.__class__):
			return not self.__eq__(other)
		return NotImplemented

	def __hash__(self):
		"""Override the default hash behavior (that returns the id or the object)"""
		return hash(tuple(sorted(self.__dict__.items())))


class Puzzle8Node(Node):
	def __init__(self, start_state, depth=0):
		# Board consists of 8 numbers and a blank space
		assert "".join(sorted(start_state)) == " 12345678"
		self.state = start_state
		self.depth = depth
		self.score = 0

	def make_board(self, name):
		board = [["_" for col in range(3)] for row in range(3)]
		index = 0
		for row in range(3):
			for col in range(3):
				board[row][col] = self.state[index]
				index += 1
		return board

	def __str__(self):
		s = ""
		board = self.make_board(self.state)
		for row in range(3):
			for col in range(3):
				if col == 0:
					s += '\t'
				s += board[row][col]
			s += "\n"
		return s

	def get_state(self, board):
		state = ""
		for row in range(3):
			for col in range(3):
				state += board[row][col]
		return state

	def get_blank(self, board):
		for row in range(3):
			for col in range(3):
				if board[row][col] == " ":
					return Move(row, col)

	def get_children(self):
		return self.get_moves()

	def get_moves(self):
		board = self.make_board(self.state)
		blank = self.get_blank(board)

		moves = []
		if blank.row != 0:
			# Can move up
			board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
			moves.append(self.get_state(board))
			# Undo what we just did
			board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
		if blank.row != 2:
			#Can move down
			board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]
			moves.append(self.get_state(board))
			board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]
		if blank.col != 2:
			# Can move right
			board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
			moves.append(self.get_state(board))
			board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
		if blank.col != 0:
			# Can move left
			board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
			moves.append(self.get_state(board))
			board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]

		return [Puzzle8Node(move, self.depth+1) for move in moves]

	def test(self):
		p = Puzzle8Node('2831647 5') # Lugar fig 3.17
		moves = p.get_moves()

		assert len(moves) == 3
		assert moves == [Puzzle8Node(move) for move in ['2831 4765', '28316475 ', '283164 75']]

def main():
	Puzzle8Node('2831647 5').test()

if __name__ == "__main__":
	main()