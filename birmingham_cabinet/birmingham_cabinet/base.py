from os import environ
import getpass

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

local_unix_socket_engine = create_engine(
        "postgresql+psycopg2://"
        "{user}@".format(user=getpass.getuser())
        "/rps_alpha"
        "?host=/var/run/postgresql")

def make_session():
        Session = sessionmaker()
        Session.configure(bind=local_unix_socket_engine)
        return Session()
