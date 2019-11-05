## 1 cylkl programu ##
# 1) nawiązywanie połączenia ze stroną
# 2) jeżeli kod połączenia to 200 przechodzę dalej
# 3) wyszukuje wszystkie pozycje w danej kategorii
# 4) zaczynam iterować po każdej z nich
    # 5) jeżeli pozycja jest nowa - tworzę nowy wpis w bazie
    # 6) jeżeli pozycja jest stara ale różni się aktualizuje
    # 7) jeżeli pozycja jest stara ale nie różni się pomijam


import requests
from bs4 import BeautifulSoup

#print(result.status_code)

class Offers:
    connection = requests.get("https://www.skillshot.pl/jobs?category=grafika")

    def __init__(self, title):
        #, link, publication_date, category, views
        self.title = title
        #self.link = link
        #self.publication_date = publication_date
        #self.category = category
        #self.views = views

    def scrapp_a_website(self):
        print(self.connection)


first_offer = Offers("abc")
print(first_offer.scrapp_a_website())
