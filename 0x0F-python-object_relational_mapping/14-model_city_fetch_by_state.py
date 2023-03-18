#!/usr/bin/python3

"""deletes all State object with the name\
        with an `a` from database hbtn_0e_6_usa
"""

import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (session.query(State, City)
              .filter(State.id == City.state_id).order_by(City.id).all())
    for state, city in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
