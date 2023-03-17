#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    conn = db.cursor()
    conn.execute("SELECT * FROM states where name LIKE 'N%' ORDER BY id ASC;")
    data = conn.fetchall()
    for key in data:
        print(key)
    db.close()
