import logging
from bson import Code
import pymongo
from pymongo.errors import AutoReconnect


class Database(object):
    def __init__(self, host, port, name):
        self._mongo = pymongo.MongoClient(host, port)
        self.name = name

    def alive(self):
        return self._mongo.alive()

    @property
    def mongo_database(self):
        return self._mongo[self.name]


class MongoDriver(object):
    def __init__(self, collection):
        self._collection = collection
        self.sort_options = {
            "ascending": pymongo.ASCENDING,
            "descending": pymongo.DESCENDING
        }

    def _apply_sorting(self, cursor, key, direction):
        if direction not in self.sort_options.keys():
            raise InvalidSortError(direction)

        cursor.sort(key, self.sort_options[direction])

    def find_one(self, query):
        return self._collection.find_one(query)

    def find(self, query, sort, limit):
        cursor = self._collection.find(query)
        self._apply_sorting(cursor, sort[0], sort[1])
        if limit:
            cursor.limit(limit)
        return cursor

    def save(self, obj, tries=3):
        try:
            self._collection.save(obj)
        except AutoReconnect:
            logging.warning("AutoReconnect on save")
            if tries > 1:
                self.save(obj, tries - 1)
            else:
                raise


class Repository(object):
    def __init__(self, mongo_driver):
        self._mongo_driver = mongo_driver

    def _validate_sort(self, sort):
        if len(sort) != 2:
            raise InvalidSortError("Expected a key and direction")

        if sort[1] not in ["ascending", "descending"]:
            raise InvalidSortError(sort[1])

    def find(self, query, sort=None, limit=None):
        if not sort:
            sort = ["_timestamp", "ascending"]

        self._validate_sort(sort)

        return self._mongo_driver.find(query.to_mongo_query(), sort, limit)

    def save(self, obj):
        obj['_updated_at'] = timeutils.now()
        self._mongo_driver.save(obj)


class InvalidSortError(ValueError):
    pass
