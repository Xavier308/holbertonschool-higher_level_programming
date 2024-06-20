#!/usr/bin/python3
"""
Module to list all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


def list_states(username, password, dbname):
    """
    Connects to the database and prints all states sorted by id.
    """
    # Create a connection string and engine
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(conn_str)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and order by id
    states = session.query(State).order_by(State.id.asc()).all()

    # Print each state
    for state in states:
        print(f"({state.id}, '{state.name}')")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)
