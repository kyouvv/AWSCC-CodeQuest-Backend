import requests


base_url = 'https://jsonplaceholder.typicode.com/posts'
headers = {
    'User-Agent' : 'MyApp/1.0'
}
post_data = {
    'title': 'test',
    'body' : 'testing'
}
data = requests.get(base_url, headers=headers)

print('GET STATUS CODE:', data.status_code)
json_data = data.json()

for key, value in data.headers.items():
    print(f"{key}: {value}")

post_req = requests.post(base_url, json=post_data)

print('POST STATUS CODE: ', post_req.status_code)