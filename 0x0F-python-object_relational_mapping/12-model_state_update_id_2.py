#!/usr/bin/python3
# change the name of States object from Arizona to New Mexico

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

    session.query(State).\
        filter(State.id == '2').\
        update({State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()
    session.close()
