#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database `hbtn_0e_6_usa`
and prints its ID.
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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Print the new State's id
    print(new_state.id)

    # Close the session
    session.close()
