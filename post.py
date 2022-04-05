import requests


class Post:
    def __init__(self):
        self.API_BLOG = 'https://api.npoint.io/c790b4d5cab58020d391'

    def get_blog(self):
        response = requests.get(self.API_BLOG)
        data = response.json()
        return data
