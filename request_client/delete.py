import requests
import pprint

endpoint = 'http://jacobcrown.pythonanywhere.com/api/2/delete/'

get_response = requests.delete(endpoint)

pprint.pprint(get_response.status_code)

