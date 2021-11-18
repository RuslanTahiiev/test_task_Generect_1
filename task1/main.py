import json
import os

REQ_DIR = 'req'
RESULT_DIR = 'result'
URL_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), REQ_DIR)
RESULT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), RESULT_DIR)


class Hub:
    @staticmethod
    def get_req(url):
        '''
            Я буду використовувати, не юрл, а лише ім'я тестового файлу імітуючи GET запит
            :param url: ім'я файлу
            :type url: str
            :return data: json данні
        '''

        with open(fr'{URL_ROOT}/{url}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data


class Lead:
    def __init__(self, full_name, job_title, profile_url, location, email, phone_number):
        self.full_name = full_name
        self.job_title = job_title
        self.profile_url = profile_url
        self.location = location
        self.email = email
        self.phone_number = phone_number

    def add_lead_to_company(self):
        return self._format_json()

    def _format_json(self):
        return {
                "full_name": self.full_name,
                "job_title": self.job_title,
                "profile_url": self.profile_url,
                "location": self.location,
                "email": self.email,
                "phone_number": self.phone_number
            }


class Company:

    def __init__(self, name, company_url, location, revenue):
        self.name = name
        self.company_url = company_url
        self.location = location
        self.revenue = revenue
        self.leads = []

    def __repr__(self):
        return f'{self.name} in list!\n'

    def create_company_report(self):
        self._create_data()

        if not os.path.exists(RESULT_ROOT):
            os.mkdir(RESULT_ROOT)

        print(RESULT_ROOT)

        with open(f'{RESULT_ROOT}/{self.name}_report.json', 'w', encoding='utf-8') as file:
            json.dump(self._format_json(), file, indent=4, ensure_ascii=False)

        return self._format_json()

    def _format_json(self):
        return {
                "name": self.name,
                "company_url": self.company_url,
                "location": self.location,
                "revenue": self.revenue,
                "leads": self.leads
            }

    def _create_data(self):
        persons = Hub.get_req('list_of_persons_url')
        for person in persons:
            if person['company_fk'] == self.company_url:
                data = Hub.get_req('person_url')
                for p in data:
                    if p['profile_url'] == person['profile_url']:
                        lead = Lead(
                            full_name=p['full_name'],
                            job_title=p['job_title'],
                            profile_url=p['profile_url'],
                            location=p['location'],
                            email=p['email'],
                            phone_number=p['phone_number']
                        )
                        self.leads.append(lead.add_lead_to_company())
                        print('Success!')


class Searcher:
    def __init__(self):
        self.companies = Hub.get_req('list_of_companies_url')

    def go(self):
        self.__parser_list_of_companies()

    def __parser_list_of_companies(self):
        for c in self.companies:
            companies = Hub.get_req('company_url')
            for company in companies:
                if c['company_url'] == company['company_url']:
                    company_obj = Company(
                        name=company['name'],
                        company_url=company['company_url'],
                        location=company['location'],
                        revenue=company['revenue']
                    )
                    print('Create company report for: ', company_obj)
                    company_obj.create_company_report()
        print('Done!')


def main():

    if not os.path.exists(REQ_DIR):
        os.mkdir(REQ_DIR)

    searcher = Searcher()
    searcher.go()


if __name__ == '__main__':
    main()
