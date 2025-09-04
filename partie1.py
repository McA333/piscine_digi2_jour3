import requests

def get_requests(url) :

    url = requests.get(url)
    print(url.status_code)
    #print(url.text)

#get_requests(input("Entrer l'URL du site : "))