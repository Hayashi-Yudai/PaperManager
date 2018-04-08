#***********************************Future Plan*************************************************
# Compile abstract info with LaTeX and show in a panel
# Setting some keyword and notificate periodically new papers relate to those words
#***********************************************************************************************

from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QHBoxLayout, QMainWindow, QMessageBox,
                             QLabel, QLineEdit, QListWidget, QPushButton, QTextEdit, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon
import os

import DataBase
import LaTeX



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.png'))
        if DataBase.FilePath().is_empty():
            self.SetFilePath()



    def initUI(self):
        ############################################
        # Widget layout
        ############################################
        centralWidget = QWidget()

        TextEntrance = self.TextEntrance()
        Buttons = self.Buttons()
        TextBox = self.TextBox()

        SubLayout = QHBoxLayout()
        SubLayout.addLayout(TextEntrance)
        SubLayout.addLayout(Buttons)
        MainLayout = QVBoxLayout()
        MainLayout.addLayout(SubLayout)
        MainLayout.addLayout(TextBox)
        centralWidget.setLayout(MainLayout)
        self.setCentralWidget(centralWidget)



        ############################################
        # Menubar Layout
        ############################################
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        registerAction = QAction('Auto Register', self)
        registerAction.triggered.connect(self.AutoRegistration)

        pathAction = QAction('Path', self)
        pathAction.triggered.connect(self.SetFilePath)
        SetPDFPath = QAction('Set PDF Path', self)
        SetPDFPath.triggered.connect(self.RegisterPDFPath)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        pathmenu = menubar.addMenu('&Setting')

        fileMenu.addAction(exitAction)
        fileMenu.addAction(registerAction)
        pathmenu.addAction(pathAction)
        pathmenu.addAction(SetPDFPath)

        self.setGeometry(300, 100, 600, 400)
        self.setWindowTitle('PaperResearcher')
        self.show()



    def SetFilePath(self):
        self.ex = SetPath()
        self.ex.show()



    def TextEntrance(self):
        self.FileName = QLineEdit()
        self.Author = QLineEdit()
        self.Journal = QLineEdit()
        self.KeyWords = QLineEdit()
        self.URL = QLineEdit()

        Text_Entrance = QGridLayout()
        Text_Entrance.addWidget(QLabel('File Name :'), 0, 0)
        Text_Entrance.addWidget(QLabel('Author :'), 1, 0)
        Text_Entrance.addWidget(QLabel('Journal :'), 2, 0)
        Text_Entrance.addWidget(QLabel('Key Words :'), 3, 0)
        Text_Entrance.addWidget(QLabel('URL :'), 4, 0)
        Text_Entrance.addWidget(self.FileName, 0, 1)
        Text_Entrance.addWidget(self.Author, 1, 1)
        Text_Entrance.addWidget(self.Journal, 2, 1)
        Text_Entrance.addWidget(self.KeyWords, 3, 1)
        Text_Entrance.addWidget(self.URL, 4, 1)

        return Text_Entrance



    def Buttons(self):
        buttons = QVBoxLayout()
        SearchBottun = QPushButton('Search')
        RegistrationButton = QPushButton('Registration')
        LaTeXButton = QPushButton('LaTeX')
        buttons.addWidget(SearchBottun)
        buttons.addWidget(RegistrationButton)
        buttons.addWidget(LaTeXButton)

        SearchBottun.clicked.connect(self.Search)
        RegistrationButton.clicked.connect(self.Registration)
        LaTeXButton.clicked.connect(self.LaTeX)

        return buttons



    def TextBox(self):
        self.search_phrase = QLabel('Search Result :')
        self.latex_phrase = QLabel('LaTeX Form :')
        self.Search_result = QListWidget()
        self.LateX_result = QTextEdit()
        self.CopyButton = QPushButton('Copy')

        self.LateX_result.setReadOnly(True)
        Search_items = QVBoxLayout()
        Search_items.addWidget(self.search_phrase)
        Search_items.addWidget(self.Search_result)
        TeXCopy = QVBoxLayout()
        TeXCopy.addWidget(self.latex_phrase)
        TeXCopy.addWidget(self.LateX_result)
        TeXCopy.addWidget(self.CopyButton)
        text = QHBoxLayout()
        text.addLayout(Search_items)
        text.addLayout(TeXCopy)

        self.Search_result.itemDoubleClicked.connect(lambda item : self.OpenPDF(item))
        self.CopyButton.clicked.connect(self.copy_tex)

        return text



    def get_KeyWord(self):
        """
        Transform entered KeyWords to a list of string
        :return: String List of KeyWords
        """
        KeyWord = self.KeyWords.text()

        if ', ' in KeyWord:
            return KeyWord.split(', ')
        if ',' in KeyWord:
            return KeyWord.split(',')

        return KeyWord.split(' ')



    def Search(self):
        FileName = self.FileName.text() #get FileName from FileName in TextEntrance
        Author = self.Author.text()     #get Authors from Author in TextEntrance
        KeyWords = self.get_KeyWord()   #String List of KeyWords

        try:
            self.SetResult(FileName, Author, KeyWords)
        except:
            return QMessageBox.information(self, 'Message', 'Cannot find such papers')



    def Registration(self):
        FileName = self.FileName.text()
        URL = self.URL.text()
        try:
            DataBase.PaperDataBase().RegistDB(FileName, URL)
            return QMessageBox.information(self, 'Message', 'Registered journal correctly')
        except:
            return QMessageBox.information(self, 'Message', 'Cannot Register journal info')



    def AutoRegistration(self):
        #TODO : Find papers have not been registered yet
        #TODO : Regisit these papers
        return None



    def LaTeX(self):
        FileName = self.FileName.text()
        try:
            self.LateX_result.setText(LaTeX.LaTeX().ToLaTeX(FileName))
        except:
            return QMessageBox.information(self, 'Message', 'Cannot create TeX format')



    def SetResult(self, FileName, Author, KeyWords):
        """
        Set Search result to Search_result. If cannnot find anything, raise AssertionError
        :param FileName:
        :param Author:
        :param KeyWords:
        :return: None
        """
        research_result = DataBase.PaperDataBase().SearchDB(FileName, Author, KeyWords)
        self.Search_result.clear()
        if research_result != []:
            for item in research_result:
                self.Search_result.addItem(item)     #show only FileName
        else:
            raise AssertionError



    def OpenPDF(self, item):
        pdf_path = DataBase.PDFPath().SearchDB(item.text())
        os.popen(pdf_path)



    def copy_tex(self):
        self.LateX_result.selectAll()
        self.LateX_result.copy()

        return None



    def RegisterPDFPath(self):
        paths  = DataBase.FilePath().get_path()
        pdf  = DataBase.PDFPath()
        try:
            pdf.clear()
        except:
            pass
        papers = DataBase.PaperDataBase()
        for path in paths:
            paper_list = papers.paper_list(path)
            for item in paper_list:
                pdf.RegistDB(item.split('/')[-1], item)

        return QMessageBox.information(self, 'Message', 'Registered All PDF Paths Correctly')





