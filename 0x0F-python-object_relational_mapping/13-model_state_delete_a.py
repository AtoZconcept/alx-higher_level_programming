#!/usr/bin/python3
"""
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""


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

    states_with_a = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id).all()
    for state in states_with_a:
        session.delete(state)
    session.commit()

    session.close()
