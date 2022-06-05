import requests
import pprint

endpoint = 'http://localhost:8000/api/3/update/'

data = {
    'imie': 'Antoni',
    'nazwisko': 'Kowalewski',
    'indeks': 223289,
    'pesel': 62071068245,
}

get_response = requests.put(endpoint, json=data)

pprint.pprint(get_response.json())
