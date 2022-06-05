import requests
import pprint

endpoint = 'http://localhost:8000/api/create/'

data = {
    'imie': 'Jakub',
    'nazwisko': 'Granieczny',
    'indeks': 256478,
    'pesel': '00247256487',
}

get_response = requests.post(endpoint, json=data)

pprint.pprint(get_response.json())

