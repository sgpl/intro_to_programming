#decode secret message
import os # importing os to use rename and listdir and cwd functions

def rename_files():
	file_list = os.listdir(r"/Users/sharad/UDACITY/IntroCS/prank") #storing filenames in a list
	# print file_list 
	saved_path = os.getcwd() # storing cwd in a variable called saved_path 
	print"Current working directory is: " + saved_path 
	os.chdir(r"/Users/sharad/UDACITY/IntroCS/prank") #chanding directory to the place where the files are 
	for file_name in file_list:
		print "Old Name: " + file_name + "          New Name: " + file_name.translate(None, "0123456789")
		os.rename(file_name, file_name.translate(None, "0123456789")) # looping through the list to rename the files
	os.chdir(saved_path) # switching back path 

rename_files()