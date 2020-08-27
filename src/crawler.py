﻿import requests
import datetime
import logging
import json


class Crawler():
    def __init__(self, endpoint):
        self._endpoint = endpoint
        self._logger = logging.getLogger("Crawler")

    def GetHistory(self, StockNo, Year, Month):
        ts = str(datetime.datetime.now().timestamp()).split('.')[0]
        
        self._logger.debug(f"timestamp = {ts}")

        dateStr = f'{Year}{Month:02d}'
        url = f'{self._endpoint}?response=json&date={dateStr}&stockNo={StockNo}&_={ts}'
        requestData = {'response' :'json',
                        'date':dateStr,
                        'stockNo':StockNo,
                        '_':ts}
        print(requestData)
        response = requests.get(self._endpoint,requestData)
        
        s = response.text
        data = json.loads(s)

        print(data)
        return data
