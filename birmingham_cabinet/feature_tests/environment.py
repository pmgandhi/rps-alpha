import contextlib

from birmingham_cabinet.base import Base, local_unix_socket_engine

def after_feature(context, feature):
    with contextlib.closing(local_unix_socket_engine.connect()) as conn:
        trans = conn.begin()
        for table in reversed(Base.metadata.sorted_tables):
            conn.execute("truncate table {table_name}".format(table_name=table.name))
        trans.commit()