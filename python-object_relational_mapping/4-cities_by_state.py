#!/usr/bin/python3
"""
Module to list all cities from the database hbtn_0e_4_usa using direct
SQL queries with MySQLdb.
"""
import MySQLdb
import sys


def list_cities(username, password, dbname):
    """
    Connects to the MySQL database and prints details of all cities,
    sorted by city ID.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.
    """
    # Define database connection parameters
    db_host = "localhost"
    db_user = username
    db_password = password
    db_name = dbname

    db = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor object using the cursor() method
    cursor = db.cursor()

    # Execute the SQL query using the cursor object
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Print each city's ID, name, and associated state's name
    for row in results:
        print(f"({row[0]}, '{row[1]}', '{row[2]}')")

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
