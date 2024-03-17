

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

	def display_matrix(self, input_string):
		matrix = [[0] * 4 for _ in range(4)]

		for i in range(4):
			for j in range(4):
				matrix[i][j] = input_string[i * 4 + j]

		for row in matrix:
			print(" ".join(row))






	def state_of_board(self):
		if " " in self.board:
			return "U"
    
		if self.player1Points > self.player2Points:
			return "oso"
		else:
			return"OSO"

		return "D"

 
	def other(self, piece):
		if piece == "oso":
			return "OSO"
		return "oso"

	def all_possible_moves(self, player_piece):
		possible_moves = []
		list = check_moves(self.board, player_piece)
 

		for index in list :
			if player_piece == "oso":
 
					possible_moves.append( CurrentBoard(self.board[:index] + "o" + self.board[index+1:]))
					possible_moves.append( CurrentBoard(self.board[:index] + "s" + self.board[index+1:]))
			else:
					possible_moves.append( CurrentBoard(self.board[:index] + "O" + self.board[index+1:]))
					possible_moves.append( CurrentBoard(self.board[:index] + "S" + self.board[index+1:]))
 
		return possible_moves

 

########### 

def replace_oso(board, position):
    # Convert the string to a 4X4 
 
    matrix = [list(board[i:i+4]) for i in range(0, 16, 4)]

    # Extract position coordinates
    row, col = position // 4, position % 4

    # Define function to check and replace "oso" in the specified direction
    def check_and_replace(dx, dy):
        if 0 <= row + 2*dx < 4 and 0 <= col + 2*dy < 4:
            if matrix[row][col].lower() == 'o' and matrix[row+dx][col+dy].lower() == 's' and matrix[row+2*dx][col+2*dy].lower() == 'o':
                matrix[row][col] = matrix[row+dx][col+dy] = matrix[row+2*dx][col+2*dy] = 'X'

    # Check and replace in all four directions
    check_and_replace(0, 1)  # Right
    check_and_replace(0, -1)  # Left
    check_and_replace(1, 0)  # Down
    check_and_replace(-1, 0)  # Up

    # Convert the updated matrix back to a string
    updated_matrix_str = ''.join([''.join(row) for row in matrix])

    return updated_matrix_str


  
def check_moves(board, player_piece):
	index = 0
	result = []

	if player_piece == "oso" and board[0] == " ":
		return [0]

	if player_piece == "OSO" and board[15] == " ":
		return [15]
	else: 
		for c in board :
 
			if c == " ":
				result += check_piece(board, index, player_piece) 
			index += 1

	return list(set(result))
 




def check_piece(board, index, player_piece):
	left = index - 1
	right = index + 1
	down = index - 4
	top = index + 4
	list = []


	if player_piece == "OSO":
		if (not (left < 0 or left == 3 or left == 7 or left == 11)) and is_upper_piece(board[left]):
				list.append(index)

		if (not (right > 15 or right == 4 or right == 8 or right == 12)) and is_upper_piece(board[right]):
				list.append(index)

		if  not (top > 15 ) and is_upper_piece(board[top]):
				list.append(index)
	
		if  not (down < 0) and is_upper_piece(board[down]):
				list.append(index)
	else:
		if (not (left < 0 or left == 3 or left == 7 or left == 11)) and is_lower_piece(board[left]):
				list.append(index)

		if (not (right > 15 or right == 4 or right == 8 or right == 12)) and is_lower_piece(board[right]):
				list.append(index)

		if  not (top > 15 ) and is_lower_piece(board[top]):
				list.append(index)
	
		if  not (down < 0) and is_lower_piece(board[down]):
				list.append(index)


	return list
 
def is_upper_piece(char):
	return char == 'S' or char == 'O'

def is_lower_piece(char):
	return char == 's' or char == 'o'


#########
# Search Tree 
 

class SearchTreeNode:

  def __init__(self,board_instance,playing_as, ply=0):
    self.children = []
    self.value_is_assigned = False
    self.ply_depth = ply
    self.current_board = board_instance
    self.move_for = playing_as
    if self.current_board.state == "U":
      self.generate_children()
    else:   # Game over
      if self.current_board.state == "D":
        self.value = 0
      else:
        if ((self.ply_depth % 2) == 0):
          self.value = -1
        else:
          self.value = 1
      self.value_is_assigned = True

  def min_max_value(self):
    if self.value_is_assigned:
      return self.value

    self.children  = sorted(self.children, key = lambda x:x.min_max_value())

    if ((self.ply_depth % 2) == 0):
      # computers move
      self.value = self.children[-1].value
    else:
      #players move
      self.value = self.children[0].value
    self.value_is_assigned = True

    return self.value

  def generate_children(self):
    for board_for_next_move in self.current_board.all_possible_moves(self.move_for):
      self.children.append(SearchTreeNode(board_for_next_move,self.current_board.other(self.move_for), ply = self.ply_depth +1))



######
def main():
	player1Start = True
	player2Start = True
	player1Position = 0
	player2Position = 15
 

#	response = input("Do you wish to play first (y/n) ?")
#	if (response == "y"):
	players_turn = "oso"
	cb = CurrentBoard()


	for x in range(16):
		print("result " , cb.player1Points , " " , cb.player2Points)

# Player oso's turn 
		if players_turn == "oso":
			print("Player oso")
			print ("possible moves \n" ,check_moves(cb.board, players_turn))

			if player1Start == True:
#  player oso's turn
				print("First move. ")
 
				player1Start = False
			else:
 
				player1Position = int(input("Choose the position "))

			letter = input ("Choose between 'o' or 's'")
			cb.board = cb.board[:player1Position] + letter + cb.board[player1Position+1 :] 
 
			aBoard = replace_oso(cb.board, player1Position)
			if (cb.board != aBoard):
				cb.board = aBoard
				cb.player1Points += 1

 
		else:
# player OSO's turn AI
			print ("possible moves \n" ,check_moves(cb.board, players_turn))
			print("Player OSO AI")

			search_tree = SearchTreeNode(cb, "OSO")
			search_tree.min_max_value()
			cb = search_tree.children[-1].current_board

 
			aBoard = replace_oso(cb.board, player2Position)
			if (cb.board != aBoard):
				cb.board = aBoard
				cb.player2Points += 1

		players_turn = cb.other(players_turn)
		cb.display()
 
	print("The winner is " , cb.state)


main()

