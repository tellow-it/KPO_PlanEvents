from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:DtnthDgjkt2002@localhost/kpo_new',
                       echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()