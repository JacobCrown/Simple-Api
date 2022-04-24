import requests
import pprint

endpoint = 'http://localhost:8000/api/5'

get_response = requests.get(endpoint)
# print(get_response.text)
# pprint.pprint(get_response.status_code)

pprint.pprint(get_response.json())
