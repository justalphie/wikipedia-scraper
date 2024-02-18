import json
import re
import requests
from requests import Session
from bs4 import BeautifulSoup

class WikipediaScraper:
    def __init__(self, base_url:str="https://country-leaders.onrender.com"):
        self.base_url= base_url
        self.country_endpoint = base_url+"/countries"
        self.leaders_endpoint = base_url+"/leaders"
        self.cookies_endpoint = base_url+"/cookie"
        self.leaders_data = {}
        self.session = Session()
        self.cookies = self.session.get(self.cookies_endpoint).cookies

    def __str__(self):
        return f"WikipediaScraper requests the {self.base_url} API to get data about the leaders of the countries in the list."

    def refresh_cookie(self) -> object:
        self.cookies = self.session.get(self.cookies_endpoint).cookies

    def get_with_cookies(self, url, params={}):
        try:
            result = self.session.get(url, params, cookies=self.cookies)
            if result.ok: 
                return result
            else:
                # refresh the cookie
                self.refresh_cookie()
                # try again
                return self.get_with_cookies(url, params)                
        except:
            # refresh the cookie
            self.refresh_cookie()
            # try again
            return self.get_with_cookies(url, params)

    def get_countries(self) -> list:
        return self.get_with_cookies(self.country_endpoint).json()

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        r = self.session.get(wikipedia_url)
        soup = BeautifulSoup(r.content, "html.parser")
        paragraphs =  soup.select("#mw-content-text > div.mw-parser-output > p")
        paragraphs = [p for p in paragraphs if len(p.text.strip())>0]
        first_paragraph = paragraphs[0].text
        patterns = [r"[/][^/]*[/][ ]*[;][ ]*", r"\/.*\/|\[.*\]|\] ;", r"Écouter", r"\(.*Écouter\)", r"Écouter\)", r"Écouter ;", r"\W;", r" ⓘ .*;", r"[A-z-ə]+;", r"uitspraakⓘ ", r"\(uitspraakⓘ\)"]
        for pattern in patterns:
            first_paragraph = re.sub(pattern, "", first_paragraph)
        return first_paragraph

    def get_leaders(self, country: str) -> None:
        params = {"country":f"{country}"}
        self.leaders_data[country] = self.get_with_cookies(self.leaders_endpoint, params=params).json()
        for i in range(len(self.leaders_data[country])):
            self.leaders_data[country][i]["first_paragraph"] = self.get_first_paragraph(self.leaders_data[country][i]["wikipedia_url"])

   
    def to_json_file(self, filepath: str) -> None:
        with open (filepath, "w", encoding="utf-8") as f:
            json.dump(self.leaders_data, f, indent=4, ensure_ascii = False)





