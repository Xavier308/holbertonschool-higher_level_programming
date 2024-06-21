#!/usr/bin/python3
"""
Module to list all cities from the database hbtn_0e_4_usa using SQLAlchemy
"""
import MySQLdb
from sys import argv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref="state")


class City(Base):
    """
    Represents a city for a MySQL database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))


def list_cities(username, password, dbname):
    # Create engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database
    cities = session.query(City.id, City.name, State.name).join(State).order_by(City.id).all()
    for city_id, city_name, state_name in cities:
        print(f"({city_id}, '{city_name}', '{state_name}')")

    session.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_cities(argv[1], argv[2], argv[3])
