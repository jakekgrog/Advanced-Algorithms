class TicTacToe:
	def __init__(self, lastmoves=None):
		self.board = ['_' for x in range(9)]
		if lastmoves == None:
			self.lastmoves = []
		else:
			self.lastmoves = lastmoves
		self.winner = None

	def print_board(self):
		board_matrix = [["-" for x in range(3)] for x in range(3)]
		string_state = "".join(self.board)
		index = 0
		for row in range(3):
			for col in range(3):
				board_matrix[row][col] = string_state[index]
		
		print("-------------")
		for x in board_matrix:
			s = "| "
			for y in x:
				s += y + " | "
			print(s)
			print("-------------")

	def get_free_positions(self):
		moves = []
		for i, v in enumerate(self.board):
			if v == "_":
				moves.append(i)
		return moves				

	def place(self, mark, pos):
		self.board[pos] = mark
		self.lastmoves.append(pos)

	def undo(self):
		self.board[self.lastmoves.pop(0)] = "_"
		self.winner = None

	def is_gameover(self):
		win_pos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 7)]
		for i, j, k in win_pos:
			if self.board[i] == self.board[j] == self.board[k] and self.board[i] != "_":
				self.winner = self.board[i]
				return True
		if "_" not in self.board:
			self.winner = "_"
			return True
		return False

	def play(self, player1, player2):
		self.p1 = player1
		self.p2 = player2

		for i in range(9):
			self.print_board()
			if i%2 == 0:
				self.p1.move(self)
			else:
				self.p2.move(self)
			if self.is_gameover():
				self.print_board()
				if self.winner == "_":
					print("Game Draw")
				else:
					print("Winner is {}".format(self.winner))

class AI:
	def __init__(self, type):
		self.type = type
		if self.type == "X":
			self.opponent = "O"
		else:
			self.opponent = "X"

	def move(self, board):
		move_pos, score = self.maximized_move(board)
		board.place(self.type, move_pos)

	def maximized_move(self,board):
		''' Find maximized move'''    
		bestscore = None
		bestmove = None

		positions = board.get_free_positions()

		for m in positions:
			board.place(self.type,m)
        
			if board.is_gameover():
				score = self.get_score(board)
			else:
				move_position,score = self.minimized_move(board)
        
		board.undo()
    
		if bestscore == None or score > bestscore:
			bestscore = score
			bestmove = m

		return bestmove, bestscore

	def minimized_move(self,board):
		''' Find the minimized move'''

		bestscore = None
		bestmove = None

		for m in board.get_free_positions():
			board.place(self.opponent,m)
        
			if board.is_gameover():
				score = self.get_score(board)
			else:
				move_position,score = self.maximized_move(board)
        
			board.undo()
            
			if bestscore == None or score < bestscore:
				bestscore = score
				bestmove = m

		return bestmove, bestscore

	def get_score(self,gameinstance):
		if gameinstance.is_gameover():
			if gameinstance.winner  == self.type:
				return 1 # Won

			elif gameinstance.winner == self.opponent:
				return -1 # Opponent won

			return 0 # Draw

def main():
	board = TicTacToe()
	player1 = AI("X")
	player2 = AI("O")
	board.play(player1, player2)

if __name__=="__main__":
	main()
