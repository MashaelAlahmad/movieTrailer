import media
import fresh_tomatoes

#object of movie with some info about it
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://imgc.allpostersimages.com/img/print/u-g-F7Z0IL0.jpg?w=550&h=550&p=0",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

the_hunt = media.Movie("The hunt",
                      " A story of a man live in deimark",
                      "https://i0.wp.com/media.fushaar.com/media/2014/07/11170774_ori.jpg?resize=329%2C495&ssl=1",
                      "https://www.youtube.com/watch?v=rTIQmt2s_24")
# this is list of movies
movies = [toy_story, the_hunt]
fresh_tomatoes.open_movies_page(movies)
