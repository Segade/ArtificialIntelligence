

class CurrentBoard:
	board = ""
	player1Points = 0
	player2Points = 0

	def __init__(self, string_def = " " * 16):
		self.board = string_def 
		self.state= self.state_of_board()
 

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

		print (c)
#		self.display_matrix(c)

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

		list = check_moves(self.board, "OSO")
 
		for i in list:
			self.player2Points += count_oso(self.board, i)

		list = check_moves(self.board, "oso")

		for i in list:
			self.player1Points += count_oso(self.board, i)


		if self.player1Points > self.player2Points:
			return "oso"
		elif self.player2Points > self.player1Points:
			return"OSO"
		else:
			return "D"

 
	def other(self, piece):
		if piece == "oso":
			return "OSO"
		return "oso"

	def all_possible_moves(self, player_piece):
		possible_moves = []
		list = check_moves(self.board, player_piece)
#		print("list " , list) 

		for index in list :
			if player_piece == "oso":
 
					possible_moves.append( CurrentBoard(self.board[:index] + "o" + self.board[index+1:]))
					possible_moves.append( CurrentBoard(self.board[:index] + "s" + self.board[index+1:]))
			else:
					possible_moves.append( CurrentBoard(self.board[:index] + "O" + self.board[index+1:]))
					possible_moves.append( CurrentBoard(self.board[:index] + "S" + self.board[index+1:]))
 
		return possible_moves

 

########### 
def count_oso(board, position):
    count = 0
    string = board.lower()  # Convert the string to lowercase for case-insensitive comparison
    row, col = position // 4, position % 4
    
    # Check right
    if col <= 1 and string[row*4 + col: row*4 + col + 3] == 'oso':
        count += 1
    
    # Check left
    if col >= 2 and string[row*4 + col - 2: row*4 + col + 1] == 'oso':
        count += 1
    
    # Check down
    if row <= 1 and string[row*4 + col: row*4 + col + 9: 4] == 'oso':
        count += 1
    
    # Check up
    if row >= 2 and string[(row - 2)*4 + col: row*4 + col + 1: 4] == 'oso':
        count += 1
    
    # Check middle (if position is the middle letter)
    if string[position] == 's':
        # Check right and left
        if string[position-1] == 'o' and string[position+1] == 'o':
            count += 1
        # Check up and down
        if string[position-4] == 'o' and string[position+4] == 'o':
            count += 1
    
    return count


  
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
    self.max_ply_depth = 6
    if self.current_board.state == "U":
      if self.ply_depth < self.max_ply_depth:
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
#		print("result " , cb.player1Points , " " , cb.player2Points)

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
 
 
 
		else:
# player OSO's turn AI
			print ("possible moves \n" ,check_moves(cb.board, players_turn))
			print("Player OSO AI")
#			for x in cb.all_possible_moves("OSO"):
#				print("all possible moves " , x.board)
			search_tree = SearchTreeNode(cb, "OSO")
			search_tree.min_max_value()
			cb = search_tree.children[-1].current_board
 
 

		players_turn = cb.other(players_turn)
		print ("state " , cb.state)
		cb.display()
 
	print("The winner is " , cb.state)


main()

