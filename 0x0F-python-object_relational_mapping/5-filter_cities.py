#!/usr/bin/python3

"""Takes in the name of a state as an argument and lists all cities of\
        that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    conn = db.cursor()
    conn.execute("""SELECT cities.name\
                  FROM states, cities\
                  WHERE states.name = %s;""", (sys.argv[4],))
    states = conn.fetchall()
    print(", ".join([state[0] for state in states]))
    db.close()
