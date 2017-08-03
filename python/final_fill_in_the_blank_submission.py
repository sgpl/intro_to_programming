# IPND Stage 2 Final Project

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

###### REQUIREMENTS
# game has ~3 levels /done
# each level has 4 or more blanks /done

# when game begins, user should select difficulty level /done
# game begins at that level of difficulty /done

# when player guesses correctly, the correct response filled in is displayed /done

# when player guesses incorrectly, they are prompted to try again

# use functions to automate tasks /done

# functions aren't longer than 18 lines /done 

# functions are producing appropriate outputs /done

# use string for text, lists for ordered data and nested lists as appropriate /done

# use loops /done

# each function includes a comment that explains intended behaviour and inputs and outputs

# extra credit: Let the user decide how many wrong guesses they can make before they lose


q_1_1 = """[1]______ lists the contents of a directory. 
[2]______ is the command that can be used to change your working 
directory. [3]______ prints your current working directory and 
[4]______ is the command used to create a new directory!"""
# ls, cd, pwd, mkdir
q_1_2 = """[1]______ is the command used to create a new 
directory, [2]______ is a command used to permanently remove a file. 
[3]______ permanently removes an empty directory and [4]______ is 
a command that creates a new file with a specified extension or file type."""
# mkdir, rm, rmdir, touch
q_1_3 = """rm -ri permanently removes a [1]______ and it's 
contents with confirmation. [2]______ is a command used to make a 
new directory. [3]______ permanently removes an empty directory and 
[4]______ permanently removes a file."""
# directory, mkdir, rmdir, rm
q_1_4 = """[1]______ is a general-purpose interpreted, interactive, 
object-oriented, and high-level [2]______ language. A [3]______ is 
created with the def keyword. Using [4]______(some_object) returns 
the number of top-level items contained in the object being queried."""
# python, programming, function, len

q_and_a = [[q_1_1, ["ls", "cd", "pwd", "mkdir"]], [q_1_2, ["mkdir", "rm", "rmdir", "touch"]], [q_1_3, ["directory", "mkdir", "rmdir", "rm"]], [q_1_4, ["python", "programming", "function", "len"]]]

blanks_list  = ["[1]______", "[2]______", "[3]______", "[4]______"]

# intended behaviour: outputs a blank (used when asking user for input) 
# inputs: takes in a word, and a list of blanks
# outputs: none if the condition is not met. otherwise it returns a blank (from list of blank) corresponding to word
def blanks_in_question(blank, list_of_blanks):
    for xx in list_of_blanks:
        if xx in blank:
            return xx
    return None


# intended behaviour: takes in some text and displays it in a fancy format
# inputs: text
# outputs: text with some fancy borders
def print_fancy_heading(heading_text):
	heading_text = "| " + heading_text + " |"
	border = len(heading_text)
	print " " 
	print "-" * border
	print heading_text
	print "-" * border
	print " "


# intended behaviour: outputs game over when a game is over
# inputs: none
# outputs: game over with some fancy asterix around it
def game_over():
	print "* " * 20
	print "* " * 20
	print " "* 9, "G A M E   O V E R"
	print "* " * 20
	print "* " * 20
	exit()


# intended behaviour: asks user if they want to try again and outputs a corresponding response
# inputs: entered by user
# outputs: starts game again or exits depending on the user's choice
def try_again(yes_or_no):
	if yes_or_no == "yes" or yes_or_no == "Yes" or yes_or_no == "y":
		# level_1(input_difficulty)
		start_game()
	else: 
		game_over()
		exit()

# intended behaviour: checks if the answers that the user has provided match the correct answer
# inputs: user's answer and a list of correct answers
# outputs: game over if both inputs don't match, returns True if inputs match
def answer_checker(user_answers, answer_list):
	if user_answers == answer_list: 
		return True
	else: 
		game_over()

