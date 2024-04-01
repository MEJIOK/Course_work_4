from colorama import *


class Job:
    """
    Class for working with job listings
    """

    def __init__(self, name, area, requirement, responsibility, salary, currency, experience, employer, url):
        self.name = name
        self.area = area
        self.requirement = self.check(requirement)
        self.responsibility = self.check(responsibility)
        self.salary = self.check_salary(salary)
        self.currency = currency
        self.experience = experience
        self.employer = employer
        self._url = url

    @staticmethod
    def check(value):
        """
        Check attribute values for None
        """
        if value is None:
            return f'Requirements are not specified'
        else:
            return f'{value}'

    @staticmethod
    def check_salary(value):
        """
        Function used to check attribute values for salary on None
        """
        if isinstance(value, dict):
            if value['from'] is None:
                return int(value['to'])

            elif value['to'] is None:
                return int(value['from'])
            else:
                return (int(value['from']) + int(value['to'])) / 2
        else:
            return 0

    def __lt__(self, other):
        """
        Function for comparing jobs by salary
        """
        if self.salary < other:
            return True
        return False

    def __eq__(self, other):
        """
        Function for comparing jobs by salary
        """
        if self.salary == other:
            return True
        return False

    def __le__(self, other):
        """
        Function for comparing jobs by salary
        """
        if self.salary <= other:
            return True
        return False

    @classmethod
    def from_dict(cls, data: list):
        """
        Conversion of JSON data set to a list of objects
        """
        if isinstance(data, list):

            jobs_list = []
            for value in data:
                if value['salary'] is None:
                    currency = ''
                else:
                    currency = value['salary']['currency']

                jobs_list.append(cls(name=value['name'],
                                     area=value['area']['name'],
                                     requirement=value['snippet']['requirement'],
                                     responsibility=value['snippet']['responsibility'],
                                     salary=value['salary'],
                                     currency=currency,
                                     experience=value['experience']['name'],
                                     employer=value['employer']['name'],
                                     url=value['alternate_url']))

            if len(jobs_list) == 0 or jobs_list is None:
                return f"Invalid data format"

            return jobs_list
        else:
            return f"Invalid data format"

    def __str__(self):
        """
        String representation of class attributes for the user
        """
        if self.salary == 0:
            self.salary = f"Salary not specified"
        return (f'Job Title: {Fore.CYAN}{self.name}{Fore.RESET}\n'
                f'City: {Fore.CYAN}{self.area}{Fore.RESET}\n'
                f'Requirements: {Fore.CYAN}{self.requirement}{Fore.RESET}\n'
                f'Responsibilities: {Fore.CYAN}{self.responsibility}{Fore.RESET}\n'
                f'Salary: {Fore.CYAN}{self.salary} {self.currency}{Fore.RESET}\n'
                f'Experience required: {Fore.CYAN}{self.experience}{Fore.RESET}\n'
                f'Employer: {Fore.CYAN}{self.employer}{Fore.RESET}\n'
                f'URL: {self._url}\n')

    def __repr__(self):
        """
        Display information about the class for the developer
        """
        return (
            f'Class Name: {self.__class__.__name__}. Class Attributes: ({self.name}, {self.area}, {self.requirement}, '
            f'{self.responsibility}, {self.salary}, {self.experience}, {self._url})\n')
