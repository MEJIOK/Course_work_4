from colorama import *


def filter_jobs(jobs_list, filter_words):
    """
    Function for filtering jobs
    """
    if not isinstance(jobs_list, list):
        return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']

    elif not filter_words:
        return jobs_list

    filtered_jobs = []
    for job in jobs_list:
        count = 0

        for word in filter_words:
            if (word in job.name or word in job.area or word in job.experience
                    or word in job.employer or word in job.requirement or word in job.responsibility):
                count += 1
                if count > 1:
                    continue
                filtered_jobs.append(job)

    if len(filtered_jobs) == 0 or filtered_jobs is None:
        return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']
    else:
        return filtered_jobs


def filter_jobs_by_salary(filtered_jobs, salary_range):
    """
    Function for getting jobs by salary
    """
    if isinstance(filtered_jobs, (int, str)):
        return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']

    try:
        if not salary_range:
            return filtered_jobs
        else:
            try:
                from_salary, to_salary, currency = salary_range.split(',')

                ranged_jobs = []
                for job in filtered_jobs:
                    if int(from_salary) <= int(job.salary) <= int(to_salary) and job.currency == currency:
                        ranged_jobs.append(job)
                return ranged_jobs

            except AttributeError:
                return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']
    except ValueError:
        return [f'{Fore.RED}Изменение формата ввода диапазона зарплат{Fore.RESET}']


def get_top_jobs(sorted_jobs, top_n):
    """
    Function for getting top jobs
    """
    if not top_n:
        top_n = len(sorted_jobs)
        top_jobs = sorted_jobs[:top_n]
        return top_jobs

    try:
        top_n = int(top_n)
        if len(sorted_jobs) < top_n:
            top_n = len(sorted_jobs)

        top_jobs = sorted_jobs[:top_n]
        return top_jobs

    except ValueError:
        return [f'{Fore.RED}Ошибка при вводе верхней N. Введите номер{Fore.RESET}']
