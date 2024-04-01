import unittest
from src.classes.job import Job
from src.filters import get_top_jobs


class TestFilters(unittest.TestCase):
    def setUp(self):
        self.job1 = Job(name="Job1", area="Moscow", requirement="Requirements for Job1",
                        responsibility="Responsibilities for Job1",
                        salary={"from": 1000, "to": 2000, "currency": "RUR"}, currency="RUR", experience="Entry level",
                        employer="Company1", url="https://example.com/job1")
        self.job2 = Job(name="Job2", area="Novosibirsk", requirement="Requirements for Job2",
                        responsibility="Responsibilities for Job2",
                        salary={"from": 1500, "to": 2500, "currency": "USD"}, currency="USD", experience="Mid level",
                        employer="Company2", url="https://example.com/job2")
        self.job3 = Job(name="Job3", area="Saint Petersburg", requirement="Requirements for Job3",
                        responsibility="Responsibilities for Job3", salary=None, currency="", experience="Senior level",
                        employer="Company3", url="https://example.com/job3")

        self.jobs_list = [self.job1, self.job2, self.job3]

    def test_get_top_jobs(self):
        top_jobs = get_top_jobs(self.jobs_list, '2')
        self.assertEqual(len(top_jobs), 2)  # Ожидаем, что будет найдено 2 вакансии

        top_jobs = get_top_jobs(self.jobs_list, '3')
        self.assertEqual(len(top_jobs), 3)  # Ожидаем, что будет найдено 3 вакансии


if __name__ == '__main__':
    unittest.main()
