import media
import fresh_tomatoes

# object of movie with some info about it
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        '''https://imgc.allpostersimages.com/img/print/u-g-F7Z0IL0.
jpg?w=550&h=550&p=0''',
                        "https://youtu.be/azyK_k52R1w")

the_hunt = media.Movie("The hunt",
                       " A story of a man live in deimark",
                       '''https://i0.wp.com/media.fushaar.com/media/2014/07/11170774_ori.
jpg?resize=329%2C495&ssl=1''',
                       "https://www.youtube.com/watch?v=rTIQmt2s_24")

Holmes_Watson = media.Movie("Holmes & Watson",
                            ''' A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring
                            Sherlock Holmes and Doctor Watson.''',
                            '''https://m.media-amazon.com/images/M/MV5BZTNjMjAwNjQtYjE4MC00OGNlLTgzN
DctNTE2NTBjMjRlMDgwXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_UY268_CR4,0,1
82,268_AL_.jpg''',
                            "https://youtu.be/brjkpRBpFnc")

A_Beautiful_Mind = media.Movie("A Beautiful Mind",
                               '''After John Nash, a brilliant but asocial mathematician,
                                  accepts secret work in cryptography, his life
                                  takes a turn for the nightmarish.''',
                               '''https://m.media-amazon.com/images/M/MV5BMzcwYWFkYzktZjAzNC00OGY1L
WI4YTgtNzc5MzVjMDVmNjY0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX18
2_CR0,0,182,268_AL_.jpg''',
                               "https://youtu.be/WFJgUm7iOKw")

# this is list of movies
movies = [toy_story, the_hunt, Holmes_Watson, A_Beautiful_Mind]
fresh_tomatoes.open_movies_page(movies)
