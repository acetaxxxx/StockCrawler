import crawler
import logging
import configparser
from repo.stockHistory import StockHistory



if __name__ == "__main__":
    ## setting
    config = configparser.ConfigParser()
    config.read("src/config.ini")


    logging.basicConfig(filename=config['DEFAULT'].get('LogPath','log.txt'),level=logging.DEBUG)

    s = crawler.Crawler(config['DEFAULT'].get('BaseUrl',''))
    f = s.GetHistory(2305,2020,2)
    t = StockHistory(config['DEFAULT']['ConnectionStr'])