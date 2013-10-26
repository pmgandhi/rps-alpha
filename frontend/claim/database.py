import pymongo


class Database(object):
    def __init__(self, host, port, name):
        self._mongo = pymongo.MongoClient(host, port)
        self.name = name

    def alive(self):
        return self._mongo.alive()

    @property
    def mongo_database(self):
        return self._mongo[self.name]
