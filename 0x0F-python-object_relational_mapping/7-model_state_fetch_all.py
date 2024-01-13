#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user_n, psswd, data_b = sys.argv[1:]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                user_n, psswd, data_b
                ),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
