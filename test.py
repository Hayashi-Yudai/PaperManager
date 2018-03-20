if __name__ == '__main__':
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
    for row in c:    # import os

        print(row[0])
    #
    # os.popen('C://Users/yudai/Desktop/1310.0255.pdf')