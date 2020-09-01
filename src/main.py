from crawler import Crawler
import logging
import configparser
from repo.stockHistory import StockRepository
import datetime
import time


def ExtractItem(list_of_data):
    dictItem = dict()
    tradeDate = str(list_of_data[0]).split('/')
    dictItem['TradeDate'] = datetime.datetime(int(tradeDate[0]) + 1911,
                                              month=int(tradeDate[1]),
                                              day=int(tradeDate[2]))

    dictItem['TotalTradeAmount'] = int(str(list_of_data[1]).replace(',', ''))
    dictItem['TotalAmount'] = float(str(list_of_data[2]).replace(',', ''))
    dictItem['OpenPrice'] = float(str(list_of_data[3]).replace(',', ''))
    dictItem['HightPrice'] = float(str(list_of_data[4]).replace(',', ''))
    dictItem['LowPrice'] = float(str(list_of_data[5]).replace(',', ''))
    dictItem['ClosePrice'] = float(str(list_of_data[6]).replace(',', ''))
    dictItem['DiffPrice'] = float(str(list_of_data[7]).replace(',', ''))
    dictItem['TradeCount'] = float(str(list_of_data[8]).replace(',', ''))

    return dictItem


if __name__ == "__main__":

    ## setting
    config = configparser.ConfigParser()
    config.read("src/config.ini")

    logging.basicConfig(filename=config['DEFAULT'].get('LogPath', 'log.txt'),
                        level=logging.DEBUG)

    crawler = Crawler(config['DEFAULT'].get('BaseUrl', ''))

    historyRepo = StockRepository(config['DEFAULT']['ConnectionStr'])
    monitorStockCollect = historyRepo.GetMonitorStock()
    historyCollect = historyRepo.GetStockHistory()

    logger  = logging.getLogger('Main')

    for stockInfo in monitorStockCollect.Select():
        no = stockInfo['StockNumber']

        for year in range(2012,2021):
            for month in range(1,13):
                try:
                    historyData = crawler.GetHistory(no, year, month)
                    time.sleep(3.5)
                    for item in historyData['data']:
                        dictItem = ExtractItem(item)
                        dictItem['StockNo'] = no
                        historyCollect.InsertOrUpdate(dictItem)
                except:
                    logger.error(f'Datetime: {datetime.datetime.now()} ,stockNo :{no},year {year},month: {month} exception')
