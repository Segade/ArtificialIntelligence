"""
The game picked for this assessment is the game that consists of a 4X4 matrix board.
There are two players. one starts from the top left corner and the second one starts from the bottom right corner.
Players must create the word "oso" as many times as they can.
moves are the closest cell to the top, bottom, left and right.
The game is finished when all the cells are filled up and the winner is the player with more words "oso" created.
For this game, the player starts from the top and left corner and the AI starts from the bottom right corner.
To differenciate the players, the player plays with lowercase and the AI with uppercase.
"""

class CurrentBoard:
	board = ""
 
 
#declaring the constructor where the board, and the scores for each player are passed
	def __init__(self, string_def = " " * 16, capital_score = 0, lower_score = 0):

#declaring the attributes and giving them the corresponding value
		self.board = string_def 
		self.state= self.state_of_board()
		self.capital_score = capital_score
		self.lower_score = lower_score
 

	def display(self, game_display = False):

#Method that displays the board situation with all the moves made

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

#		print (c)
		self.display_matrix(c)

	def display_matrix(self, input_string):
		print ("  1 2 3 4 ")
		print ("1 " , self.board[0] , "|" , self.board[1] , "|" , self.board[2] , "|" , self.board[3])
		print ("-----------")
		print ("2 " , self.board[4] , "|" , self.board[5] , "|" , self.board[6] , "|" , self.board[7])
		print ("-----------")
		print ("3 " , self.board[8] , "|" , self.board[9] , "|" , self.board[10] , "|" , self.board[11])
		print ("-----------")
		print ("4 " , self.board[12] , "|" , self.board[13] , "|" , self.board[14] , "|" , self.board[15])






	def state_of_board(self):

#Method that processes the state of the board.
#the game is Unfinished until all the cells are filled up

		if " " in self.board:
			return "U"
 
		return "F"

 
	def other(self, piece):

#Method that processes the change of player when the Search Tree algorithm works 

		if piece == "oso":
			return "OSO"
		return "oso"

	def all_possible_moves(self, player_piece):

#Method that processes all the possible moves 
#possible_movess is an array that stores all the combinations that a player can made in each situation

		possible_moves = []
		list = check_moves(self.board, player_piece)

#The check_moves returns an array with the possible cell that the corresponding player can choose 

#		print("list " , list) 


#the for loop iterates the array 
#then, depending on the player's turn assigns lower or upper letters 
#then, the options are added to the possible_moves array 


		for index in list :
			if player_piece == "oso":
					self.lower_score += count_oso(self.board[:index] + "o" + self.board[index+1:], index)
					possible_moves.append( CurrentBoard(self.board[:index] + "o" + self.board[index+1:], self.capital_score, self.lower_score))
					self.lower_score += count_oso(self.board[:index] + "s" + self.board[index+1:], index)
					possible_moves.append( CurrentBoard(self.board[:index] + "s" + self.board[index+1:], self.capital_score, self.lower_score))
			else:
					self.capital_score += count_oso(self.board[:index] + "O" + self.board[index+1:], index)
					possible_moves.append( CurrentBoard(self.board[:index] + "O" + self.board[index+1:], self.capital_score, self.lower_score))
					self.capital_score += count_oso(self.board[:index] + "S" + self.board[index+1:], index)
					possible_moves.append( CurrentBoard(self.board[:index] + "S" + self.board[index+1:], self.capital_score, self.lower_score))

#it returns the array to provide it to the Search Tree algorithm 

		return possible_moves

 

########### 
def count_oso(board, position):
    """
Method that counts the number of words "oso" the player creates using the that given position 
It checks the four directions and sum the number of words made
    """
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
        if position - 4 >= 0 and position + 4 < 16:
          if string[position-4] == 'o' and string[position+4] == 'o':
            count += 1
    
# It returns the totoal result 
    return count


  
def check_moves(board, player_piece):
	"""
Method that checks the available cells that the player can use
Depending on the player, the method checks lower or upper letters 
and checks the cells close to the corresponding player
result is the array with the available cells
index is the position of the string corresponding to the board 
	"""
	index = 0
	result = []

