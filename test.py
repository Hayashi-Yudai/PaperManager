# from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QHBoxLayout, QMainWindow, QMessageBox,
#                              QLabel, QLineEdit, QListWidget, QPushButton, QTextEdit, QVBoxLayout, QWidget)
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         centralWidget = QWidget()
#         MainLayout = QVBoxLayout()
#
#         self.List = QListWidget()
#         self.List.addItem('a')
#         self.List.addItem('b')
#         self.List.itemDoubleClicked.connect(self.Print)
#         MainLayout.addWidget(self.List)
#
#         centralWidget.setLayout(MainLayout)
#         self.setCentralWidget(centralWidget)
#
#         self.show()
#
#     def Print(self):
#         item  = self.List.selectedItems()
#
#         print(item)

if __name__ == '__main__':
    # import sys
    #
    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())
    import sqlite3 as sq

    DB = sq.connect('FilePath.db')
    c = DB.cursor()
    # try:
    #     c.execute("create table Path(path);")
    # except: pass
    #
    # c.execute("insert into Path values(?);", ["C//Users/yudai/Dropbox"])
    # DB.commit()
    # DB.close()

    c.execute("select * from FilePath")
    for row in c:
        print(row[0])