import webbrowser
class Movie():
  """ this class provide a way to store a movie related infrmation"""
  VALID_RATING = ["G", "PG", "PG-13", "R"]
  #constructor
  def __init__(self, movie_title, movie_storyline, poster_image,
               trailer_youtube):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

#fct to play movie trailer
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
