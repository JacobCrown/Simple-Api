import requests
import pprint

endpoint = 'http://localhost:8000/api/2/update/'

data = {
    'imie': 'Maciejeczek',
    'nazwisko': 'Kowalczyczek',
    'indeks': '258274',
    'pesel': '62032701132',
}

get_response = requests.put(endpoint, json=data)
# print(get_response.text)
# pprint.pprint(get_response.status_code)

pprint.pprint(get_response.json())
