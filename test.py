if __name__ == '__main__':
    import DataBase

    test = DataBase.PaperDataBase()
    # test.c.execute("insert into Journal values('test','test','test','test','test','test','test','test')")
    # test.db.commit()
    test.c.execute("delete from Journal")
    test.db.commit()
    for row in test.c.execute('select * from Journal'):
        print(row)