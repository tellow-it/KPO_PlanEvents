from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:DtnthDgjkt2002@localhost/kpo',
                       echo=True)

Base = declarative_base()

Session = sessionmaker()
