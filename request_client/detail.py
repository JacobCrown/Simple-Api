import requests
import pprint

endpoint = 'http://jacobcrown.pythonanywhere.com/api/1'

get_response = requests.get(endpoint)

pprint.pprint(get_response.json())
