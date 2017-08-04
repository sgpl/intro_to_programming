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


question_easy = """[1]______ lists the contents of a directory. 
[2]______ is the command that can be used to change your working 
directory. [3]______ prints your current working directory and 
[4]______ is the command used to create a new directory!"""
# ls, cd, pwd, mkdir
question_medium = """[1]______ is the command used to create a new 
directory, [2]______ is a command used to permanently remove a file. 
[3]______ permanently removes an empty directory and [4]______ is 
a command that creates a new file with a specified extension or file type."""
# mkdir, rm, rmdir, touch
question_hard = """rm -ri permanently removes a [1]______ and it's 
contents with confirmation. [2]______ is a command used to make a 
new directory. [3]______ permanently removes an empty directory and 
[4]______ permanently removes a file."""
# directory, mkdir, rmdir, rm
question_superhard = """[1]______ is a general-purpose interpreted, interactive, 
object-oriented, and high-level [2]______ language. A [3]______ is 
created with the def keyword. Using [4]______(some_object) returns 
the number of top-level items contained in the object being queried."""
# python, programming, function, len

list_of_questions_and_answers = [[question_easy, ["ls", "cd", "pwd", "mkdir"]], [question_medium, ["mkdir", "rm", "rmdir", "touch"]], [question_hard, ["directory", "mkdir", "rmdir", "rm"]], [question_superhard, ["python", "programming", "function", "len"]]]

blanks_list  = ["[1]______", "[2]______", "[3]______", "[4]______"]


def blanks_in_question(blank, list_of_blanks):
	"""
	intended behaviour: outputs a blank (used when asking user for input) 
	inputs: takes in a word, and a list of blanks
	outputs: none if the condition is not met. otherwise it returns a blank (from list of blank) corresponding to word
	"""
    for xx in list_of_blanks:
        if xx in blank:
            return xx
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
	print "* " * 20
	print "* " * 20
	print " "* 9, "G A M E   O V E R"
	print "* " * 20
	print "* " * 20
	exit()



def try_again(yes_or_no):
	"""
	intended behaviour: asks user if they want to try again and outputs a corresponding response
	inputs: entered by user
	outputs: starts game again or exits depending on the user's choice
	"""
	if yes_or_no == "yes" or yes_or_no == "Yes" or yes_or_no == "y":
		# level_1(input_difficulty)
		start_game()
	else: 
		game_over()
		exit()


def answer_checker(user_answers, answer_list):
	"""
	intended behaviour: checks if the answers that the user has provided match the correct answer
	inputs: user's answer and a list of correct answers
	outputs: game over if both inputs don't match, returns True if inputs match
	"""
	if user_answers == answer_list: 
		print "\n", "* " * 4, "C O N G R A T U L A T I O N S", " *" * 4
		return True
	else: 
		try_level_again = raw_input("\nYour answers weren't correct. \nWould you like to retry this level? Enter: 'yes' or 'no': " )
		if try_level_again == "yes" or try_level_again == "Yes" or try_level_again == "y":
			print " " # inserting a blank line for clarity
			level_functionality(list_of_questions_and_answers, blanks_list, int(input_difficulty)-1)
		else: 
			game_over()


def level_functionality(question, blanks_list, levelx):
	"""
	intended behaviour: takes in question, list of pre-defined blanks, and a number corresponding to a level (minus 1)
	inputs: three inputs as listed above
	outputs: meat of the fill in the blanks game / correct response if user enters correct response / game over otherwise. 
	"""
	print list_of_questions_and_answers[levelx][0]
	replaced = []
	list_of_user_answers = []
	question = list_of_questions_and_answers[levelx][0].split()
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
	answer_checker(list_of_questions_and_answers[levelx][1], list_of_user_answers)
	print "ANSWER: " + replaced

def start_game(): 
	"""
	intended behaviour: starts the game and asks user for what level they want to start at
	inputs: user's choice in level of difficulty
	outputs: takes user to corresponding level of difficulty in the game. 
	"""
	print """The objective of the game is to fill in the blanks correctly. \nWhen entering your answers, please use all lowercase responses. \nThis game has three levels of difficulty. Please enter: \n"1" for Easy \n"2" for Medium \n"3" for Hard"""
	global input_difficulty
	input_difficulty = raw_input("Choose level of difficulty: " )
	if input_difficulty == str(1): 
		print_fancy_heading("Level 1: Easy")
		level_functionality(list_of_questions_and_answers, blanks_list, 0)
	elif input_difficulty == str(2): 
		print_fancy_heading("Level 2: Medium")
		level_functionality(list_of_questions_and_answers, blanks_list, 1)
	elif input_difficulty == str(3): 
		print_fancy_heading("Level 3: Hard")
		level_functionality(list_of_questions_and_answers, blanks_list, 2)
	else: 
		yes_or_no = raw_input("I'm sorry, but you didn't follow the instructions :'( \nWould you like to start again? Enter: 'yes' or 'no': " )
		try_again(yes_or_no)

# prints fancy heading: welcome to the game
print_fancy_heading("WELCOME TO THE GAME")
# starts gameplay: 
start_game()

