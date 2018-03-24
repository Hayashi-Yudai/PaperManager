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
    """
    Scrape
        * Physical Review Letters
        * Physical Review B
        * Review of Modern Physics
    """

    def __init__(self, URL):
        super().__init__(URL)



    def get_authors(self):
        authors = str(self.soup.find('h5', {'class': 'authors'}))
        try:
            author_list = re.search(r'>.*<', authors).group()[1:-1].split(', ')
            if 'and' in author_list[-1]:
                author_list[-1] = author_list[-1][4:]
            return author_list
        except:
            return -1



    def get_year(self):
        result = self.soup.find('meta', {'name' : 'citation_date'})
        try:
            return result.get("content").split('/')[0]
        except:
            return -1




    def get_JName(self):
        if 'prl' in self.URL:
            return 'Phys. Rev. Lett.'

        if 'prb' in self.URL:
            return 'Phys. Rev. B'

        if 'rmp' in self.URL:
            return 'Rev. Mod. Phys.'



    def get_Vol(self):
        info = self.URL.split('/')[-1]
        return info.split('.')[1:]



    def get_Abst(self):
        section = self.soup.find('section', {'class': 'article open abstract'})
        content = section.find('div', {'class' : 'content'})

        return content.get_text()






class Nature(Scraper):
    """
    Scrape
        * Nature
        * Nature Physics
        * Nature Nanotechnology
        * Nature Materials
        * Nature Optics
        * Nature Communications
    """

    def __init__(self, URL):
        super().__init__(URL)



    def get_authors(self):
        pass



    def get_year(self):
        dataLayer = self.soup.find("script", text=re.compile("dataLayer"))
        return re.search(r'"authors":\[.*"\]', str(dataLayer)).group()[11:-1].replace('"', '').split(',')



    def get_JName(self):
        pass



    def get_Vol(self):
        pass



    def get_Abst(self):
        pass





class Science(Scraper):
    """
    Scrape
        * Science
        * Scientific Reports
    """

    def __init__(self, URL):
        super().__init__(URL)



    def get_authors(self):
        return self.soup.find_all('meta', {'name': 'citation_author'})



    def get_year(self):
        pass



    def get_JName(self):
        pass



    def get_Vol(self):
        pass



    def get_Abst(self):
        pass





class JPSJ(Scraper):
    """
    Scrape
        * Journal of Phycical Society of Japan
    """

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
    """
    Scrape
        * Applied Physical Letters
    """

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





def SortJournal(URL):
    if 'PhysRev' in URL:
        return PhysRev(URL)

    if 'nature' in URL:
        return Nature(URL)

    if 'science' in URL:
        return Science(URL)

    if 'JPSJ' in URL:
        return JPSJ(URL)

    if 'APL' in URL:
        return APL(URL)