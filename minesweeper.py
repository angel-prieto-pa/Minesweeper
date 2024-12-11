### Valuable assets used by the code that never get reset or changed ### ==============================================================


## Dictionaries  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# tkinter is a very prominent aspect of our project, because it is what assists in making the graphical interface.
# With the tkinter libray, we were able to create a window, use buttons and labels, bind mouse actions and 
# create our stopwatch.
from tkinter import * # Imports the tkinter library

# random is used in this game in order to get the location of the bombs
import random # Imports random


## Creating the Window  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  -

window = Tk() # Creates the window named "window"
window.title("Minesweeper") # Titles the window "Minesweeper"
window.configure(background = "light gray") # Sets color of window


## Images  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# These are all the images used in the code on buttons and on labels that have been sized to fit their respective 
# place using "subsample".
flag = PhotoImage(file = "assets/flag.png")
flag_sized = flag.subsample(45, 35)
question = PhotoImage(file = "assets/question.png")
question_sized = question.subsample(22,22)
happy = PhotoImage(file = "assets/happy.png")
happy_sized = happy.subsample(2, 2)
dead = PhotoImage(file = "assets/dead.png")
dead_sized = dead.subsample(20, 20)
cool = PhotoImage(file = "assets/cool.png")
cool_sized = cool.subsample(15, 15)
shock = PhotoImage(file = "assets/shock.png")
shock_sized = shock.subsample(3, 3)
mine = PhotoImage(file = "assets/mine.png")
mine_sized = mine.subsample(12,12)

# imagevar can be seen as a dummy image used to size labels and buttons which rely on either an image or text
# without an image or text, the size of the widget (name of assests on window) would be determined by the computer
# as a result, we used imagevar to ensure a consistent size
imagevar = PhotoImage()


## Lists  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# These two lists are practical in assigning values to buttons, labels, mines, flags, and question marks, they are also
# efficient when used with for loops to create grids out of lists or dictionaries
a_h = ["a","b","c","d","e","f","g","h"] # Creates a list "a-h"
to_8 = range(1,9) # Creates a list 1-8


### Reset

## Reset is responsible for being the foundation for the game and sets all the values to begin, as well as being able to reset it, 
## it is controlled by the control button. Everything is global in reset() in order for other functions to access it.

def reset():

	##Setup  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

	if control_button.cget("image") == "pyimage6" or control_button.cget("image") == "pyimage8" or control_button.cget("image") == "pyimage10" or start:

		start = False # To ensure it doesn't occur twice

		## Creating the board  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

		# The following code creates a dictionary that allows us to call a specific number on the board by using -- board["letter"][num]
		global board
		board = {}

		for col in a_h:	# Creates a dictionary for each column
			board[col] = {}
			for row in to_8: # Fills each column's dictionary with rows, from 1 to 8, with a value of 0
				board[col][row] = [0]

		## Creating the board interface  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  -- 

		# The following code uses for loops to create a grid of buttons which are placed in the board list. Additionally
		# it labels the button as "not_clicked" which is only ever used to test if a button has been clicked at all.
		# Furthermore, it binds the left and right click to 1) change to shock face when button is clicked, as in the original
		# game, and 2) perform their intended actions (left: to reveal what's under the button when clicked and to empty
		# clear tiles) (right: to place flags or question marks)
		for colname in a_h:
			for rownum in to_8:
				board[colname][rownum].append(Button(window, image = imagevar, width = 30, height = 25))
				board[colname][rownum][1].grid(row = to_8.index(rownum) + 2, column = a_h.index(colname))
				board[colname][rownum].append("not clicked")
				def lambda_for_position(col, row):
					return lambda event: click(event, col, row)
				board[colname][rownum][1].bind("<Button-1>", change_button_shock)
				board[colname][rownum][1].bind("<Button-2>", change_button_shock)
				board[colname][rownum][1].bind("<ButtonRelease-1>",lambda_for_position(colname, rownum))
				board[colname][rownum][1].bind("<ButtonRelease-2>", lambda_for_position(colname, rownum))

		control_button.configure(image = happy_sized)
		control_button.grid(row = 0, column = 3, columnspan = 2, sticky = "nswe")

		global bombs
		bombs = [] # All of the bombs coordinates will be in this list

		# The set up of the timer and flag label, as well as their location
		global timer_label
		timer_label = Label(window, text = "000", font = ("arial", 16, "bold"), foreground = "red", bg = "black", borderwidth = 5, relief = "ridge", width = 2, height = 2)
		timer_label.grid(row = 0, columnspan = 2, sticky = "nswe")
	
		global flag_label
		flag_label = Label(window, text = "010", font = ("arial", 16, "bold"), foreground = "red", bg = "black", borderwidth = 5, relief = "ridge", width = 2, height = 2)
		flag_label.grid(row = 0, column = 6, columnspan = 2, sticky = "nswe")

		global state
		state = "-" # state is used to signify if a game is normal, lost, or won
		
		global delete
		delete = [] # delete is a list that contains all buttons that were destroyed and replaced with labels
		
		global flags
		flags = 10 # flags counts the number of flags a user has left
		
		global running
		running = False # used by stopwatch to determine if it should be running
		
		global counter
		counter = 0 # counts the number of seconds


