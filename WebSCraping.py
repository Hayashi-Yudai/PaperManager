from bs4 import BeautifulSoup
#import os
import re
import requests
#from selenium import webdriver




class Scraper:
    def __init__(self, URL):
        self.URL = URL
        self.soup = self.BS_object()


    def BS_object(self):
        #Cookiesの関係でPhantomJSでしか開けないページがあるかも
        # driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
        # # get a HTML response
        # driver.get(self.url)
        # html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
        #soup = BeautifulSoup(html, "lxml")
        r = requests.get(self.URL)
        soup = BeautifulSoup(r.text, "lxml")

        return soup



    def get_title(self):
        pass



    def get_authors(self):
        pass



    def get_year(self):
        pass


    def get_JName(self):
        pass



    def get_Vol(self):
        pass



    def get_Abst(self):
        pass