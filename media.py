
class Movie():
    """ this class provide a way to store a movie related infrmation

    Attributes
    title (str):  represent the title of movie
    storyline (str): represent the story of movie
    poster_image_url (str): it's a link for poster poster_image
    trailer_youtube_url (str): it's a link for movie """
# constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
