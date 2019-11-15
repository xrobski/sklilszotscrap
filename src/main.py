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
            self.links.append(('{}{}'.format('http://www.skillshot.pl', link.get('href'))))

    def next_page(self):
        if self.soup.find_all("a", class_="page-link", rel="next"):
            self.page_to_scrap ="http://www.skillshot.pl"+ self.soup.find_all("a", class_="page-link", rel="next")[0].get('href')
        else:
            self.page_to_scrap = False

    def run_process_of_scrapping(self):
        while self.page_to_scrap:
            self.connect_with_page()
            self.colecting_links()
            self.next_page()

    def offers_excractor(self):
        for link in self.links:
            self.page_to_scrap = link
            self.connect_with_page()
            # self.category = self.soup.find_all(class_=re.compile("badge badge-default badge-job-category"))
            # self.id = pass
            # self.name = pass

            self.category = self.soup.find(class_=re.compile("badge badge-default badge-job-category")).string
            self.views = self.soup.find_all("strong")[1].string
            self.pub_date = self.soup.find_all("strong")[0].string
            # print(self.category)
            # print(self.views)
            # print(self.pub_date)

            x = re.findall("+\d", link)
            print(x)
            
            exit()



test = Scrapper("https://www.skillshot.pl/jobs?page=5")
# print(test.connect_with_page())
print(test.run_process_of_scrapping())
test.offers_excractor()
# print(test.scrapp_a_website_for_links())
