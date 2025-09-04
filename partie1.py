import requests

def get_requests(url) :

    url = requests.get(url)
    print(url.status_code)
    print(url.json())

#def get_countries_info(country_code, info) :


get_requests(input("Entrer l'URL du site : "))