### Functions ### ======================================================================================================================



## Game Value  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# Used to work the stopwatch
def stopwatch(label):
	def count():
		global counter # ensures access to counter, which is defined outside
		if running: # must be running in order to work
			label.configure(text = '{:03}'.format(counter)) # sets text to counter in the form of "000"
			label.after(1000, count) # waits a second before proceeding to change label again
			counter += 1
	count()

# Function used to determine the color of the number that shows how many bombs surround it
# Colors are based off the original Minesweeper* 
# Used to make labels
def image_color(num):
	global colors # colors made global fo
	colors = ["blue", "green", "red", "navy", "maroon", "teal", "black", "gray"]
	color_value = num - 1 # index of value
	return colors[color_value] #returns the color based off the index of value

# When coding the game, I realized how versatile this block was, so I used it for several different functions. check() returns a
# different value dependent on what you want it to do.
def check(col, row, func):

	# The lists include all possible options of a tile in a 3 x 3 square
	check_col = [col - 1, col, col + 1]
	check_row = [row - 1, row, row + 1]

	# The pupose of the list is to check the tiles that surround it, while limiting it if on the edge, which is what deleting
	# certain values does. 
	if col == 0:
		check_col.pop(0)
	elif col == 7:
		check_col.pop()

	if row == 1:
		check_row.pop(0)
	elif row == 8:
		check_row.pop()

	# The Variables
	value = 0 # value is the variable that is returned to indicate how many bombs surround a tile
	bubble_values = [] # bubble_values returns the 8 locations of the tiles that surround the middle tile
	new_delete = [] # new_delete returns all the values that need to be deleted because they're in an empty patch of tiles,
					# which ultimately creates the empty patch of tiles with numbers enclosing buttons, that allows you to
					# efficiently play the game (*It sounds more complicated than it is)
					#
					# new_delete differs from delete in that delete is a very accessible variable that contains all buttons
					# deleted, in contrast, new_delete are the values that have not yet been deleted
	
	# The Function

	# The for loops check all values of a 3 x 3 square, if not on the edge
	for col_value in check_col:
		col_value_letter = a_h[col_value]
		for row_value in check_row:

			location = col_value_letter + str(row_value) # Assigns name to coordinates

			# If there is a bomb that in the perimeter of the tile clicked, then it increments one to the value
			# We ultimately get a value of the bombs around a position
			if func == "values":
				if board[col_value_letter][row_value][0] == "X":
					value += 1

			# This one's a bit trickier*
			# If surrounding tile has not yet been deleted, it is added to delete and new_delete
			# The role of new_delete is to be a list will be deleted in the forseeable future in the function delete_surrounding()
			# It adds all locations of a 3 x 3 block, whose center is 0, and does so recursively
			elif func == "delete":
				if location not in delete:
					delete.append(location)
					new_delete.append(location)
					if board[col_value_letter][row_value][0] == 0:
						for values in check(col_value, row_value, "delete"):
							new_delete.append(values)

			# Adds all the locations that surround a tile into a list
			elif func == "click_bubble":
				bubble_values.append(location)

	# Returns values based on the function
	if func == "values":
		return value
	elif func == "click_bubble":
		return bubble_values
	elif func == "delete":
		return new_delete


