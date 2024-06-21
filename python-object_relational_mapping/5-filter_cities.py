import MySQLdb
import sys


def list_cities_by_state(username, password, dbname, state_name):
    """
    Connects to the MySQL database and prints names of all cities from
    a specified state, sorted by city ID.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.
        state_name (str): The name of the state to search for cities.
    """
    # Define database connection parameters
    db_host = "localhost"
    db_user = username
    db_password = password
    db_name = dbname
    db_port = 3306  # Specify the MySQL port

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        db=db_name,
        port=db_port  # Include the port in the connection
    )
    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to find the state ID
    cursor.execute("SELECT id FROM states WHERE name = %s", (state_name,))
    state_id = cursor.fetchone()

    # If a state was found, retrieve cities
    if state_id:
        state_id = state_id[0]
        # Define the SQL query and parameters
        sql_query = "SELECT name FROM cities WHERE state_id = %s ORDER BY id"
        params = (state_id,)

        # Execute the SQL query using safe parameter substitution
        cursor.execute(sql_query, params)
        cities = cursor.fetchall()
        # Print cities if any are found
        if cities:
            print(", ".join(city[0] for city in cities))
        else:
            print("No cities found for this state.")
    else:
        print("State not found.")

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        # Extract command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]

        # Call the function with the unpacked arguments
        list_cities_by_state(username, password, dbname, state_name)
