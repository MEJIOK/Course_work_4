import os
import json
from src.classes.abstract_manager import AbstractDataManager


class DataManager(AbstractDataManager):
    """
    Class for working with files
    """

    def __init__(self, filename):
        """
        Constructor takes the path to the file
        """
        self.filename = filename

    def add_job(self, value):
        """
        Adds data to the file
        """
        with open(self.filename, 'a', encoding='UTF-8') as file:
            json.dump(value, file, indent=2, ensure_ascii=False)
            file.write('\n')

    def open_file(self):
        """
        Opens the file for reading
        """
        with open(self.filename, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def delete_job(self):
        """
        Completely clears the file
        """
        open(self.filename, 'w').close()
        os.remove(self.filename)
