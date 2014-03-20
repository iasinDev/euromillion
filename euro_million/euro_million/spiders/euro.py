import datetime

from scrapy.spider import Spider

from bs4 import BeautifulSoup

from euro_class import Euromillion


class EuroMillionSpider(Spider):
    name = "euro_numbers"
    allowed_domains = ["national-lottery.co.uk"]
    start_urls = [
        "https://www.national-lottery.co.uk/player/euromillions/results/results.ftl"
    ]

    def clean_list(self, string):
        return ", ".join(string.replace("-", '').replace('\n', '').rsplit())

    def parse(self, response):
        import ipdb; ipdb.set_trace()
        soup = BeautifulSoup(response.body)
        table = soup.find('table', {'class': 'drawhistory'})
        tbody = table.find('tbody')
        rows = tbody.findAll('tr')
        for row in rows:
            if row.find('td', {'class': 'first'}):
                row_gen = list(row.stripped_strings)
                date = datetime.datetime.strptime(
                    row_gen[0], "%a %d %b %y"
                )
                five_numbers = self.clean_list(row_gen[1])
                lucky_numbers = self.clean_list(row_gen[2])
                euro = Euromillion()
                euro.insert_data(date, five_numbers, lucky_numbers)
                euro.close_connection()
