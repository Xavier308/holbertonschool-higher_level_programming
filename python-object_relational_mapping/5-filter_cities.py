#!/usr/bin/python3
"""
Lists all cities of a state passed as an argument.
"""
import MySQLdb
import sys


def list_cities(username, password, db_name, state_name):
    """
    Lists all cities of the state passed as an argument.
    """
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    # SQL query to fetch cities
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the query with parameter to avoid SQL injection
    cursor.execute(query, (state_name,))

    # Fetch all results
    cities = cursor.fetchall()

    # Format and print the result
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to list cities
    list_cities(username, password, db_name, state_name)
