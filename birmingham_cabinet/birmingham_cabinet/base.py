from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("postgresql+psycopg2://vagrant@/rps_alpha?host=/var/run/postgresql")

def make_session():
	Session = sessionmaker()
	Session.configure(bind=engine)
	return Session()