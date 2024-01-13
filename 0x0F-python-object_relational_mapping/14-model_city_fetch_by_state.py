#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