# The following code produces 10 non-duplicate bombs, that avoid the 8 blocks that surround where the first tile is clicked. In
# addition to that the second part of the code assigns the tiles with their values as to how many bombs surround their 8 block
# perimeter.
def make_bombs(col, row):

	# Making the bombs

	# col_index is used in order to manipulate the column value and check columns before and after it with the function "check()"
	col_index = a_h.index(col)
	# The function check is used to indicate the tiles that surround the first click, which are the bubble values
	bubble_values = check(col_index, row, "click_bubble")
	while len(bombs) != 10: # The while loop ensures we have 10 bombs, the amount in an 8 x 8 game of minesweeper
		random_letter = a_h[random.randint(0, len(a_h)-1)] # Chooses a random letter from a_h, based off its index in the list
		random_number = random.randint(1, len(to_8)) # Chooses a random number from 1 to 8
		location = random_letter + str(random_number) # String name for the coordinates
		if location not in bubble_values: # This if ensures that a bomb is not placed in the 8 tiles surrounding the first click
			if location not in bombs: # The if ensures we don't have two of the same bombs in our list
				board[random_letter][random_number][0] = "X" # X is a value in board that we define as the bomb
				bombs.append(location) # Adds the bomb name to the list

	# Assigning values

	# Uses for loops to ensure every block is given a number.
	for col in range(0,8): # This step is to make sure column's index is used in check()
		col_val = a_h[col]
		for row in to_8:
			if board[col_val][row][0] != "X": # Ensures that bombs aren't replaced with number values
				board[col_val][row][0] = check(col, row, "values") # check() returns the intended value for the tile


# The following code is intended to return True or False depending if the click was the first or not, which is used in order to 
# ensure that on the first click the bomb is not withing the 8 tiles that surround it. Since values are only labeled "clicked"
# upon releasing the button, one click means that we need a value of one to determine if it was first or not.
def first_click():
	value = 0
	for colname in a_h: # The loops check the board to count how many clicks there have been.
		for rownum in to_8:
			if board[colname][rownum][2] == "clicked":
				value += 1
	if value == 1: # If there has only been one click it reports True, if not it reports False.
		return True
	else:
		return False

# The following code is intended to return True or False depending if the click is the last non-bomb tile, thus making a win.
def last_click():
	if len(delete) == 54: # if delete is 54, meaning it has deleted all buttons except for the bombs then it will report True to click
		return True
	else:
		return False

## Interface  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# The following functions change to the shocked face when a button is clicked and return back to the normal happy face after
# button is released. (*Note that this does not occur when the game is lost, since the face remains as dead)
def change_button_shock(event):
	if control_button.cget("image") != "pyimage8" and control_button.cget("image") != "pyimage10": # Uses cget to ensure face isn't changed if dead (pyimage8 = 8th image defined)
		control_button.configure(image = shock_sized) # Updates button image to labeled one, in this case "shock_sized"

def change_button_normal(event):
	if control_button.cget("image") != "pyimage8" and control_button.cget("image") != "pyimage10":
		control_button.configure(image = happy_sized)

# The function loss reveals all the bombs (salmon: if that bomb was clicked, green: if that bomb was flagged, pink: when revealed)
def loss(clicked):
	index = bombs.index(clicked) # ensures button, which has already been destroyed by click does not affect code
	bombs.pop(index)

	for mine in bombs: # Will delete all buttons in the list location and reveal bombs

		# Specifies row and col, based off their string coordinate
		col = mine[0]
		row = int(mine[1])

		# Determines color of label, as explained in the description
		if board[col][row][1].cget("image") == "pyimage2":
			color = "light green"
		else:
			color = "pink"

		# Destroys button and replaces it with a label showing bomb, indicating that bombs have exploded
		board[col][row][1].destroy()
		board[col][row][1] = Label(window, image = mine_sized, bg = color, borderwidth = 2, relief = "sunken", width = 32, height = 27)
		board[col][row][1].grid(row = to_8.index(row) + 2, column = a_h.index(col), sticky = "nswe")

