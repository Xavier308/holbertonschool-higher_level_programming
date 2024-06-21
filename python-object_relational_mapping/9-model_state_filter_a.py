#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database `hbtn_0e_6_usa`.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Retrieve command-line arguments
    username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for all State objects containing 'a', ordered by State.id
    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)\
                    .all()

    # Print states that contain the letter 'a'
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
