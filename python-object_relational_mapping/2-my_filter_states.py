#!/usr/bin/python3
"""Filter states by user input using direct SQL queries"""


import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    cursor = db.cursor()

    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(state_name)

    cursor.execute(query)

 
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
