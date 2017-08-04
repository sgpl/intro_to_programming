import urllib

def read_text():
	quotes = open("/Users/sharad/UDACITY/IntroCS/movie_quotes/movie_quotes.txt")
	contents_of_file = quotes.read()
	# print contents_of_file
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text_to_check)
	output = connection.read()
	# print output
	connection.close()
	if "true" in output: 
		print "PROFANITY ALERT!!!"
	elif "false" in output: 
		print "This document has no curse words!"
	else: 
		print "Could not read the file properly!"

read_text()
