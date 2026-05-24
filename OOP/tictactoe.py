# Tic Tac Toe game using AI
# class TicTacToe:
# 	def __init__(self):
# 		self.board = [" "] * 9
# 		self.current = "X"

# 	def display(self):
# 		b = self.board
# 		print(f" {b[0]} | {b[1]} | {b[2]} ")
# 		print("---+---+---")
# 		print(f" {b[3]} | {b[4]} | {b[5]} ")
# 		print("---+---+---")
# 		print(f" {b[6]} | {b[7]} | {b[8]} ")

# 	def make_move(self, pos):
# 		if pos < 1 or pos > 9:
# 			return False
# 		if self.board[pos - 1] != " ":
# 			return False
# 		self.board[pos - 1] = self.current
# 		return True

# 	def switch(self):
# 		self.current = "O" if self.current == "X" else "X"

# 	def winner(self):
# 		b = self.board
# 		lines = [
# 			(0,1,2),(3,4,5),(6,7,8),
# 			(0,3,6),(1,4,7),(2,5,8),
# 			(0,4,8),(2,4,6)
# 		]
# 		for a,b_,c in lines:
# 			if b[a] == b[b_] == b[c] and b[a] != " ":
# 				return b[a]
# 		if all(cell != " " for cell in self.board):
# 			return "Draw"
# 		return None

# def main():
# 	game = TicTacToe()
# 	print("Tic Tac Toe")
# 	while True:
# 		game.display()
# 		try:
# 			move = int(input(f"Player {game.current}, enter position (1-9): "))
# 		except Exception:
# 			print("Invalid input")
# 			continue
# 		if not game.make_move(move):
# 			print("Invalid move")
# 			continue
# 		res = game.winner()
# 		if res:
# 			game.display()
# 			if res == "Draw":
# 				print("It's a draw.")
# 			else:
# 				print(f"Player {res} wins!")
# 			break
# 		game.switch()

# if __name__ == '__main__':
# 	main()
