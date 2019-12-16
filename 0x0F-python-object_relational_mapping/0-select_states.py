#!/usr/bin/python3
import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_passwd = sys.argv[2]
db_name = sys.argv[3]

db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=mysql_username,
                     passwd=mysql_passwd,
                     db=db_name)

cur = db.cursor()
cur.execute("SELECT * FROM states")
for row in cur.fetchall():
    print(row[0], ",", row[1])
