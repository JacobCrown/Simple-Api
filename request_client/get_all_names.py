import requests
import pprint

endpoint = 'http://jacobcrown.pythonanywhere.com/api/look-by-name/Jakub/'

get_response = requests.get(endpoint)

pprint.pprint(get_response.json())
