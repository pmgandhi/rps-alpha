from birmingham_cabinet.models import *
from birmingham_cabinet.base import Base, local_unix_socket_engine

def after_feature(context, feature):
    Base.metadata.drop_all(local_unix_socket_engine)
    Base.metadata.create_all(local_unix_socket_engine)