import unittest
import os
import json

from task1.main import Hub, Lead, Company


class TestTaskTestCase(unittest.TestCase):

    def setUp(self):
        RESULT_DIR = 'result'
        self.RESULT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), RESULT_DIR)
        self.person = {
                "full_name": "Joe Doe",
                "job_title": "CEO",
                "profile_url": "https://linkedin.com/in/joedoe",
                "location": "Italy",
                "email": "mail@domain.com",
                "phone_number": "+1-354-489-4804"
            }

        self.person2 = {
                "full_name": "Big Ben",
                "job_title": "SMM",
                "profile_url": "https://linkedin.com/in/bigben",
                "location": "UK",
                "email": "mail@domain.com",
                "phone_number": "+2-354-489-4804"
            }

        self.list_of_persons = [
            {
                "full_name": "Joe Doe",
                "profile_url": "https://linkedin.com/in/joedoe",
                "company_fk": "https://fanta.com"
            },
            {
                "full_name": "Big Ben",
                "profile_url": "https://linkedin.com/in/bigben",
                "company_fk": "https://cocacola.com"
            },
        ]
        self.company = {
                "name": "Fanta",
                "company_url": "https://fanta.com",
                "location": "Italy, Roma",
                "revenue": "$365M"
            }

        self.company2 = {
                "name": "Coca-Cola",
                "company_url": "https://cocacola.com",
                "location": "UK, London",
                "revenue": "$675M"
            }
        self.list_of_companies = [
            {
                "name": "Fanta",
                "company_url": "https://fanta.com"
            },
            {
                "name": "Coca-Cola",
                "company_url": "https://cocacola.com"
            },
        ]
        self.persons = [self.person, self.person2]
        self.companies = [self.company, self.company2]

    # Class HUB

    # Method GET_REQ
    def test_get_req(self):
        self.assertEqual(self.person, Hub.get_req('person_url')[0])

    # Class Lead
    def test_Lead(self):
        lead = Lead(
            full_name="Big Ben",
            job_title="SMM",
            profile_url="https://linkedin.com/in/bigben",
            location="UK",
            email="mail@domain.com",
            phone_number="+2-354-489-4804"
        )
        self.assertEqual(lead.add_lead_to_company(), self.person2)

    # Class Company
    def test_Company(self):
        company = Company(
            name="Coca-Cola",
            company_url="https://cocacola.com",
            location="UK, London",
            revenue="$675M"
        )

        json_data = [
            {
                "full_name": "Big Ben",
                "job_title": "SMM",
                "profile_url": "https://linkedin.com/in/bigben",
                "location": "UK",
                "email": "mail@domain.com",
                "phone_number": "+2-354-489-4804"
            }
        ]

        self.assertEqual(company.create_company_report(), json_data)

    # Class Searcher


if __name__ == '__main__':
    unittest.main()
