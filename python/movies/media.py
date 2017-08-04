import webbrowser

class Movie():
	"""This class provides a way for us to store information about movies!"""

	# this is the constructor method for the movie class. it is called when an instance of a movie is created. 
	# it contains the inputs that the instance of the movie needs to be created with such as: 
	# the title, storyline, duration, poster, trailer link, year, and director. 
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, duration, year, director): 
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.duration = duration
		self.year = year
		self.director = director

	# this function is called to display a trailer for a movie. it takes in self / itself as an argument and 
	# outputs a tab in the browser where it opens the youtube url and plays it. 
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	# this function opens a poster for the movie in a webbrowser. 
	def show_poster(self):
		webbrowser.open(self.poster_image_url)

	# this function displays the name of the director. 
	def show_director(self):
		return(self.director)

	# this function displays the runtime of the movie. 
	def show_runtime(self):
		return(self.duration)
		