import sqlite3


class SqlConnection:

    def __init__(self):
        conn = sqlite3.connect(r'E:\Roy\Projects\Standarto\movies.db')

        cur = conn.cursor()
        cur.execute("SELECT * FROM movies")

        rows = cur.fetchall()

        for row in rows:
            print(row)

        #cur.execute('SELECT * FROM movies')

        #print(cur.fetchall())

    #sql_fetch(con)

# c.execute("""CREATE TABLE moveis (
#            tconst text,
#            averageRating real,
#            numVotes integer,
#            startYear integer,
#            geners text
#            )""")
