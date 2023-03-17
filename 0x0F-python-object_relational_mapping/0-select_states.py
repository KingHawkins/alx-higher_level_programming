#!/usr/bin/python3

"""selects all from a table"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    data = cursor.fetchall()

    for key in data:
        print(key)

    db.close()
