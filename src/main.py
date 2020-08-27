import crawler

s = crawler.Crawler('https://www.twse.com.tw/exchangeReport/STOCK_DAY')
s.GetHistory(2305,2020,2)