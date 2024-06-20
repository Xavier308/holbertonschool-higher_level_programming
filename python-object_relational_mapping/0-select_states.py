#!/usr/bin/python3
"""
Module to list all states from the database hbtn_0e_0_usa using SQLAlchemy.
This script takes 3 arguments: mysql username, mysql password,
and database name.
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import sys


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)


def list_states(username, password, dbname):
    """
    Connects to the database using SQLAlchemy and prints all states
    sorted by id.
    """
    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}'
        f'@localhost:3306/{dbname}'
    )
    Base = declarative_base()

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'({state.id}, {state.name})')

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
