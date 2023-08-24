import requests
from numpy import random

def GetImages(title):
    url = "https://imdb8.p.rapidapi.com/title/get-images"

    querystring = {"tconst":title,"limit":"1"}

    headers = {
	    "X-RapidAPI-Key": "de15a6ea5dmshde27d79a7d350bfp1611e4jsn8766f00c2bf3",
	    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    return response.json()


def PopularMoviesTitles():
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

    querystring = {"homeCountry":"US","purchaseCountry":"US","currentCountry":"US"}

    headers = {
	    "X-RapidAPI-Key": "de15a6ea5dmshde27d79a7d350bfp1611e4jsn8766f00c2bf3",
	    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    all_titles = response.json()
    array = random.randint(len(all_titles) , size=4)
    titles = []
 
    for x in array:
        s = all_titles[x]
        titles.append(s.split('/')[2])

    return titles


def getDetails(title):

    url = "https://imdb8.p.rapidapi.com/title/get-overview-details"

    querystring = {"tconst":title,"currentCountry":"US"}

    headers = {
	    "X-RapidAPI-Key": "de15a6ea5dmshde27d79a7d350bfp1611e4jsn8766f00c2bf3",
	    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    
    return response.json()

def findDetails(title):
    import requests

    url = "https://imdb8.p.rapidapi.com/title/find"

    querystring = {"q":title}

    headers = {
	    "X-RapidAPI-Key": "de15a6ea5dmshde27d79a7d350bfp1611e4jsn8766f00c2bf3",
	    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    out = response.json()['results'][0]['id'].split('/')[2]
    
    return out