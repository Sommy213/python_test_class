import requests
url = 'https://jsonplaceholder.typicode.com/todos'
response =requests.delete(url)
print(response.json())
