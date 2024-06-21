#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database `hbtn_0e_6_usa`.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for the first State object with the name passed as argument
    state = session.query(State).filter(State.name == state_name).first()

    # Check if the state was found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
