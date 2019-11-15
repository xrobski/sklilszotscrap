import re
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, link):
        self.links = []
        self.page_to_scrap = link

    def connect_with_page(self):
        self.result = requests.get(self.page_to_scrap)
        self.soruce = self.result.content
        self.soup = BeautifulSoup(self.soruce, 'lxml')

    def colecting_links(self):
        for link in self.soup.find_all(href=re.compile(r"/jobs/\d+")):
            self.links.append(('{}{}'.format('www.skillshot.pl', link.get('href'))))

    def next_page(self):
        if self.soup.find_all("a", class_="page-link", rel="next"):
            self.page_to_scrap ="http://www.skillshot.pl"+ self.soup.find_all("a", class_="page-link", rel="next")[0].get('href')
        else:
            self.page_to_scrap = False

    def run_process_of_scrapping(self):
        while self.page_to_scrap:
            self.connect_with_page()
            self.next_page()



test = Scrapper("http://www.skillshot.pl/")
# print(test.connect_with_page())
print(test.run_process_of_scrapping())
# print(test.scrapp_a_website_for_links())
