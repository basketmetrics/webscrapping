import requests
from bs4 import BeautifulSoup


class Soup:
    def __init__(self, url):
        self.url = url
        self.html = None
        self.soup = None
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            response = requests.get(url, headers = headers)
            self.html_document = response.content
            self.soup = BeautifulSoup(self.html_document, "html.parser")
        except Exception as err:
            print(f"Soup::constructor::ERROR::{err}")

    def __del__(self):
        del self.html
        del self.soup
        del self.url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @url.deleter
    def url(self):
        del self.__url

    @property
    def html(self):
        return self.__html

    @html.setter
    def html(self, html):
        self.__html = html

    @html.deleter
    def html(self):
        del self.__html

    @property
    def soup(self):
        return self.__soup

    @soup.setter
    def soup(self, soup):
        self.__soup = soup

    @soup.deleter
    def soup(self):
        del self.__soup