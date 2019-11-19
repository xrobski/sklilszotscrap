import sqlite3
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

    def colect_links(self):
        for link in self.soup.find_all(href=re.compile(r"/jobs/\d+")):
            self.links.append(('{}{}'.format('http://www.skillshot.pl', link.get('href'))))

    def next_page(self):
        if self.soup.find_all("a", class_="page-link", rel="next"):
            self.page_to_scrap ="http://www.skillshot.pl"+ self.soup.find_all("a", class_="page-link", rel="next")[0].get('href')
        else:
            self.page_to_scrap = False

    def run_process_of_scrap(self):
        while self.page_to_scrap:
            self.connect_with_page()
            self.colect_links()
            self.next_page()

    def offers_excractor(self):
        for link in self.links:
            self.page_to_scrap = link
            self.connect_with_page()

            self.direct_link = link
            self.u_id = re.findall(r"[0-9]+", link)[0]
            self.category = self.soup.find(class_=re.compile("badge badge-default badge-job-category")).string
            self.name = self.soup.find("h1").string
            self.views = re.search(r"\d+\s\w+", self.soup.text).group()
            self.pub_date = re.search(r"\d+-\d+-\d+", self.soup.text).group()

            scrap_localization = self.soup.find_all("p", style="font-size: 115%; margin-bottom: 0.7rem;")[0].text
            self.localization = scrap_localization[scrap_localization.find(' w ')+3:]

            exit()


test = Scrapper("https://www.skillshot.pl/jobs?page=5")
test.run_process_of_scrap()
test.offers_excractor()
