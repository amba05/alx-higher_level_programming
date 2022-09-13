#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], \
                         db=sys.argv[3], port=3306, charset="utf8")
    
    cur = db.cursor()
    
    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
