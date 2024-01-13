#!/usr/bin/python3
"""
script that changes the name of a State
object from the database hbtn_0e_6_usa
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

    states = session.query(State).filter_by(id=2).first()
    if states:
        states.name = "New Mexico"
        session.commit()
    else:
        print("State with id = 2 not found")

    session.close()
