import requests

data = requests.get('https://jsonplaceholder.typicode.com/')

if data.status_code == 200:
    print('Request Succesful.')
else:
    print('Request Failed.')