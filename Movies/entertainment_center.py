import fresh_tomatoes
import media

url_youtube = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
url_photo = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
story_movie = "Woody (Tom Hanks), a good-hearted cowboy d"
toy_story = media.Movie("Toy Story",story_movie,url_photo,url_youtube)


Ratatouille = media.Movie("Ratatouille","Remy (Patton Oswalt), a resident of Paris, appreciates good food and has quite a sophisticated palate."
                          ,"https://vignette3.wikia.nocookie.net/disney/images/3/30/Ratatouille-_2007.jpg/revision/latest?cb=20130420023426"
                          ,"https://www.youtube.com/watch?v=ALUmKa_mpik")


Up = media.Movie("UP","Carl Fredricksen (Ed Asner), a 78-year-old balloon salesman, is about to fulfill a lifelong dream."
                 ,"http://www.impawards.com/2009/posters/up_ver9.jpg"
                 ,"https://www.youtube.com/watch?v=pkqzFUhGPJg")
#print (toy_story)
#toy_story.show_trailer()

movies = [toy_story,Ratatouille,Up]
fresh_tomatoes.open_movies_page(movies)
