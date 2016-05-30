import webbrowser

class Movie():
    
	
	# a class to store the movie related information 
	
    def __init__(self,title,description,cover_art,trailer_url):
        self.title = title
        self.description=description
        self.poster_image_url = cover_art
        self.trailer_youtube_url = trailer_url

	# method for opening the vieo URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)