# IPND Stage 2 Final Project

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

###### REQUIREMENTS
# game has 3 or more levels
# each level has 4 or more blanks

# when game begins, user should select difficulty level
# game begins at that level of difficulty

# when player guesses correctly, 
#  the correct response filled in is displayed

# when player guesses incorrectly, they are prompted to try again

# use functions to automate tasks 

# functions aren't longer than 18 lines 

# functions are producing appropriate outputs

# use string for text, lists for ordered data and nested lists as appropriate

# use loops 

# each function includes a comment that explains intended behaviour
# and inputs and outputs

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
# questions = [q_1_1, q_1_2, q_1_3, q_1_4]

q_and_a = [[q_1_1, ["ls", "cd", "pwd", "mkdir"]], [q_1_2, ["mkdir", "rm", "rmdir", "touch"]], [q_1_3, ["directory", "mkdir", "rmdir", "rm"]], [q_1_4, ["python", "programming", "function", "len"]]]


# The answer for ___1___ is 'function'. Can you figure out the others?
blanks_list  = ["[1]______", "[2]______", "[3]______", "[4]______"]

def blanks_in_question(blank, list_of_blanks):
    for xx in list_of_blanks:
        if xx in blank:
            return xx
    return None


# A function to make the headings fancy
def print_fancy_heading(heading_text):
	heading_text = "| " + heading_text + " |"
	border = len(heading_text)
	print " " 
	print "-" * border
	print heading_text
	print "-" * border
	print " "

# a function that is called when the game is over
def game_over():
	print "* " * 20
	print "* " * 20
	print " "* 9, "G A M E   O V E R"
	print "* " * 20
	print "* " * 20
	exit()

# a function asking the user to try again
def try_again(yes_or_no):
	if yes_or_no == "yes" or yes_or_no == "Yes" or yes_or_no == "y":
		# level_1(input_difficulty)
		start_game()
	else: 
		game_over()
		exit()

def answer_checker(user_answers, answer_list):
	if user_answers == answer_list: 
		return True
	else: 
		game_over()

def level_1(question, blanks_list):
	print q_and_a[0][0]
	replaced = []
	list_of_user_answers = []
	question = q_and_a[0][0].split()
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
	answer_checker(q_and_a[0][1], list_of_user_answers)
	print replaced

def level_2(question, blanks_list):
	print q_and_a[1][0]
	replaced = []
	list_of_user_answers = []
	question = q_and_a[1][0].split()
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
	answer_checker(q_and_a[1][1], list_of_user_answers)
	print replaced

def level_3(question, blanks_list):
	print q_and_a[2][0]
	replaced = []
	list_of_user_answers = []
	question = q_and_a[2][0].split()
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
	answer_checker(q_and_a[2][1], list_of_user_answers)
	print replaced

def start_game(): 
	print_fancy_heading("WELCOME TO THE GAME")
	print """The objective of the game is to fill in the blanks correctly. \nThis game has three levels of difficulty. Please enter: \n"1" for Easy \n"2" for Medium \n"3" for Hard"""
	input_difficulty = raw_input("Choose level of difficulty: " )
	if input_difficulty == str(1): 
		print_fancy_heading("Level 1: Easy")
		level_1(q_and_a, blanks_list)
	elif input_difficulty == str(2): 
		print_fancy_heading("Level 2: Medium")
		level_2(q_and_a, blanks_list)
	elif input_difficulty == str(3): 
		print_fancy_heading("Level 3: Hard")
		level_3(q_and_a, blanks_list)
	else: 
		yes_or_no = raw_input("I'm sorry, but you didn't follow the instructions :'( \nWould you like to start again? Enter: 'yes' or 'no': " )
		try_again(yes_or_no)

start_game()

