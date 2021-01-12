# 2 of 10 application - Winter Holidays Challenge 2021

# Napisz program, który po uruchomieniu wyświetla w czytelnej formie aktualną datę, godzinę, dzień tygodnia 
# i pogodę/temperaturę/ciśnienie w zadanym mieście 
# (wykorzystaj np. https://rapidapi.com/commu.../api/open-weather-map/endpoints - 
# pamiętaj o poprawnym przeliczeniu jednostek np. temperatura z kelwinów na stopnie) 
# oraz losowy cytat (np. https://type.fit/api/quotes ). Wykorzystaj requests i datetime.

# Propozycja rozszerzenia: Wyświetl również bieżący czas dla miast w różnych strefach czasowych 
# (np. Pekin, Sydney, Waszyngton, Londyn) - wykorzystaj np. pytz: https://pypi.org/project/pytz/ 
# oraz wyświetl listę osób obchodzących imieniny (poszukaj otwartej bazy danych lub wykorzystaj prosty 
# web scrapping np. z wykorzystaniem: https://imienniczek.pl/widget/js ).

import requests
import datetime
import random

city = input("Please select city: ")

def weather():

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"","lat":"0","lon":"0","id":"2172797","lang":"null","units":"metric","mode":"xml, html"}
    querystring["q"] = city

    headers = {
        'x-rapidapi-key': "6a07f1ac4fmsh8c60eb9fac2e604p1d7bf9jsn3ff03131ee18",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    if response ['cod'] == 200:
        print(f"""
            Weather: {response['weather'][0]['main']}
            Detailed weather: {response['weather'][0]['description']}
            Temperature: {response['main']['temp']} C
            Pressure: {response['main']['pressure']} hPa 
            Humidity: {response['main']['humidity']}% """)
    else:
        print("Oops something went wrong! Try again")

def page_from_callendar():
    today = datetime.datetime.today()
    print(f"""
            Today is {today.day} {today.strftime('%B')} {today.year} year
            Day of the week: {today.strftime('%A')}
            The current time: {today.strftime('%H')}:{today.strftime('%M')}""")

def quote():
    url_quote = "https://type.fit/api/quotes"
    q_response = random.choice(requests.request("GET", url_quote).json())
    print(f"""
            Special quote today: {q_response['text']}
            Author: {q_response['author']}""")

page_from_callendar()
weather()
quote()
