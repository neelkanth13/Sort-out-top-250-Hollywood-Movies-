import imdb
import requests

# create an instance of the IMDb class
ia = imdb.IMDb()

# get the top 250 rated movies on IMDb
top250 = ia.get_top250_movies()

movie_list = []
# loop through each movie and print the title if it has the "Family" genre and was released between 2000 and 2020
for movie in top250:
    rating = movie['rating']
    year   = movie['year']
    title  = movie['title']
    # Make a GET request to the OMDb API with the movie name as a parameter
    response = requests.get('http://www.omdbapi.com/', params={'t': movie['title'], 'apikey': '55615d53'})
    # Parse the response as JSON
    data = response.json()
    
    # Check if the response is valid
    if data['Response'] == 'True':
        # Extract genre
        genre = data['Genre']
        # Extract rated
        rated = data['Rated']
        # Extract director
        director = data['Director']
        # Extract actor
        actor = data['Actors']
    else:
        print('Movie not found')

    #print(f"{title:<50}  {rating:<5}  {year:<6} {rated:<10} {genre}")
    movie_list.append([title , rating, year,  rated,  genre])

movie_list.sort(key=lambda x: x[2])

for i in movie_list:
    print(i)
