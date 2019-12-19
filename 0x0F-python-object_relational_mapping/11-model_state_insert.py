#!/usr/bin/python3
# add the States object "Louisiana" to the database hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usr, passwd, db_name, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    row = State(name='Louisiana')
    session.add(row)
    session.commit()
    states = session.query(State).filter(State.name == 'Louisiana').first()
    if states:
        print("{}".format(states.id))
    session.close()
