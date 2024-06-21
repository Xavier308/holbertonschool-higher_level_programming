#!/usr/bin/python3
"""Filter states by user input using direct SQL queries with MySQLdb."""

import sys
import MySQLdb

if __name__ == "__main__":

    # Read command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Establish a database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # Initialize a cursor for executing queries
    cursor = db.cursor()

    # Define a SQL query to retrieve states matching the user input
    query = """
    SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC
    """
    # Execute the SQL query using safe parameter substitution
    cursor.execute(query, (state_name,))

    # Retrieve and print all records from the query result
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Clean up: close the cursor and the database connection
    cursor.close()
    db.close()
