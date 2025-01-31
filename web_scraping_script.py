import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
