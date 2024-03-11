

class CurrentBoard:
	board = ""
	player1Points = 0
	player2Points = 0

	def __init__(self, string_def = " " * 16):
		self.board = string_def 
		self.state= ""
 

	def display(self, game_display = False):
		if game_display :
			index = 0
			c = "" 
			for char in self.board:
				if char == "": 
					c += str(index)
				else:
					c += char 

				index += 1

		else:
			c = self.board 

		self.display_matrix(c)

	def display_matrix(self,input_string):

		matrix = [[0] * 4 for _ in range(4)]

		for i in range(4):
			for j in range(4):
				matrix[i][j] = input_string[i * 4 + j]

		for row in matrix:
			print(" ".join(row))

	def state_of_board(self):
		if " " in self.board:
			return "U"
    
		if player1Points > player2Points:
			return "1"
		else:
			return"2"

		return "D"
 
	def other(self, piece):
		if piece == "1":
			return "2"
		return "1"


	def eq3(self):
		return 1

########### 

def get_blank_positions(board, position):
    matrix = [list(board[i:i+4]) for i in range(0, 16, 4)]

    row, col = position // 4, position % 4

    # Right cell position
    right_position = (row, col + 1) if col + 1 < 4 and matrix[row][col + 1] == ' ' else None

    # Left cell position
    left_position = (row, col - 1) if col - 1 >= 0 and matrix[row][col - 1] == ' ' else None

    # Top cell position
    top_position = (row - 1, col) if row - 1 >= 0 and matrix[row - 1][col] == ' ' else None

    # Bottom cell position
    bottom_position = (row + 1, col) if row + 1 < 4 and matrix[row + 1][col] == ' ' else None

    return right_position, left_position, top_position, bottom_position

def display_matrix_with_blank_positions(board, position):
    matrix = [list(board[i:i+4]) for i in range(0, 16, 4)]

    row, col = position // 4, position % 4

    # Display the matrix
    print("Matrix:")
    for i in range(4):
        for j in range(4):
            cell_value = matrix[i][j]
            if i == row and j == col:
                cell_value = f"[{cell_value}]"
            print(cell_value, end=' ')
        print()

    right_position, left_position, top_position, bottom_position = get_blank_positions(board, position)

    # Display blank cell positions in the original string
    print("\nBlank Cell Positions:")
    print(f"Right Cell Position: {right_position[0] * 4 + right_position[1]}" if right_position is not None else "Right Cell is not blank")
    print(f"Left Cell Position: {left_position[0] * 4 + left_position[1]}" if left_position is not None else "Left Cell is not blank")
    print(f"Top Cell Position: {top_position[0] * 4 + top_position[1]}" if top_position is not None else "Top Cell is not blank")
    print(f"Bottom Cell Position: {bottom_position[0] * 4 + bottom_position[1]}" if bottom_position is not None else "Bottom Cell is not blank")


def replace_oso(board, position):
    # Convert the string to a 4X4 
    matrix = [list(board[i:i+4]) for i in range(0, 16, 4)]

    # Extract position coordinates
    row, col = position // 4, position % 4

    # Define function to check and replace "oso" in the specified direction
    def check_and_replace(dx, dy):
        if 0 <= row + 2*dx < 4 and 0 <= col + 2*dy < 4:
            if matrix[row][col] == 'o' and matrix[row+dx][col+dy] == 's' and matrix[row+2*dx][col+2*dy] == 'o':
                matrix[row][col] = matrix[row+dx][col+dy] = matrix[row+2*dx][col+2*dy] = 'X'

    # Check and replace in all four directions
    check_and_replace(0, 1)  # Right
    check_and_replace(0, -1)  # Left
    check_and_replace(1, 0)  # Down
    check_and_replace(-1, 0)  # Up

    # Convert the updated matrix back to a string
    updated_matrix_str = ''.join([''.join(row) for row in matrix])

    return updated_matrix_str


 

######
def main():
	player1Start = True
	player2Start = True
	player1Position = 0
	player2Position = 15
	player1Points = 0
	player2Points = 0

#	response = input("Do you wish to play first (y/n) ?")
#	if (response == "y"):
	players_turn = "1"
	cb = CurrentBoard()


	for x in range(16):
		print("result " , cb.player1Points , " " , cb.player2Points)

		if players_turn == "1":
			print("Player 1")

			if player1Start == True:
				print("First move. ")
 
				player1Start = False
			else:
				display_matrix_with_blank_positions(cb.board, player1Position)

				player1Position = int(input("Choose the position "))

			letter = input ("Choose between 'O' or 'S'")
			cb.board = cb.board[:player1Position] + letter + cb.board[player1Position+1 :] 
 
			aBoard = replace_oso(cb.board, player1Position)
			if (cb.board != aBoard):
				cb.board = aBoard
				cb.player1Points += 1

 
		else:
			print("Player 2")
			if  player2Start == True:
				print("First move. ")
 
				player2Start = False
			else:
				display_matrix_with_blank_positions(cb.board, player2Position )

				player2Position = int(input("Choose the position "))

			letter = input ("Choose between 'O' or 'S'")
			cb.board = cb.board[:player2Position] + letter + cb.board[player2Position+1 :]
 
			aBoard = replace_oso(cb.board, player2Position)
			if (cb.board != aBoard):
				cb.board = aBoard
				cb.player2Points += 1

		players_turn = cb.other(players_turn)
		cb.display()
 



main()

