#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=db_name,
                         charset="utf8")

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities, states
                WHERE states.id = cities.state_id AND
                binary states.name = %s
                ORDER BY cities.id ASC""", (state_name,))
    print(", ".join([row[0] for row in cur.fetchall()]))
    db.close()
    cur.close()
