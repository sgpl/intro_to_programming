import fresh_tomatoes
import media 

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life", 
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						"https://youtu.be/KYz2wyBy3kc", 
						"81 Minutes", 
						"1995", 
						"John Lasseter")

avatar = media.Movie("Avatar", 
					"A story about aliens", 
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
					"https://youtu.be/cRdxXPV9GNQ",
					"161 Minutes", 
					"2009", 
					"James Cameron")


the_godfather = media.Movie("The Godfather", 
							"A story about hope, and cool things", 
							"https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg", 
							"https://youtu.be/sY1S34973zA", 
							"177 Minutes", 
							"1972", 
							"Francis F. Coppola")


inception = media.Movie("Inception", 
							"The film tells the story of an alternate reality where people can invade your dreams and plant ideas.", 
							"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", 
							"https://youtu.be/66TuSJo4dZM", 
							"148 Minutes", 
							"2010", 
							"Christopher Nolan")


wonder_woman = media.Movie("Wonder Woman", 
							"A story about wonder woman and her contribution during WWII", 
							"http://www.dccomics.com/sites/default/files/imce/2016/07-JUL/WWPosterRdcd_579260f4b9aba4.81209460.jpg", 
							"https://youtu.be/VSB4wGIdDwo", 
							"141 Minutes", 
							"2017", 
							"Patty Jenkins")

casino_royale = media.Movie("Casino Royale", 
							"Casino Royale is set at the beginning of Bond's career as Agent 007, just as he is earning his licence to kill.", 
							"https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg", 
							"https://youtu.be/36mnx8dBbGE", 
							"144 Minutes", 
							"2006", 
							"Martin Campbell")

dark_knight = media.Movie ("The Dark Knight", 
					"Dark, complex and unforgettable, The Dark Knight succeeds not just as an entertaining comic book film, but as a richly thrilling crime saga.", 
					"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", 
					"https://youtu.be/EXeTwQWrcwY", 
					"152 Minutes", 
					"2008", 
					"Christopher Nolan")

angry_men = media.Movie ("12 Angry Men", 
					"A jury argues a case in a stuffy room on a hot summer's day. Eleven say 'guilty!'' But one holdout (Jack Lemmon) is convinced of the defendant's innocence and stubbornly argues reasonable doubt.", 
					"https://upload.wikimedia.org/wikipedia/en/4/44/12_Angry_Men_1997_film_poster.jpg", 
					"https://youtu.be/A7CBKT0PWFA", 
					"117 Minutes", 
					"1997", 
					"William Friedkin")


slist = media.Movie ("Schindler's List", 
					"Schindler's List blends the abject horror of the Holocaust with Steven Spielberg's signature tender humanism to create the director's dramatic masterpiece", 
					"https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg", 
					"https://youtu.be/JdRGC-w9syA", 
					"196 Minutes", 
					"1993", 
					"Steven Spielberg")

ant_man = media.Movie ("Ant Man", 
					"The story about a man who becomes an ant, and harnesses an ant's super powers to save the world", 
					"https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg", 
					"https://youtu.be/pWdKf3MneyI", 
					"117 Minutes", 
					"2015", 
					"Peyton Reed")


forrestgump = media.Movie ("Forrest Gump", 
					"A movie about hope, determination and beliefs.", 
					"https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg", 
					"https://youtu.be/uPIEn0M8su0", 
					"142 Minutes", 
					"1994", 
					"Robert Zemeckis")

matrix = media.Movie ("The Matrix", 
					"A movie about an interesting alternate reality!", 
					"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", 
					"https://youtu.be/m8e-FF8MsqU", 
					"136 Minutes", 
					"1999", 
					"Wachowski Brothers")



movies = [dark_knight, the_godfather, angry_men, wonder_woman, inception, toy_story, casino_royale, ant_man, slist, avatar, matrix, forrestgump]
fresh_tomatoes.open_movies_page(movies)
