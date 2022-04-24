import requests
import pprint

student_id = input('What is the product id you want to use\n')

try: 
    student_id = int(student_id)
except Exception:
    print(f'{student_id} not a valid id')

if student_id:

    endpoint = f'http://localhost:8000/api/{student_id}/delete/'

    get_response = requests.delete(endpoint)
    # print(get_response.text)
    # pprint.pprint(get_response.status_code)

    pprint.pprint(get_response.status_code)

