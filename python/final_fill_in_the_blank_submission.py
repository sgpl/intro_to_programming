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
# when player guesses incorrectly, they are prompted to try again / done
# use functions to automate tasks /done
# functions aren't longer than 18 lines /done 
# functions are producing appropriate outputs /done
# use string for text, lists for ordered data and nested lists as appropriate /done
# use loops /done
# each function includes a comment that explains intended behaviour and inputs and outputs /done
# TODO: extra credit: Let the user decide how many wrong guesses they can make before they lose

_questions_ = { 
	'easy': {
		'prompt' : '[1]______ lists the contents of a directory. [2]______ is the command that can be used to change your working directory. [3]______ prints your current working directory and [4]______ is the command used to create a new directory!',
		'answer': ['ls', 'cd', 'pwd', 'mkdir']
	},
	'medium': { 
		'prompt' : '[1]______ is the command used to create a new directory, [2]______ is a command used to permanently remove a file. [3]______ permanently removes an empty directory and [4]______ is a command that creates a new file with a specified extension or file type.',
		'answer': ['mkdir', 'rm', 'rmdir', 'touch']
	},
	'hard': {
		'prompt' : 'rm -ri permanently removes a [1]______ and it\'s contents with confirmation. [2]______ is a command used to make a new directory. [3]______ permanently removes an empty directory and [4]______ permanently removes a file.',
		'answer': ['directory', 'mkdir', 'rmdir', 'rm']
	}
	}

blanks_list  = ["[1]______", "[2]______", "[3]______", "[4]______"]


def blanks_in_question(blank, list_of_blanks):
	"""
	intended behaviour: outputs a blank (used when asking user for input) 
	inputs: takes in a word, and a list of blanks
	outputs: none if the condition is not met. otherwise it returns a blank (from list of blank) corresponding to word
	"""
	for current_element in list_of_blanks:
		if current_element in blank:
			return current_element
	return None


def print_fancy_heading(heading_text):
	"""
	intended behaviour: takes in some text and displays it in a fancy format
	inputs: text
	outputs: text with some fancy borders
	"""
	heading_text = "| " + heading_text + " |"
	border = len(heading_text)
	print " " 
	print "-" * border
	print heading_text
	print "-" * border
	print " "



def game_over():
	"""
	intended behaviour: outputs game over when a game is over
	inputs: none
	outputs: game over with some fancy asterix around it
	"""
	asterix_multiplier = 20
	space_multiplier = 9
	print "* " * asterix_multiplier
	print "* " * asterix_multiplier
	print " "* space_multiplier, "G A M E   O V E R"
	print "* " * asterix_multiplier
	print "* " * asterix_multiplier
	exit()


def start_again(yes_or_no):
	"""
	intended behaviour: asks user if they want to start again and outputs a corresponding response
	inputs: entered by user
	outputs: starts game again or exits depending on the user's choice
	"""
	if yes_or_no == "yes" or yes_or_no == "y":
		# level_1(input_difficulty)
		start_game()
	else: 
		game_over()
		exit()

def try_level_again():
	"""
	intended behaviour: asks user if he wants to try level again if the user provides a wrong answer. 
	input: yes or no, provided by the user. 
	output: replay level or gameover depending on user choice. 
	"""
	try_level_again = raw_input("\nYour last answer wasn't correct. \nWould you like to retry this level? Enter: 'yes' or 'no': " ).lower()
	if try_level_again == "yes" or try_level_again == "y":
		print " " # inserting a blank line for clarity
		level_functionality(_questions_, blanks_list, input_difficulty)### have to change stuff here due to input difficulty
	else: 
		game_over()


# def answer_checker(user_answers, answer_list):
# 	"""
# 	intended behaviour: checks if the answers that the user has provided match the correct answer
# 	inputs: user's answer and a list of correct answers
# 	outputs: game over if both inputs don't match, returns True if inputs match
# 	"""
# 	end_multiplier = 4
# 	if user_answers == answer_list: 
# 		print "\n", "* " * end_multiplier, "C O N G R A T U L A T I O N S - YOU WIN", " *" * end_multiplier
# 		return True
# 	else: 
# 		try_level_again = raw_input("\nYour answers weren't correct. \nWould you like to retry this level? Enter: 'yes' or 'no': " ).lower()
# 		if try_level_again == "yes" or try_level_again == "y":
# 			level_functionality(_questions_, blanks_list, input_difficulty)
# 		else: 
# 			game_over()

def game_play_logic(question, replaced, list_of_user_answers, index_counter, answer_counter, level_type):
	"""
	intended behaviour: game play logic. looks at user response and spits out appropriate output.
	inputs: question, replaced, list_of_user_answers, index_counter, answer_counter, level_type
	outputs: outputs correctly filled in blank if user answer is correct, otherwise asks user if they'd like to try again. 
	"""
	for element in question: 
		replacement = blanks_in_question(element, blanks_list)
		if replacement != None: 
			user_input = raw_input("\nWhat should go in blank " + replacement + " ")
			list_of_user_answers.append(user_input)
			element = element.replace(replacement, user_input)
			replaced.append(element)
			if user_input == _questions_[level_type]['answer'][answer_counter]:
				print "\n" + " ".join(replaced) + " " + " ".join(question[index_counter+1:]) + "\n"
				answer_counter += 1 
			else: 
				print "\nWRONG ANSWER!!!!!!!!!!!", try_level_again()
				break
		else: 
			replaced.append(element)
		index_counter += 1 
	return game_over()


def level_functionality(question, blanks_list, level_type):
	"""
	intended behaviour: takes in question, list of pre-defined blanks, and a number corresponding to a level (minus 1)
	inputs: three inputs as listed above
	outputs: meat of the fill in the blanks game / correct response if user enters correct response / game over otherwise. 
	"""
	print _questions_[level_type]['prompt']
	replaced = []
	list_of_user_answers = []
	question = _questions_[level_type]['prompt'].split()
	index_counter = 0 
	answer_counter = 0
	game_play_logic(question, replaced, list_of_user_answers, index_counter, answer_counter, level_type)
	replaced = " ".join(replaced)
	return game_over()
	# return answer_checker(_questions_[level_type]['answer'], list_of_user_answers)


def start_game(): 
	"""
	intended behaviour: starts the game and asks user for what level they want to start at
	inputs: user's choice in level of difficulty
	outputs: takes user to corresponding level of difficulty in the game. 
	"""
	print """The objective of the game is to fill in the blanks correctly. \nThis game has three levels of difficulty. Please enter: \n"easy" for Easy \n"medium" for Medium \n"hard" for Hard"""
	global input_difficulty
	input_difficulty = raw_input("Choose level of difficulty: " ).lower()
	if input_difficulty == "easy": 
		print_fancy_heading("Level 1: Easy")
		level_functionality(_questions_, blanks_list, input_difficulty)
	elif input_difficulty == "medium": 
		print_fancy_heading("Level 2: Medium")
		level_functionality(_questions_, blanks_list, input_difficulty)
	elif input_difficulty == "hard": 
		print_fancy_heading("Level 3: Hard")
		level_functionality(_questions_, blanks_list, input_difficulty)
	else: 
		yes_or_no = raw_input("I'm sorry, but you didn't follow the instructions :'( \nWould you like to start again? Enter: 'yes' or 'no': " ).lower()
		start_again(yes_or_no)

# prints fancy heading: welcome to the game
print_fancy_heading("WELCOME TO THE GAME")
# starts gameplay: 
start_game()

