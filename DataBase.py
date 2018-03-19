import sqlite3 as sq

class PaperDataBase:
    def __init__(self):
        self.db, self.c = self.__set_DB()
        self.__set_Table()

    def __set_DB(self):
        db = sq.connect('JData.db')
        c = db.cursor()

        return db, c

    def __set_Table(self):
        try:
            self.c.execute("create table Journal(FileName, URL, Title, Authors, Year, JName, Vol, Abst);")
        except sq.OperationalError:
            pass


    def SearchDB(self, FileName, Author, KeyWords):
        """
        Connect to SetResult in main.py and connect to Search button
        :param FileName: File name of .pdf
        :param Author: Authors' name or empty
        :param KeyWords: Key words' list
        :return: String list shows absolute path to the .pdf file. We will also use this result to open PDF file
        """
        #TODO : Make conditional expression 'Where (cond1) and (cond2) and ...'
        #TODO : Search with that expression 'select * from Journal (conditional expression)'
        #TODO : Append serch result in a List and return it

        return []

    def RegistDB(self, FileName, URL):
        """
        Regist (FileName, URL, Title, AuthorsName, Year, JournalName, Vol., Abstract) to DataBase
        If could not get paper's info, raise AssertionError
        :param FileName: File name of .pdf
        :param URL: URL to the info page of the paer
        :return: None. Registrate the journal info to DataBase
        """
        #TODO : If URL = '', analyze PDF file and get URL -> if cannot, raise AassertionError
        #TODO : Scrape the HP and get neccesary info -> if cannnot, raise AssertionError
        raise AssertionError

class FilePath:

    def __init__(self):
        self.db, self.c = self.__set_DB()
        self.set_Table()

    def __set_DB(self):
        db = sq.connect('FilePath.db')
        c = db.cursor()

        return db, c

    def set_Table(self):
        try:
            self.c.execute("create table FilePath(path);")
        except sq.OperationalError:
            pass


    def is_empty(self):
        """
        If the DataBase of file path to papers is empty or there isn't FilePath.db, return True.
        :return: Boolean
        """
        self.c.execute('select * from FilePath')
        PathList = []
        for row in self.c:
            PathList.append(row)
        if PathList: return False

        return True

    def add_path(self, path):
        sql = "insert into FilePath values(?);"
        self.c.execute(sql, [path])
        self.db.commit()

        return None

    def clear(self):
        self.c.execute("delete from FilePath;")
        self.db.commit()

    def close(self):
        self.db.close()

class PDFPath:
    def __init__(self):
        self.DB, self.c = self.__set_DB()
        self.__set_Table()

    def __set_DB(self):
        DB = sq.connect('PDFPath.db')
        c = DB.cursor()

        return DB, c

    def __set_Table(self):
        try:
            self.c.execute('create table PDF_path(FileName, Path);')
        except sq.OperationalError:
            pass

    def SearchDB(self, FileName):
        """
        Return absolute path of a paper. Using this path, open PDF with os.popen(path) connected to QListWidget.
        :param FileName: PDF File Name
        :return: Absolute Path to the FileName
        """
        self.c.execute('search * from PDF_path where FileName=' + FileName)
        for row in self.c:
            return row[1]

    def RegistEB(self, FileName, Path):
        self.c.execute('insert into PDF_path values(?, ?)', (FileName, Path))