#!/usr/bin/python3

"""ython file that contains the class definition of a State\
        and an instance Base = declarative_base():
            """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newCity = City(name='San Fransisco')
    newState = State(name='California')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
