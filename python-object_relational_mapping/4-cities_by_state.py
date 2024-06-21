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
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")


def list_cities(username, password, dbname):
    """
    Connects to the database and prints all cities, sorted by city id,
    using direct execution of SQL via SQLAlchemy's execute method.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.
    """
    # Create a connection string and engine
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(conn_str)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use the execute method to perform a raw SQL query safely
    query = text(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    result = session.execute(query).fetchall()

    # Print each city
    for city_id, city_name, state_name in result:
        print(f"({city_id}, '{city_name}', '{state_name}')")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
