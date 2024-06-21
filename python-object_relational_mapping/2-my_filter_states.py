#!/usr/bin/python3
"""Filter states by user input using direct SQL queries with MySQLdb."""

import sys
import MySQLdb


def filter_states(username, password, dbname, state_name):
    """
    Connects to the MySQL database and prints states that match
    the user-provided state name, sorted by state ID.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.
        state_name (str): The state name to filter by.
    """
    # Define database connection parameters
    db_host = "localhost"
    db_user = username
    db_password = password
    db_name = dbname

    # Create a connection to the MySQL database
    db = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        db=db_name,
        charset="utf8"
    )

    # Create a cursor object using the cursor() method
    cursor = db.cursor()

    # Prepare SQL query to filter states safely
    query = """
        SELECT id, name
        FROM states
        WHERE name LIKE BINARY %s
        ORDER BY id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of lists.
    states = cursor.fetchall()

    # Print each state's ID and name
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
