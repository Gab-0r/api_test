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


class ApiFunctions:
    def __init__(self):
        load_dotenv()
        self.api_url = os.getenv("API_URL")

    def get_request(self, endpoint):
        return requests.get(self.api_url + endpoint)

    def check_status_code(self, response: Response, status_code):
        return True if response.status_code == int(status_code) else False

    def check_get(self, response: Response, element: str):
        info_to_check = element_to_data(element)
        info_obtained = response.json()
        if info_to_check == info_obtained:
            return True
        else:
            return False

