import requests
import pprint

endpoint = 'http://localhost:8000/api/'

get_response = requests.get(endpoint)

pprint.pprint(get_response.json())


