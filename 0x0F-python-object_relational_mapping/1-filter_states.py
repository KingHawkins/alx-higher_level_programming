#!/usr/bin/python3
"""selects names that begin with capital N"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    conn = db.cursor()
    conn.execute("""SELECT * FROM states\
                 WHERE name\
                 COLLATE utf8mb4_bin LIKE 'N%'\
                 ORDER BY id ASC;""")
    data = conn.fetchall()
    for key in data:
        print(key)
    db.close()
