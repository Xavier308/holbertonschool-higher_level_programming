#!/usr/bin/python3
"""
Displays all cities from the database `hbtn_0e_14_usa` by state.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    session = Session()

    # Query all cities joined with states, order by cities.id
    result = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
