##THIS IS A PROJECT FOR THEORYA YPOLOGISMOU
import re
import requests
from bs4 import BeautifulSoup


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
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    def extractData(self):
        if self.soup is not None:
            # Example: Extract all the text from the page
            text = self.soup.get_text()
            print(re.findall(r'\b[A-Za-z][a-z]+\b', text)  # Example regex to find capitalized words
)
        else:
            print("Page not loaded. Please call getPage() first.")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Trikala"  # Replace with the URL you want to scrape
    scraper = scraperPage(url)
    scraper.getPage()
    scraper.extractData()
