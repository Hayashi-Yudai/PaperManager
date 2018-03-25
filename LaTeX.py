import DataBase

class LaTeX:

    def ToLaTeX(self, FileName):
        """
        Connect to LaTeX button in main.py. If cannot create TeX format, raise AssertionError
        :param FileName: File name of .pdf
        :return: String. LaTeX form reference
        """
        try:
            cursor = DataBase.PaperDataBase().c.execute("select * from Journal where FileName=" + "'" + FileName +"'")
            paper = ()
            for row in cursor:
                paper = row
                break

            authors = self.trans_author(paper[3])
            journal = paper[5]
            vol = self.trans_vol(paper[6])
            year = paper[4]

            return authors + ', ' + journal + ' ' + vol[0] + ', (' + year + ') ' + vol[1]

        except:
            raise AssertionError



    def trans_author(self, authors):
        """
        get authors separated by ',' and transform first name to initial if need
        :param authots: String separated by ';'
        :return: String
        """
        authors = authors.split(';')
        for i in range(len(authors)):
            if '.' not in authors[i]:
                authors[i] = authors[i].split(' ')
                authors[i][0] = authors[i][0][0]
                authors[i] = '. '.join(authors[i])
        last_author = authors[-1]
        author = ', '.join(authors[:-1])

        return author + ' and ' + last_author



    def trans_vol(self, vol):
        """
        vol -> \textbf{vol}
        page -> page
        :param vol: String separated by ';'
        :return: List
        """
        vol = vol.split(';')
        vol[0] = '\\textbf{' + vol[0] + '}'

        return vol