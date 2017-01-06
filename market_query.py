import requests
import json

def query_stock(symbol_list):
    url = 'https://query.yahooapis.com/v1/public/yql';
    start_date = '2017-01-04'
    end_date = '2017-01-05'
    data = 'select * from yahoo.finance.historicaldata where symbol in (' + \
        symbol_list + ') and startDate="' + start_date + '" and endDate="' + \
        end_date + '"&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json'
    constructed_url = url + '?q=' + data

    response = requests.get(constructed_url)
    print constructed_url
    print response.text

def iterate_stocks():
    f = open('nasdaqlisted.txt')
    lines = f.readlines()[1:-1]
    tickers = []
    batches = []
    for line in lines:
        ticker = line.split('|')[0]
        tickers.append(ticker)
    for i in range(len(tickers)):
        if i % 100 == 0:
            batches.append([])
        batches[-1].append(tickers[i])
    for batch in batches:
        symbol_list = ', '.join('"{0}"'.format(ticker) for ticker in batch)
        query_stock(symbol_list)

iterate_stocks()
