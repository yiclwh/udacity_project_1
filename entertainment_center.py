from media import Movie
import fresh_tomatoes

""" Summary
It creats a list of 3 movie objects and display in static webpage

"""

american_beauty = Movie(14,
                    "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",
                    "https://www.youtube.com/watch?v=3ycmmJ6rxA8&t=61s")
blade_runner_2049 = Movie(335984, 
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcTPzZknP1D3cmxl_h5_Dc2eb-3_CA-XML7lYSthbX4r_VYADgKD",
                    "https://www.youtube.com/watch?v=gCcx85zbxz4")
king_of_comedy = Movie(53168, 
                    "https://i2.wp.com/china-underground.com/wp/wp-content/uploads/2017/03/8vOAFDbi90X25eSfIL9ZFHczxG.jpg?fit=1000%2C1500&ssl=1",
                    "https://www.youtube.com/watch?v=8ugDobAFpOo")

movies=[american_beauty, blade_runner_2049, king_of_comedy]
fresh_tomatoes.open_movies_page(movies)