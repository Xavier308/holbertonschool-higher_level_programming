#!/usr/bin/python3
"""filter the states by the name"""
import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect mysql server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # Create cursor object
    cursor = db.cursor()

    # Query
    query = """SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC"""
    query = query.format(state_name)
    # Execute the query
    cursor.execute(query)

    # Fetch results
    states = cursor.fetchall()

    # Loop to print the resutls
    for state in states:
        print(state)

    # Close cursor
    cursor.close()
    db.close()
