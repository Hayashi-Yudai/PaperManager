class PaperDataBase:

    def SearchDB(self, FileName, Author, KeyWords):
        """
        Connect to SetResult in main.py and connect to Search button
        :param FileName: File name of .pdf
        :param Author: Authors' name or empty
        :param KeyWords: Key words' list
        :return: String list shows absolute path to the .pdf file. We will also use this result to open PDF file
        """
        return []

    def RegistDB(self, FileName, URL):
        """
        Regist (FileName, URL, AuthorsName, Year, JournalName, Vol., Abstract) to DataBase
        If could not get paper's info, show pop up window
        :param FileName: File name of .pdf
        :param URL: URL to the info page of the paer
        :return: None. Registrate the journal info to DataBase
        """
        raise AssertionError

class FilePath:

    def is_empty(self):
        """
        If the DataBase of file path to papers is empty or there isn't FilePath.db, return True.
        :return: Boolean
        """
        return False

    def add_path(self, path):
        pass