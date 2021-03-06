#!/usr/bin/python3
# lists all states with a name starting with N (upper N) from the database
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states where name LIKE binary 'N%'")
    for row in cur.fetchall():
        print(row)
    db.close()
    cur.close()
