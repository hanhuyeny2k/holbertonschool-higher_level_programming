#!/usr/bin/python3
# print the States with the name passed as argument from the database

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name_search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usr, passwd, db_name, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        if state.name == state_name_search:
            print("{}".format(state.id))
            break
    if state.name is None or state.name != state_name_search:
        print("Not found")
    session.close()
