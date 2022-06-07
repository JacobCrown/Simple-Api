import requests
import pprint

endpoint = 'http://jacobcrown.pythonanywhere.com/api/create/'

data = {
    'imie': 'Maciejek',
    'nazwisko': 'Wilhelm',
    'indeks': 323411,
    'pesel': '08237226417',
}

get_response = requests.post(endpoint, json=data)

pprint.pprint(get_response.json())

