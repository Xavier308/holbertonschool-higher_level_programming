#!/usr/bin/python3
"""
Module to list all cities from the database hbtn_0e_4_usa using SQLAlchemy
"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    Defines a relationship to the City model,
    which represents cities within the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    cities = relationship("City", back_populates="state")


class City(Base):
    """
    Represents a city for a MySQL database.
    Linked to a State via a foreign key to
    represent the state-city relationship.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")


def list_cities(username, password, dbname):
    """
    Connects to the database using SQLAlchemy and prints details of all cities,
    sorted by city ID.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.
    """
    # Create a connection string and engine
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(conn_str)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Perform the query and fetch all results
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print each city's ID, name, and associated state's name
    for city in cities:
        print(f"({city.id}, '{city.name}', '{city.state.name}')")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
