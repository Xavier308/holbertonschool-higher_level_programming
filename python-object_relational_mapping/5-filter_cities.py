#!/usr/bin/python3
"""
This script lists all cities from a specified state in the database
'hbtn_0e_4_usa' using SQLAlchemy, an ORM tool.
"""
import MySQLdb
from sys import argv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref="state")


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))


def list_cities_by_state(username, password, dbname, state_name):
    # Create engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database
    states = session.query(State).filter(State.name == state_name).all()
    cities_list = []
    for state in states:
        cities = session.query(City.name).filter(City.state_id == state.id).order_by(City.id).all()
        for city in cities:
            cities_list.append(city[0])

    if cities_list:
        print(", ".join(cities_list))
    else:
        print()

    session.close()


if __name__ == "__main__":
    if len(argv) == 5:
        list_cities_by_state(argv[1], argv[2], argv[3], argv[4])
