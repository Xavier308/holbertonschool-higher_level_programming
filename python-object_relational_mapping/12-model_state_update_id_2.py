#!/usr/bin/python3
"""
Changes the name of the State with id = 2 to 'New Mexico' in
the database `hbtn_0e_6_usa`.
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

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Find the State with id = 2
    state_to_update = session.get(State, 2)

    # Check if the state was found and update it
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
