import pymongo

class StockHistory():

    def __init__(self,connection_Str):
        client = pymongo.MongoClient(connection_Str)
        self._db = client.stock
        self._history = self._db['History']

    def Select(self):

        return self._history
    def Insert(self):
        return True