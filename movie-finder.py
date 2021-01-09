# Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części filmu zadanego w wyszukiwaniu 
# (np. Rambo, Scary Movie, Shrek). Można przyjąć założenie, że wszystkie filmy “z serii” muszą zawierać 
# szukany ciąg - czasem zdarzają się błędne wyniki wyszukiwania z baz, można je spróbować odfiltrować. 
# Wyświetl dla każdego podstawowe informacje np. rok, długość, ocena, spis aktorów (pierwszych 5 z listy).
# Przykładowe API do wykorzystania: 
# https://rapidapi.com/apidojo/api/imdb8/endpoints - do wyszukania filmów z daną nazwą 
# (do odfiltrowania można użyć warunku, że dany rekord posiada nazwę i rok wydania)
# https://rapidapi.com/.../imdb-internet-movie-database... - pobranie szczegółów o danym filmie


import requests
import json

def search_movie(search_title):
    movie_ids = []
    url = "https://imdb8.p.rapidapi.com/title/find"
    querystring = {"q": search_title}
    headers = {
        'x-rapidapi-key': "6a07f1ac4fmsh8c60eb9fac2e604p1d7bf9jsn3ff03131ee18",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }   
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    movie_list = response.json()['d']

    for item in movie_list:
        movie_ids.append(item["id"])
    return movie_ids

def movie_information(movie_ids):
    
    headers = {
        'x-rapidapi-key': "6a07f1ac4fmsh8c60eb9fac2e604p1d7bf9jsn3ff03131ee18",
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

    for movie_id in movie_ids:
        url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{movie_id}"
        response = requests.request("GET", url, headers=headers)
        movie_details = response.json()

        if len(movie_details["title"]) > 0 and len(movie_details["year"]) > 0:
            print(f"Tytuł: {movie_details['title']}, Rok produkcji: {movie_details['year']}, Ocena: {movie_details['rating']}")
            print()
            print("*** Występują ***")
            
            for i in range(5):
                try:
                    print(movie_details['cast'][i]['actor'], '-', movie_details['cast'][i]['character'])
                except IndexError:
                    break
            print('-'*5)

movie_information(search_movie(input("Podaj tytuł filmu: ")))