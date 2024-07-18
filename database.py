from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    'postgresql://eauoymizingrlv:d35616e35c444139ca513c8ff9c4c014f678d7fb6d052f90a43b29e54b658b64@ec2-52-30-75-37.eu-west-1.compute.amazonaws.com:5432/d9nddjh5gs4sao',
    echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
