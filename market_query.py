import requests
import json

def query_stock():
    url = 'https://query.yahooapis.com/v1/public/yql';
    start_date = '2017-01-01'
    end_date = '2017-01-06'
    symbol_list = '"GOOG"'
    data = 'select * from yahoo.finance.historicaldata where symbol in (' + \
        symbol_list + ') and startDate="' + start_date + '" and endDate="' + \
        end_date + '"&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json'
    constructed_url = url + '?q=' + data

    response = requests.get(constructed_url)
    print response.text

def iterate_stocks():
    f = open('nasdaqlisted.txt')
    lines = f.readlines()[1:-1]
    for line in lines:
        ticker = line.split('|')[0]
        print ticker

iterate_stocks()
