import re
import requests
from bs4 import BeautifulSoup


class Jobs:
    def __init__(self):
        # Hardcode link for scrapping an offers
        self.actual_page = "https://www.skillshot.pl/"
        self.connection = requests.get(self.actual_page)
        self.src = self.connection.content
        self.soup = BeautifulSoup(self.src, 'lxml')

        self.links = []
        self.page_counter = len(self.soup.find_all("a", class_="page-link"))

        # Function that's scrapping for links
    def scrapping_page(self):
        for link in self.soup.find_all(href=re.compile(r"/jobs/\d+")):
            self.links.append(('{}{}'.format('www.skillshot.pl', link.get('href'))))

    def next_page(self):
        if self.soup.find_all("a", class_="page-link", rel="next"):
            print(self.page_counter)


        # for page in self.soup.find_all("a", class_="page-link", rel="next"):
        #     self.pages.add(page.get('href'))
        # print(self.pages)

    # def process_of_scrapping(self):
    #     for x in range():
    #         self.scrapp_a_website_for_links
    #         self.change_page

test = Jobs()
print(test.next_page())
# print(test.scrapp_a_website_for_links())
