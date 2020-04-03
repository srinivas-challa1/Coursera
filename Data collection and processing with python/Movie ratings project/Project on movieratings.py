
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")
import requests
import json


def get_movies_from_tastedive(movie, key="362396-Srinivas-YJWHR8FT"):
    baseurl = "https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"] = movie
    params_d["k"] = key
    params_d["type"] = "movies"
    params_d["limit"] = "5"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    # print(resp.text)
    resp_dict = resp.json()
    return resp_dict


'''
def extract_movie_titles(movie):
    movieTitles = []
    resp_dict = get_movies_from_tastedive(movie)
    for movie in resp_dict['Similar']['Results']:
        movieTitles.append(movie['Name'])
    return(movieTitles)
'''


def extract_movie_titles(MovieDict):
    movieTitles = []
    resp_dict = MovieDict['Similar']['Results']
    for movie in resp_dict:
        movieTitles.append(movie['Name'])
    return(movieTitles)


'''
print(extract_movie_titles(get_movies_from_tastedive("Bridesmaids")))
'''
# print(extract_movie_titles("Bridesmaids"))


def get_related_titles(Movietitles):
    relatedMovies = []
    for title in Movietitles:
        Movielist = extract_movie_titles(get_movies_from_tastedive(title))
        # relatedMovies = [title for title in Movielist if title not in relatedMovies]
        for movie in Movielist:
            if movie not in relatedMovies:
                relatedMovies.append(movie)
    return(relatedMovies)
# print(get_related_titles(["Black Panther", "Captain Marvel"]))


def get_movie_data(MovieName):
    baseurl = "http://www.omdbapi.com/"
    paramDict = {'t': MovieName, 'r': 'json', 'apikey': '4e843aa5'}
    omdbresp = requests.get(baseurl, params=paramDict)
    omdbDict = json.loads(omdbresp.text)
    return(omdbDict)


# print(get_movie_data("Venom"))
#print(get_movie_data("Baby Mama"))

def get_movie_rating(OMDBdict):
    rating = None
    if len(OMDBdict['Ratings']) > 1:
        if OMDBdict['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            rating = int(OMDBdict['Ratings'][1]['Value'][:2])
           # rotten_rating = int(rotten_rating)
        else:
            rating = 0

    return(rating)


#print(get_movie_rating(get_movie_data("Deadpool 2")))
def get_sorted_recommendations(listMovieTitle):
    listMovie = get_related_titles(listMovieTitle)
    listMovie = sorted(listMovie, key=lambda movieName: (
        get_movie_rating(get_movie_data(movieName)), movieName), reverse=True)

    return listMovie


print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
