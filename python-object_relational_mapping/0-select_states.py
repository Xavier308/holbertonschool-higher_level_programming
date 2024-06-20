#!/usr/bin/python3
"""
Module to list all states from the database hbtn_0e_0_usa.
This script takes 3 arguments: mysql username, mysql password,
and database name.
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed.
"""

import MySQLdb
import sys


def list_states(username, password, dbname):
    """
    Connects to the database and prints all states sorted by id.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
