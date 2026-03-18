##THIS IS A PROJECT FOR THEORYA YPOLOGISMOU
import re
import requests
from bs4 import BeautifulSoup
import time


class scraperPage:
    def __init__(self, url):
        self.url=url
        self.soup=None

    def getPage(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            response = requests.get(self.url,headers=headers)
            response.raise_for_status()  # Check if the request was successful
            self.soup = BeautifulSoup(response.text, 'html.parser')
            return self.soup
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


class Find:
    def __init__(self, soup):
        self.soup = soup
        self.text = self.soup.get_text()

    def extractTokens(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return []
        # Use regex to find words (tokens)
        tokens = re.findall(r'\b[A-Za-z][a-z]+\b', self.text)
        
        return tokens
    
    def findName(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.search(r'[A-Z][a-z]+',self.text).group()



if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Trikala"  # Replace with the URL you want to scrape
    scraper = scraperPage(url)
    page=scraper.getPage()
    finder=Find(page)
    name=finder.findName()
    print(name)
