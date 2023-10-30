import os
from dotenv import load_dotenv
import requests
from requests import Response
from utilities.testing_data import TestingData as td


def element_to_data(element: str):
    data_dict = {
        "post": td.POST_INFO,
        "comment": td.COMMENT_INFO,
        "album": td.ALBUM_INFO,
        "photo": td.PHOTO_INFO,
        "todo": td.TODO_INFO,
        "user": td.USER_INFO
    }
    return data_dict[element]


def get_data_len(name: str):
    load_dotenv()
    len_dict = {
        "posts": td.POSTS_LEN,
        "comments": td.COMMENTS_LEN,
        "albums": td.ALBUMS_LEN,
        "photos": td.PHOTOS_LEN,
        "todos": td.TODOS_LEN,
        "users": td.USERS_LEN
    }
    return len_dict[name]


def get_data_to_post(element: str):
    load_dotenv()
    data_dict = {
        "post": td.POST2POST,
        "comment": td.COMMENT2POST,
        "album": td.ALBUM2POST,
        "photo": td.PHOTO2POST,
        "todo": td.TO_DO2POST,
        "user": td.USER2POST,
        "wrong_post": td.WRONG_POST,
        "wrong_photo": td.WRONG_PHOTO,
        "wrong_todo": td.WRONG_TODO
    }
    return data_dict[element]


def get_data_to_put(element: str):
    load_dotenv()
    data_dict ={
        "post": td.POST2PUT,
        "comment": td.COMMENT2PUT,
        "album": td.ALBUM2PUT,
        "photo": td.PHOTO2PUT,
        "todo": td.TODO2PUT,
        "user": td.USER2PUT
    }
    return data_dict[element]


def get_data_to_patch(element: str):
    load_dotenv()
    data_dict = {
        "post": td.POST2PATCH,
        "comment": td.COMMENT2PATCH,
        "album": td.ALBUM2PATCH,
        "photo": td.PHOTO2PATCH,
        "todo": td.TODO2PATCH,
        "user": td.USER2PATCH
    }
    return data_dict[element]


class ApiFunctions:
    def __init__(self):
        load_dotenv()
        self.api_url = os.getenv("API_URL")

    def send_request(self, request_type: str, endpoint: str, data=None):
        if request_type == "GET":
            return requests.get(self.api_url + endpoint)
        elif request_type == "POST":
            data_ = get_data_to_post(data)
            return requests.post(self.api_url + endpoint, json=data_)
        elif request_type == "PUT":
            data_ = get_data_to_put(data)
            return requests.put(self.api_url + endpoint, json=data_)
        elif request_type == "PATCH":
            data_ = get_data_to_patch(data)
            return requests.patch(self.api_url + endpoint, json=data_)
        elif request_type == "DELETE":
            return requests.delete(self.api_url + endpoint)

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

    def check_delete_return(self, response: Response):
        data = response.json()
        info_to_check = {}
        if data == info_to_check:
            return True
        else:
            return False

