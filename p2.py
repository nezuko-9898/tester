import requests


data = {

    'title' : 'Hello',
    'body' :  'Hello Morning star',
    'userId' : 1
}

response = requests.get('https://jsonplaceholder.typicode.com/posts' ,  data)
print(response.status_code)
print(response.url)
print(response.json())



