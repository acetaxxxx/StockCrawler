import pymongo
from pymongo.collection import Collection


class StockRepository():
    def __init__(self, connection_Str):
        client = pymongo.MongoClient(connection_Str)
        self._db = client.stock

    def GetStockHistory(self):
        return StockCollection(self._db, 'DailyHistory')

    def GetMonitorStock(self):
        return StockCollection(self._db, 'MonitorStock')


class StockCollection():
    def __init__(self, db, collection_Name):
        self._collection = Collection(db, name=collection_Name)

    def Select(self, condition=None, filter=None):
        if condition is None:
            return self._collection.find()
        return self._collection.find(condition)

    def Insert(self, item=None):
        if item is None:
            return False
        self._collection.insert_one(item)
