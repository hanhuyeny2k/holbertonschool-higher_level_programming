#!/usr/bin/python3
# Take an argument and displays all values in the states table match the name
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name_search = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=db_name)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                where binary name = %s
                ORDER BY id ASC""", (state_name_search,))
    for row in cur.fetchall():
        print(row)
    db.close()
