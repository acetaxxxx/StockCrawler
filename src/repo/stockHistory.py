import pymongo
from pymongo.collection import Collection
import logging


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
        self._logger = logging.getLogger(f'StockCollection_{collection_Name}')

    def Select(self, condition=None, filter=None):
        if condition is None:
            return self._collection.find()
        return self._collection.find(condition)

    def Insert(self, item=None):
        if item is None:
            return False
        self._logger.debug(f'insert {item}')
        self._collection.insert_one(item)

    def InsertOrUpdate(self, item=None):
        if item is None:
            return False
        condition = dict({
            'TradeDate': item['TradeDate'],
            'StockNo': item['StockNo']
        })
        temp = self.Select(condition=condition)

        if temp.count() < 1:
            return self.Insert(item)
        self._logger.info(f'item {item} is inserted.')
        return True  ## add update