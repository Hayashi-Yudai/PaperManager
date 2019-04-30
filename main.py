# ***********************************Future Plan*************************************************
# Compile abstract info with LaTeX and show in a panel
# Setting some keyword and notificate periodically new papers relate to those words
# ***********************************************************************************************

from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QHBoxLayout, QMainWindow, QMessageBox,
                             QLabel, QLineEdit, QListWidget, QPushButton, QTextEdit, QVBoxLayout, QWidget,
                             QFileDialog)
from PyQt5.QtGui import QIcon
import os
import subprocess
import psycopg2

import DataBase


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.png'))

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

        #registerAction = QAction('Auto Register', self)
        # registerAction.triggered.connect(self.AutoRegistration)

        pathAction = QAction('Path', self)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        pathmenu = menubar.addMenu('&Setting')

        fileMenu.addAction(exitAction)
        # fileMenu.addAction(registerAction)
        # pathmenu.addAction(pathAction)

        self.setGeometry(300, 100, 600, 400)
        self.setWindowTitle('PaperResearcher')
        self.show()

    def TextEntrance(self):
        self.Title = QLineEdit()
        self.Author = QLineEdit()
        self.Journal = QLineEdit()
        self.KeyWords = QLineEdit()
        self.Path = QLineEdit()

        Text_Entrance = QGridLayout()
        Text_Entrance.addWidget(QLabel('Title :'), 0, 0)
        Text_Entrance.addWidget(QLabel('Author :'), 1, 0)
        Text_Entrance.addWidget(QLabel('Journal :'), 2, 0)
        Text_Entrance.addWidget(QLabel('Key Words :'), 3, 0)
        Text_Entrance.addWidget(QLabel('Path :'), 4, 0)
        Text_Entrance.addWidget(self.Title, 0, 1)
        Text_Entrance.addWidget(self.Author, 1, 1)
        Text_Entrance.addWidget(self.Journal, 2, 1)
        Text_Entrance.addWidget(self.KeyWords, 3, 1)

        Path_select = QGridLayout()
        file_button = QPushButton('...')
        file_button.clicked.connect(self.FileOpen)
        Path_select.addWidget(self.Path, 0, 0)
        Path_select.addWidget(file_button, 0, 1)
        Text_Entrance.addLayout(Path_select, 4, 1)

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
        # LaTeXButton.clicked.connect(self.LaTeX)

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

        self.Search_result.itemDoubleClicked.connect(
            lambda item: self.OpenPDF(item))

        return text

    def Registration(self):
        title = self.Title.text()
        authors = self.Author.text()
        journal = self.Journal.text()
        keyword = self.KeyWords.text()
        path = self.Path.text()

        db = DataBase.PaperDataBase('test', 'yudai')
        try:
            db.register(title, authors, journal, keyword, path)
        except psycopg2.errors.NotNullViolation:
            QMessageBox.warning(
                self, 'Message', 'The title should not be empty'
            )

    def Search(self):
        title = self.Title.text()
        authors = self.Author.text()
        journal = self.Journal.text()
        keyword = self.KeyWords.text()

        db = DataBase.PaperDataBase('test', 'yudai')
        result = db.search(title, authors, journal, keyword)

        self.Search_result.clear()
        for item in result:
            self.Search_result.addItem(item)

    def FileOpen(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Select File', '/home/yudai/Documents/papers'
        )
        self.Path.setText(fname[0])

    def OpenPDF(self, item):
        db = DataBase.PaperDataBase('test', 'yudai')
        result = db.search_pdf_path(item.text())
        if result != '':
            subprocess.Popen(['okular', result])


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