# The function win reveals all the bombs (yellow: if that bomb was not flagged, green: if that bomb was flagged)
# Very similar to loss, so will not go over
def win():

	for mine in bombs: # Will delete all buttons in the list location and reveal bombs

		# Specifies row and col, based off their string coordinate
		col = mine[0]
		row = int(mine[1])

		# Determines color of label, as explained in the description
		if board[col][row][1].cget("image") == "pyimage2":
			color = "light green"
		else:
			color = "light yellow"

		# Destroys button and replaces it with a label showing bomb, indicating that bombs have exploded
		board[col][row][1].destroy()
		board[col][row][1] = Label(window, image = mine_sized, bg = color, borderwidth = 2, relief = "sunken", width = 32, height = 27)
		board[col][row][1].grid(row = to_8.index(row) + 2, column = a_h.index(col), sticky = "nswe")

# Deletes the surrounding blocks 
def delete_surrounding(col, row):
	check_col = a_h.index(col) # uses column's index in order to use check
	new = check(check_col, row, "delete") # uses check to determine new values to delete
	
	clicked = col + str(row) # coordinate name is given to clicked value
	if len(new)!= 0: # if there are no new values to delete nothing needs to be done
		for locations in new: # for all the values it will deleter their button and replace it with a blank space or number accordingly
			
			temp_col = locations[0]
			temp_row = int(locations[1])

			if board[temp_col][temp_row][1].cget("image") != "pyimage2":	# ensures flagged buttons aren't destroyed		
				
				# destroys button and gets row and col from location coordinate
				board[temp_col][temp_row][1].destroy()
				

				# Assigns them a label accordingly
				if board[temp_col][temp_row][0] == 0:
					board[temp_col][temp_row][1] = Label(window, image = imagevar, borderwidth = 2, relief = "sunken", width = 32, height = 27)
				elif board[col][row][0] != "X":
					board[temp_col][temp_row][1] = Label(window, text = board[temp_col][temp_row][0], font = ("Monaco", 15, "bold"), foreground = image_color(board[temp_col][temp_row][0]), borderwidth = 2, relief = "sunken", width = 1, height = 1)
				board[temp_col][temp_row][1].grid(row = to_8.index(temp_row) + 2, column = a_h.index(temp_col), sticky = "nswe")

				# the function of the following for lines is to show the shock face when mouse clicked on labels like on the original game
				board[temp_col][temp_row][1].bind("<Button-1>", change_button_shock)
				board[temp_col][temp_row][1].bind("<Button-2>", change_button_shock)
				board[temp_col][temp_row][1].bind("<ButtonRelease-1>", change_button_normal)
				board[temp_col][temp_row][1].bind("<ButtonRelease-2>", change_button_normal)


				if last_click():
					control_button.configure(image = cool_sized)
					running = False
					state = "won"
					win()
# click is responsible for several actions, I would examin line by line, but the gist is that it acts accordingly to a mouse press

