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
        "user": os.getenv("USER2POST"),
        "wrong_post": os.getenv("WRONG_POST"),
        "wrong_photo": os.getenv("WRONG_PHOTO"),
        "wrong_todo": os.getenv("WRONG_TODO")
    }
    return json.loads(data_dict[element])

def get_data_to_put(element: str):
    load_dotenv()
    data_dict ={
        "post": os.getenv("POST2PUT"),
        "comment": os.getenv("COMMENT2PUT"),
        "album": os.getenv("ALBUM2PUT"),
        "photo": os.getenv("PHOTO2PUT"),
        "todo": os.getenv("TODO2PUT"),
        "user": os.getenv("USER2PUT")
    }
    return json.loads(data_dict[element])

def get_data_to_patch(element: str):
    load_dotenv()
    data_dict = {
        "post": os.getenv("POST2PATCH"),
        "comment": os.getenv("COMMENT2PATCH"),
        "album": os.getenv("ALBUM2PATCH"),
        "photo": os.getenv("PHOTO2PATCH"),
        "todo": os.getenv("TODO2PATCH"),
        "user": os.getenv("USER2PATCH")
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
        if element == "empty":
            if data == info_check:
                return True
            else:
                return False

        if not data == info_check:
            return True
        else:
            return False

    def put_request(self, endpoint, element):
        data = get_data_to_put(element)
        return requests.put(self.api_url + endpoint, json=data)

    def check_updated_info(self, element, response: Response):
        data = response.json()
        if element == "empty":
            info_to_check = {}
        else:
            info_to_check = get_data_to_put(element)
        if data == info_to_check:
            return True
        else:
            return False

    def patch_request(self, endpoint, element):
        data = get_data_to_patch(element)
        return requests.patch(self.api_url + endpoint, json=data)

    def check_patch_returned(self, response, element):
        data = response.json()
        info_to_check = {}
        if element == "empty":
            if data == info_to_check:
                return True
            else:
                return False

        if not data == info_to_check:
            return True
        else:
            return False

    def delete_request(self, endpoint):
        return requests.delete(self.api_url + endpoint)


    def check_delete_return(self, response: Response):
        data = response.json()
        info_to_check = {}
        if data == info_to_check:
            return True
        else:
            return False

