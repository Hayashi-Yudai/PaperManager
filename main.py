from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QHBoxLayout, QMainWindow, QMessageBox,
                             QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon

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

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        pathAction = QAction('Path', self)
        pathAction.triggered.connect(self.SetFilePath)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        pathmenu = menubar.addMenu('&Setting')
        fileMenu.addAction(exitAction)
        pathmenu.addAction(pathAction)

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
        self.Search_result = QTextEdit()
        self.LaTex_result = QTextEdit()

        self.Search_result.setReadOnly(True)
        self.LaTex_result.setReadOnly(True)
        text = QHBoxLayout()
        text.addWidget(self.Search_result)
        text.addWidget(self.LaTex_result)

        return text

    def get_KeyWord(self):
        """
        :return: String List of KeyWords
        """
        KeyWord = self.KeyWords.text()

        if ',' in KeyWord:
            return KeyWord.split(',')
        return KeyWord.split(' ')

    def Search(self):
        FileName = self.FileName.text()
        Author = self.Author.text()
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
        except:
            return QMessageBox.information(self, 'Message', 'Cannot Regist journal info')

    def LaTeX(self):
        FileName = self.FileName.text()
        try:
            self.LaTex_result.setText(LaTeX.LaTeX().ToLaTeX(FileName))
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

        raise AssertionError

class SetPath(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.initUI()

    def initUI(self):
        PathEntrance = QGridLayout()
        Phrase = QLabel('Setting the paper folder')
        self.PathSpace = QLineEdit()
        PathEntrance.addWidget(Phrase,0,0)
        PathEntrance.addWidget(self.PathSpace,1,0)

        Buttons = QHBoxLayout()
        self.OKButton = QPushButton('OK')
        self.CancelButton = QPushButton('Cancel')
        self.ConfirmPath = QPushButton('Confirm Path')
        Buttons.addWidget(self.OKButton)
        Buttons.addWidget(self.CancelButton)
        Buttons.addWidget(self.ConfirmPath)

        self.OKButton.clicked.connect(self.RegistPath)

        PathWindow = QVBoxLayout()
        PathWindow.addLayout(PathEntrance)
        PathWindow.addLayout(Buttons)
        self.setLayout(PathWindow)

        self.setGeometry(300, 300, 600, 100)
        self.show()

    def RegistPath(self):
        path = self.PathSpace.text()
        DataBase.FilePath().add_path(path)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())