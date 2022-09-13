#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306, charset="utf8")
    
    cur = db.cursor()
    
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states on cities.state_id = states.id"
                ) # HERE I have to know SQL to grab all states in my database
    
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