# intended behaviour: takes in question, list of pre-defined blanks, and a number corresponding to a level (minus 1)
# inputs: three inputs as listed above
# outputs: meat of the fill in the blanks game / correct response if user enters correct response / game over otherwise. 
def level_functionality(question, blanks_list, levelx):
	print q_and_a[levelx][0]
	replaced = []
	list_of_user_answers = []
	question = q_and_a[levelx][0].split()
	for element in question: 
		replacement = blanks_in_question(element, blanks_list)
		if replacement != None: 
			user_input = raw_input("Fill in the answer for: " + replacement + " ")
			list_of_user_answers.append(user_input)
			element = element.replace(replacement, user_input)
			replaced.append(element)
		else: 
			replaced.append(element)
	replaced = " ".join(replaced)
	answer_checker(q_and_a[levelx][1], list_of_user_answers)
	print replaced


# def level_1(question, blanks_list):
# 	print q_and_a[0][0]
# 	replaced = []
# 	list_of_user_answers = []
# 	question = q_and_a[0][0].split()
# 	for element in question: 
# 		replacement = blanks_in_question(element, blanks_list)
# 		if replacement != None: 
# 			user_input = raw_input("Fill in the answer for: " + replacement + " ")
# 			list_of_user_answers.append(user_input)
# 			element = element.replace(replacement, user_input)
# 			replaced.append(element)
# 		else: 
# 			replaced.append(element)
# 	replaced = " ".join(replaced)
# 	answer_checker(q_and_a[0][1], list_of_user_answers)
# 	print replaced

# def level_2(question, blanks_list):
# 	print q_and_a[1][0]
# 	replaced = []
# 	list_of_user_answers = []
# 	question = q_and_a[1][0].split()
# 	for element in question: 
# 		replacement = blanks_in_question(element, blanks_list)
# 		if replacement != None: 
# 			user_input = raw_input("Fill in the answer for: " + replacement + " ")
# 			list_of_user_answers.append(user_input)
# 			element = element.replace(replacement, user_input)
# 			replaced.append(element)
# 		else: 
# 			replaced.append(element)
# 	replaced = " ".join(replaced)
# 	answer_checker(q_and_a[1][1], list_of_user_answers)
# 	print replaced

# def level_3(question, blanks_list):
# 	print q_and_a[2][0]
# 	replaced = []
# 	list_of_user_answers = []
# 	question = q_and_a[2][0].split()
# 	for element in question: 
# 		replacement = blanks_in_question(element, blanks_list)
# 		if replacement != None: 
# 			user_input = raw_input("Fill in the answer for: " + replacement + " ")
# 			list_of_user_answers.append(user_input)
# 			element = element.replace(replacement, user_input)
# 			replaced.append(element)
# 		else: 
# 			replaced.append(element)
# 	replaced = " ".join(replaced)
# 	answer_checker(q_and_a[2][1], list_of_user_answers)
# 	print replaced

# intended behaviour: starts the game and asks user for what level they want to start at
# inputs: user's choice in level of difficulty
# outputs: takes user to corresponding level of difficulty in the game. 
def start_game(): 
	print_fancy_heading("WELCOME TO THE GAME")
	print """The objective of the game is to fill in the blanks correctly. \nThis game has three levels of difficulty. Please enter: \n"1" for Easy \n"2" for Medium \n"3" for Hard"""
	input_difficulty = raw_input("Choose level of difficulty: " )
	if input_difficulty == str(1): 
		print_fancy_heading("Level 1: Easy")
		level_functionality(q_and_a, blanks_list, 0)
	elif input_difficulty == str(2): 
		print_fancy_heading("Level 2: Medium")
		level_functionality(q_and_a, blanks_list, 1)
	elif input_difficulty == str(3): 
		print_fancy_heading("Level 3: Hard")
		level_functionality(q_and_a, blanks_list, 2)
	else: 
		yes_or_no = raw_input("I'm sorry, but you didn't follow the instructions :'( \nWould you like to start again? Enter: 'yes' or 'no': " )
		try_again(yes_or_no)

start_game()

