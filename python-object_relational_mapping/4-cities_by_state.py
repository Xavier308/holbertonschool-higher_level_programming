#!/usr/bin/python3
"""
Module to list all cities from the database hbtn_0e_4_usa using SQLAlchemy
"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    cities = relationship("City", back_populates="state")


class City(Base):
    """
    Represents a city for a MySQL database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")


def list_cities(username, password, dbname):
    """
    Connects to the database and lists all cities sorted by id.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.
    """
    # Create a connection string and engine
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(conn_str)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all cities and their states, ordered by city id
    cities = (
        session.query(City)
        .join(State)
        .order_by(City.id.asc())
        .all()
    )

    # Print each city with its state
    for city in cities:
        print(f"({city.id}, '{city.name}', '{city.state.name}')")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_cities(username, password, dbname)
