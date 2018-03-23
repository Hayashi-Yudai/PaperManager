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
        #Some pages may open only by PhantomJS because of Cookies
        # driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
        # # get a HTML response
        # driver.get(self.url)
        # html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
        #soup = BeautifulSoup(html, "lxml")
        r = requests.get(self.URL)
        soup = BeautifulSoup(r.text, "lxml")

        return soup



    def get_title(self):
        """
        Title of the paper. If cannot find, return -1
        :return: String
        """
        if self.URL == -1:
            return -1

        result = self.soup.find('meta', {'property' : 'og:title'})
        try:
            return result.get("content")
        except:
            return -1



    def get_authors(self):
        """
        Full name of authors
        :return: List of String
        """
        pass



    def get_year(self):
        """
        :return: String
        """
        pass


    def get_JName(self):
        """
        Return abbrebiated name used in reference. For example,
            Physical Review B -> Phys. Rev. B
            Nature Physics -> Nat. Phys.
        :return: String
        """
        pass



    def get_Vol(self):
        """
        Volume and page
        :return: List of String.
        """
        pass



    def get_Abst(self):
        """
        If I can, return LaTeX form abstract and compile with Tex compiler (Future Plan)
        :return: String
        """
        pass





class PhysRev(Scraper):
    def __init__(self, URL):
        super().__init__(URL)



    def get_authors(self):

        authors = str(self.soup.find('h5', {'class': 'authors'}))
        try:
            return re.search(r'>.*<', authors).group()[1:-1]
        except:
            return -1



    def get_year(self):
        pass



    def get_JName(self):
        pass



    def get_Vol(self):
        pass



    def get_Abst(self):
        pass





class Nature(Scraper):
    def __init__(self, URL):
        super().__init__(URL)



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





class JPSJ(Scraper):
    def __init__(self, URL):
        super().__init__(URL)



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





class APL(Scraper):
    def __init__(self, URL):
        super().__init__(URL)



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
