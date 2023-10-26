import os
from dotenv import load_dotenv
import requests
from requests import Response
import json


def element_to_data(element: str):
    load_dotenv()
    data_dict = {
        "post": os.getenv("POST_INFO"),
        "comment": os.getenv("COMMENT_INFO"),
        "album": os.getenv("ALBUM_INFO"),
        "photo": os.getenv("PHOTO_INFO"),
        "todo": os.getenv("TODO_INFO"),
        "user": os.getenv("USER_INFO")
    }
    return json.loads(data_dict[element])


def get_data_len(name: str):
    load_dotenv()
    len_dict = {
        "posts": os.getenv("POSTS_LEN"),
        "comments": os.getenv("COMMENTS_LEN"),
        "albums": os.getenv("ALBUMS_LEN"),
        "photos": os.getenv("PHOTOS_LEN"),
        "todos": os.getenv("TODOS_LEN"),
        "users": os.getenv("USERS_LEN")
    }
    return len_dict[name]

def get_data_to_post(element: str):
    load_dotenv()
    data_dict = {
        "post": os.getenv("POST2POST"),
        "comment": os.getenv("COMMENT2POST"),
        "album": os.getenv("ALBUM2POST"),
        "photo": os.getenv("PHOTO2POST"),
        "todo": os.getenv("TO_DO2POST"),
        "user": os.getenv("USER2POST")
    }
    return json.loads(data_dict[element])

class ApiFunctions:
    def __init__(self):
        load_dotenv()
        self.api_url = os.getenv("API_URL")

    def get_request(self, endpoint):
        return requests.get(self.api_url + endpoint)

    def check_status_code(self, response: Response, status_code):
        return True if response.status_code == int(status_code) else False

    def check_get(self, response: Response, element: str):
        info_obtained = response.json()
        if element == "empty":
            info_to_check = {}
        else:
            info_to_check = element_to_data(element)

        if info_to_check == info_obtained:
            return True
        else:
            return False

    def check_getall_len(self, response: Response, name: str):
        data = response.json()
        len_expected = get_data_len(name)
        return True if len(data) == int(len_expected) else False

    def post_request(self, endpoint: str, element: str):
        data = get_data_to_post(element)
        return requests.post(self.api_url + endpoint, json=data)

    def check_post_returned(self, element, response: Response):
        data = response.json()
        info_check = {}
        if not data == info_check:
            return True
        else:
            return False