class SetPath(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.initUI()
        self.showPath()

    def initUI(self):
        PathEntrance = QGridLayout()
        Phrase = QLabel('Setting the paper folder')
        self.PathSpace = QLineEdit()
        self.PathPhrase = QLabel('Registerd Path :')
        self.PathList = QListWidget()
        PathEntrance.addWidget(Phrase,0,0)
        PathEntrance.addWidget(self.PathSpace, 1, 0)
        PathEntrance.addWidget(self.PathPhrase, 2, 0)
        PathEntrance.addWidget(self.PathList, 3, 0)

        Buttons = QHBoxLayout()
        self.OKButton = QPushButton('OK')
        self.CancelButton = QPushButton('Cancel')
        self.DeletePath = QPushButton('Delete Path')
        Buttons.addWidget(self.OKButton)
        Buttons.addWidget(self.CancelButton)
        Buttons.addWidget(self.DeletePath)

        self.OKButton.clicked.connect(self.RegistPath)
        self.CancelButton.clicked.connect(self.close)
        self.DeletePath.clicked.connect(self.Delete)


        PathWindow = QVBoxLayout()
        PathWindow.addLayout(PathEntrance)
        PathWindow.addLayout(Buttons)
        self.setLayout(PathWindow)

        self.setGeometry(300, 300, 400, 150)
        self.show()


    def showPath(self):
        path = DataBase.FilePath().get_path()
        for item in path:
            self.PathList.addItem(item)



    def RegistPath(self):
        path = self.PathSpace.text()
        if path == '': return QMessageBox.critical(self, 'ERROR', 'File Path is empty!')

        file = DataBase.FilePath()
        file.add_path(path)
        file.close()
        self.PathList.clear()
        self.showPath()



    def Delete(self):
        file = DataBase.FilePath()
        file.clear(self.PathList.currentItem().text())
        file.close()
        self.PathList.clear()
        self.showPath()
        QMessageBox.information(self, 'Message', 'Deleted Path from Data Base')





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())