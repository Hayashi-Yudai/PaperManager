import psycopg2
import os


class PaperDataBase:
    def __init__(self, dbname, user):
        self.connect = psycopg2.connect(f"dbname={dbname} user={user}")
        self.cursor = self.connect.cursor()

        self.create_table()

    def create_table(self):
        self.cursor.execute(
            "create table if not exists paper_list( \
                title varchar(100) not null, \
                authors varchar(200), \
                journal_name varchar(100), \
                keywords varchar(200), \
                path varchar(200), \
                primary key (title) \
            );"
        )

    def register(self, title, author, journal, keyword, path):
        title = title if title != '' else None
        self.cursor.execute(
            "insert into paper_list (title, authors, journal_name, keywords, path) values \
            (%s, %s, %s, %s, %s);",
            (title, author, journal, keyword, path)
        )

        self.connect.commit()
        self.connect.close()

    def search(self, title, author, journal, keyword):
        query = "select * from paper_list \
                    where title = %s; \
                "
        self.cursor.execute(query, (title,))
        result = []
        for c in self.cursor:
            result.append(c[0])

        self.connect.close()

        return result

    def search_pdf_path(self, title):
        query = "select * from paper_list \
                    where title = %s; \
                "
        self.cursor.execute(query, (title,))
        for c in self.cursor:
            result = c[-1]
            self.connect.close()

            return result


if __name__ == '__main__':
    conn = psycopg2.connect("dbname=test user=yudai")
    cur = conn.cursor()
    cur.execute("drop table paper_list;")
    conn.commit()
    conn.close()
    #cur.execute('select * from paper_list;')
    # print(cur.fetchall())
