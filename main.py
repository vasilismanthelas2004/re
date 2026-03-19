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
    
    def findPopulation(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'Municipality[0-9]+\.?[0-9]+',self.text)[1].replace("Municipality","")

    def findArea(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'Municipality[0-9]+\.?[0-9]+',self.text)[0].replace("Municipality","")

    def findRegion(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'region[A-Z][a-z]+Regional',self.text)[0].replace("region","").replace("Regional","")

    def findCoordinates(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'Coordinates:\s[0-9]+°[0-9]+..*[0-9]+°[0-9]+..',self.text)[0].replace("Coordinates: ","")    

    def findElevation(self):
        if self.soup is None:
            print("Soup object is not initialized.")
            return None
        return re.findall(r'Elevation[0-9]+',self.text)[0].replace("Elevation","")
    
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

if __name__ == "__main__":
    #url="https://en.wikipedia.org/wiki/Larissa"
    url = "https://en.wikipedia.org/wiki/Trikala"  # Replace with the URL you want to scrape
    scraper = scraperPage(url)

    """with open("data.txt", "r", encoding="utf-8") as file:
        page = file.read()"""
    

    page=scraper.getPage()
    finder=Find(page)
    
    print("NAME : "+finder.findName())
    print("POPULATION : "+finder.findPopulation())
    print("AREA : "+finder.findArea()+" km²")
    print("REGION : " +finder.findRegion())
    print("COORDINATES : " +finder.findCoordinates())
    print("ELEVATION : "+finder.findElevation())
    print("TIMEZONE : "+finder.findTimeZone()[0])
    print("TEMPERATURE(YEAR HIGH/YEAR LOW/YEAR AVG) : "+finder.findTemp()[0]+"/"+finder.findTemp()[1]+"/"+finder.findTemp()[2])