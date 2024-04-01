from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """
    Abstract class for working with job service APIs, serves as a template for all subclasses
    """

    @abstractmethod
    def get_jobs(self, search_query):
        pass
