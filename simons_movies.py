import media
import fresh_tomatoes
import urllib
import urllib2
import json

# For each movie get the IMDB ID for the movie to access the movie information from omdbapi.com

def find_movie(movie_name):

  query_args = { 's':movie_name }
  encoded_args = urllib.urlencode(query_args)
  movie_url = 'http://www.omdbapi.com/?' + encoded_args
  movie_data = json.load(urllib2.urlopen(movie_url))
  movie_imdb_id = movie_data['Search'][0]['imdbID']
  return movie_imdb_id

# For the selected movie get the plot, poster image and cast from omdbapi.com using the 
# previously found IMDB ID

def get_movie_details(movie_imdb_id):
  query_args = { 'i':movie_imdb_id }
  encoded_args = urllib.urlencode(query_args)
  movie_url = 'http://www.omdbapi.com/?' + encoded_args
  movie_details = json.load(urllib2.urlopen(movie_url))
  plot = movie_details['Plot']
  poster = movie_details['Poster']
  actors = movie_details['Actors']
  return [plot,poster,actors]


# Create the instances for each movie
# Find the movie details from the movie name

movie_name = "The Shawshank Redemption"
movie_id = find_movie(movie_name)
movie_details = get_movie_details(movie_id)
shawshank_redemption = media.Movie(movie_name,
                        movie_details[0],
                        movie_details[1],
                        "www.youtube.com/watch?v=6hB3S9bIaco",
                        movie_details[2])

# Movie #2

movie_name = "We're The Millers"
movie_id = find_movie(movie_name)
movie_details = get_movie_details(movie_id)

were_the_millers = media.Movie(movie_name,
                     movie_details[0],
                     movie_details[1],
                     "www.youtube.com/watch?v=0Vsy5KzsieQ",
                     movie_details[2])

# Create the array of movie instances for rendering

movies = [shawshank_redemption,were_the_millers]

fresh_tomatoes.open_movies_page(movies)