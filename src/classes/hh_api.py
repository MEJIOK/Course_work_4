import requests
from src.classes.abstract_api import AbstractAPI


class HHApi(AbstractAPI):
    """
    Class for working with hh.ru API requests
    """

    def __init__(self):
        """
        Default constructor with the URL address for working with hh.ru API requests
        """
        self.__base_url = "https://api.hh.ru/vacancies"

    def get_jobs(self, search_query):
        """
        Function returns data from the website based on the entered key
        """
        if search_query == '' or search_query == int:
            return f"Input cannot be empty or numeric"
        else:
            params = {"per_page": 100, "text": search_query, "page": 10}
            response = requests.get(self.__base_url, params=params)

            if response.status_code != 200:
                raise ConnectionError("Failed to access the website")
            else:
                return response.json()["items"]
