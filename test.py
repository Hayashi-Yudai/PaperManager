if __name__ == '__main__':
    import WebSCraping
    import PDFParse
    import DataBase
    import sqlite3
    from pdfminer.layout import LTTextBoxHorizontal

    # layout = PDFParse.PDFAnalyze("C://Users/yudai/Dropbox/takahashi_lab/paper/Cu2OSeO3/PhysRevLett.109.037603.pdf").get_PDFLayout(0)
    # for l in layout:
    #     if isinstance(l, LTTextBoxHorizontal) and 'PhysRevLett' in l.get_text():
    #         print(l.get_text())

    # soup = WebSCraping.PhysRev('https://journals.aps.org/prb/abstract/10.1103/PhysRevB.95.174407').get_Abst()
    # print(soup)
    # abstract  = soup.find('section', {'class' : 'article open abstract'})
    #
    # print(abstract.find('div', {'class' : 'content'}).get_text())
    # FileName = 'PhysRevB.85.220406'
    # URL = 'https://journals.aps.org/prb/abstract/10.1103/PhysRevB.85.220406'
    # DataBase.PaperDataBase().RegistDB(FileName, URL)
    # path = 'C://Users/yudai/Dropbox/takahashi_lab/paper/Cu2OSeO3/PhysRevLett.109.037603.pdf'
    # pdf = PDFParse.PhysRev(path).get_URL()
    # print(pdf)


    db = sqlite3.connect('JData.db')
    c = db.cursor()
    # c.execute('delete from Journal')
    # db.commit()
    c.execute("select * from Journal")

    for row in c:
        print(row)