def click(event, col, row):
	# global ensures that this function can access state, which indicates if we have lost or won, and running, used to indicate
	# is stopwatch is runnning.
	global state
	global running

	# After button is released this code executes, thus we must change the face button back to happy.
	change_button_normal(event)
	# The following if statement ensures we have not won or lost, in which all buttons stop functioning.
	if state == "-":
		# provides location coordinates without replacing variable
		location = lambda: col + str(row)
		# when a button is left clicked
		if event.num == 1:

			if board[col][row][1].cget("image") != "pyimage2": # ensures flagged bomb can't be destroyed
				
				delete.append(location())
				board[col][row][1].destroy() # destroys the button that was clicked
				board[col][row][2] = "clicked" # sets list item indicating it has been clicked

				if first_click(): # validates if it is the first click
					control_button.configure(state = "normal") # face button set to "normal" after it being disabled when 
															   # board is full of buttons (done to prevent it from being closed without a move)
					# begin stopwatch
					running = True
					stopwatch(timer_label)

					# begins making bombs, ensuring that the 3 x 3 square surrounding the clicked tile is empty
					make_bombs(col, row)

					# replaces destroyed button with label (either empty or showing a number)
					board[col][row][1] = Label(window, image = imagevar, borderwidth = 2, relief = "sunken", width = 32, height = 27)

					# deletes surrounding area since first click is for sure empty
					delete_surrounding(col, row)

				elif last_click(): #

					# replaces destroyed button with label (either empty or showing a number)
					board[col][row][1] = Label(window, image = imagevar, borderwidth = 2, relief = "sunken", width = 32, height = 27)

					control_button.configure(image = cool_sized)
					running = False
					state = "won"
					win()

				else: 
					# when it is not the first click

					# if the board encounters a blank space, it deletes it and all surrounding spaces
					if board[col][row][0] == 0:
						board[col][row][1] = Label(window, image = imagevar, borderwidth = 2, relief = "sunken", width = 32, height = 27)
						delete_surrounding(col, row)

					# if the board hits a bomb, it destroyes the space, stops the clock, changes face button to dead, and states a loss to other function
					elif board[col][row][0] == "X":
						control_button.configure(image = dead_sized)
						running = False
						board[col][row][1] = Label(window, image = mine_sized, bg = "salmon", borderwidth = 2, relief = "sunken", width = 32, height = 27)
						state = "loss"
						loss(location())

					# if it hits a regular number it deletes the button clicked and shows the number of bombs that surround it
					else:
						board[col][row][1] = Label(window, text = board[col][row][0], font = ("Monaco", 15, "bold"), foreground = image_color(board[col][row][0]), borderwidth = 2, relief = "sunken", width = 1, height = 1)
					
				board[col][row][1].grid(row = to_8.index(row) + 2, column = a_h.index(col), sticky = "nswe")
				
				# explained in delete_surrounding()
				board[col][row][1].bind("<Button-1>", change_button_shock)
				board[col][row][1].bind("<Button-2>", change_button_shock)
				board[col][row][1].bind("<ButtonRelease-1>", change_button_normal)
				board[col][row][1].bind("<ButtonRelease-2>", change_button_normal)
		
		# When a button is right clicked
		elif event.num == 2:
			global flags # ensures access to flags

			# if image on button is a question mark it makes it blank
			if board[col][row][1].cget("image") == "pyimage4":
				board[col][row][1].configure(image = imagevar, width = 30, height = 25)

			# if image on button is a flag it makes it a quaestion mark and adds a flag back, then corrects counter
			elif board[col][row][1].cget("image") == "pyimage2":
				board[col][row][1].configure(image = question_sized, width = 30, height = 25)
				flags += 1
				flag_label.configure(text = '{:03}'.format(flags))

			# once there are no more flags all right clicks turn into question marks or blanks
			elif flags == 0:
				board[col][row][1].configure(image = question_sized, width = 30, height = 25)

			# if button is blank it makes it a flag and reduces a flag, then corrects counter
			else:
				board[col][row][1].configure(image = flag_sized, width = 30, height = 25)
				flags -= 1
				flag_label.configure(text = '{:03}'.format(flags))


### The Following Code Begins the Game ### ===============================================================================================

# The set-up of the face button, it's location and it's action if pressed
control_button = Button(window, image = happy_sized, width = 10, height = 25, relief = "raised", borderwidth = 5, bg = "dark gray", state = "disable", command = reset)

# Is what makes the initial game
reset()

### =================================================================================================================================================

window.mainloop() # executes widgets until the program is closed

# Testing

# This test is meant to show that the color we give blocks is the correct one according to the list we assigned.

# This block was helpful in making because at one point we were struggling to determine why our numbers did not have any colors.
def test(num):
	if image_color(num) ==  colors[num - 1]:
		return True
	else:
		return False

