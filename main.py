##THIS IS A PROJECT FOR THEORYA YPOLOGISMOU
import re
import requests
from bs4 import BeautifulSoup
import time
import argparse


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
            self.soup = BeautifulSoup(response.text, 'html.parser').get_text()
            return self.soup
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


class Find:
    def __init__(self, soup):
        
        self.soup = soup
        #self.text = self.soup.get_text()

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
    
    def findPopulation(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'[Mm]unicipality([0-9]+,?[0-9]+)',self.text)[1]

    def findArea(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'[Mm]unicipality([0-9]+\.?[0-9]+)',self.text)[0]

    def findRegion(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'Administrative region([A-Z][a-z]+(?: [A-Z][a-z]+)?)',self.text)[0]

    def findCoordinates(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'Coordinates:\s([0-9]+°[0-9]+..*[0-9]+°[0-9]+.*[NSWE])',self.text)[0]

    def findElevation(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'[Ee]levation([0-9]+)',self.text)[0]
    
    def findTimeZone(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'UTC\+[0-9+]',self.text)

    def findTemp(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        tempArray=re.findall(r'−?[0-9]+.?[0-9]\(−?[0-9]+\.?[0-9]\)',self.text)
        return tempArray[12],tempArray[64],tempArray[38]
    
    def findCountry(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'Country.?([A-Z][a-z]+)',self.text)[0]

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Scrape a Wikipedia page for specific information.")
    parser.add_argument('--url', type=str, help='The URL of the Wikipedia page to get info')
    args=parser.parse_args()
    if  args.url is None:
        url=input("URL : ")
    else:
        url=args.url
    scraper = scraperPage(url)

    """with open("data.txt", "r", encoding="utf-8") as file:
        page = file.read()"""
    

    page=scraper.getPage()
    finder=Find(page)
    try:
        print("NAME : "+finder.findName())
        print("COUNTRY : "+finder.findCountry())
        print("POPULATION : "+finder.findPopulation())
        print("AREA : "+finder.findArea()+" km²")
        print("REGION : "+finder.findRegion())
        print("COORDINATES : " +finder.findCoordinates())
        print("ELEVATION : "+finder.findElevation()+" m")
        print("TIMEZONE : "+finder.findTimeZone()[0])
        print("TEMPERATURE(YEAR HIGH/YEAR LOW/YEAR AVG) : "+finder.findTemp()[0]+"/"+finder.findTemp()[1]+"/"+finder.findTemp()[2])
    except IndexError:
        print("Some information could not be found on the page.")