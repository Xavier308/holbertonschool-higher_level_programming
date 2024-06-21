#!/usr/bin/python3
"""
Module to list all states where name matches the argument from the
database hbtn_0e_0_usa using SQLAlchemy, safe from SQL injections.
"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


def list_states_by_name(username, password, dbname, state_name):
    """
    Connects to the database and prints all states where the name matches
    the provided argument, sorted by id, safe from SQL injections.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.
        state_name (str): The name of the state to search for.
    """
    # Create a connection string and engine
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(conn_str)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use parameterized query to prevent SQL injection
    states = (
        session.query(State)
        .filter(State.name == state_name)
        .order_by(State.id.asc())
        .all()
    )

    # Print each state
    for state in states:
        print(f"({state.id}, '{state.name}')")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        list_states_by_name(username, password, dbname, state_name)
