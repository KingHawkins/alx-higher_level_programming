#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    conn = db.cursor()
    conn.execute("SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC;")
    data = conn.fetchall()
    for key in data:
        print(key)
    db.close()
