import requests
import pprint

endpoint = 'http://localhost:8000/api/create/'

data = {
    'imie': 'Maciej',
    'nazwisko': 'Kowalczyk',
    'indeks': '257894',
    'pesel': '66042701234',
}

get_response = requests.post(endpoint, json=data)

pprint.pprint(get_response.json())

