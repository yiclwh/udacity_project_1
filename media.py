import webbrowser, requests, json

class Movie():
    """ Movie()
    Build a movie instance 
    and open up web browser to play its movie trailer. It takes an ID to go to api.themoviedb.org to
    get movie title and storyline and another set of image and video urls to get poster and trailer

    Attributes: 
      title(string)
      movie_storyline(string)
      poster_image(string): url of poster image
      trailer_link(string): url of movie trailer
    """
    """ TODO
    Find API docs to auto generate correct image url and trailer url
    """

    """ 
    movie_id(int): movie ID got it from www.themoviedb.org
    poster_image(string): url of poster image
    trailer_link(string): url of movie trailer
    """
    def __init__(self, movie_id, image_url, trailor_url):
        API_KEY = "fce10e9926d00abd4f6318147db734ad"
        movie_url = "https://api.themoviedb.org/3/movie/%d?api_key=%s"%(movie_id, API_KEY)
        response = requests.get(movie_url)
        if response.ok:
            jdata = json.loads(response.content)
            self.title = jdata["title"]
            self.movie_storyline = jdata["overview"]
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailor_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)  