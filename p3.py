import requests


url = "https://jsonplaceholder.typicode.com/posts"


respons = requests.get(url)




if respons.status_code == 200:
    posts = respons.json()
    print ('list of posts title')

    for post in posts:
         print(f" - {post ['id']}")
        

else:

    print('not found')