# if it is the first move for each player, the option is predefined 
	if player_piece == "oso" and board[0] == " ":
		return [0]

	if player_piece == "OSO" and board[15] == " ":
		return [15]
	else: 
# for loop that iterates the board looking for blank cells 
# index is incremented by 1 each iteration to calculate the position in the string 
		for c in board :
 
			if c == " ":
# check_piece finds the available cells in the given index and player 
				result += check_piece(board, index, player_piece) 
			index += 1
# It returns the final list removing the repeated values with the list and set method 
	return list(set(result))
 




def check_piece(board, index, player_piece):
	""" 
Method that checks the top, bottom, right and left cells are available for the given index 
	"""

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

# It returns the available cells for the given index 
	return list
 
def is_upper_piece(char):
# Method that checks that the letter is uppercase for the AI
	return char == 'S' or char == 'O'

def is_lower_piece(char):
# Method that checks that the letter is lowercase for the player 

	return char == 's' or char == 'o'


#########
# Search Tree 
 
# class that processes the Search  Tree algorithm 
class SearchTreeNode:

  def __init__(self,board_instance,playing_as, ply=0):
    """
Constructor that receives the board, the player#s turn and the plyvalue 
children  is the array where all the Tree stores the calculation made to determinen the best option 
value is the value that determinens how good the options are. this is set with the result of the game 
The higher the value the better for the algorithm 
max_ply determinens hthe depth of the tree, otherwise, the algorithm is creating children continuesly 
    """
    self.children = []
    self.value_is_assigned = False
    self.ply_depth = ply
    self.current_board = board_instance
    self.move_for = playing_as
    self.max_ply_depth = 6

# if the game is not finished 
# and the ply is not bigger than the maximum, the algorithm generates children 
    if self.current_board.state == "U":
      if self.ply_depth < self.max_ply_depth:
        self.generate_children()
      else:
# max ply depth here 
# the value attribute is assigned with the value of the board result 
        self.value = self.current_board.capital_score - self.current_board.lower_score
        self.value_is_assigned = True



  def min_max_value(self):
    """ 
Method that sorts the children array in ascending order 
the higher the better for the algorithm 
the bottom of the array are the best solutions for the AI
The top ar the best solutions for the player
    """

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
    """
Method that generates the children with the possible moves for the game
    """


    for board_for_next_move in self.current_board.all_possible_moves(self.move_for):
      self.children.append(SearchTreeNode(board_for_next_move,self.current_board.other(self.move_for), ply = self.ply_depth +1))



######

def main():
# Method that runs the whole program 
	player1Start = True
	player2Start = True
	player1Position = 0
	player2Position = 15
 

	response = input("Do you wish to play first (y/n) ?")
 
	players_turn = (response == "y")

 

	cb = CurrentBoard()

# in this game we know the number of moves. So the for loop is clear to 16
	for x in range(16):
#		print("result " , cb.player1Points , " " , cb.player2Points)

# Player oso's turn 
		if players_turn :
			print("Player's turn")
			print ("possible moves \n" ,check_moves(cb.board, "oso"))

			if player1Start == True:
#  player's turn
				print("First move. ")
 
				player1Start = False
			else:
 
				player1Position = int(input("Choose the position "))

			letter = input ("Choose between 'o' or 's'")
			cb.board = cb.board[:player1Position] + letter + cb.board[player1Position+1 :] 
			cb.lower_score += count_oso(cb.board, player1Position)
 
 
		else:
# player OSO's turn AI
			print("AI's turn")
			print ("possible moves \n" ,check_moves(cb.board, "OSO"))
 
# execution of the algorithm 
# It initialises the Search Tree passing the board and the AI piece used 
			search_tree = SearchTreeNode(cb, "OSO")

# It sorts all the children generated in ascending order according to the values got 

# The child with the highest value is at the bottom. So that is the one chosen for the AI
			search_tree.min_max_value()
			cb = search_tree.children[-1].current_board
 
 

		players_turn = not players_turn
 
		cb.display()
 
 


main()

