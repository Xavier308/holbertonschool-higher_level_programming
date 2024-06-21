#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
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

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for all State objects containing 'a' and delete them
    session.query(State) \
           .filter(State.name.like('%a%')) \
           .delete(synchronize_session='fetch')

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
