import grequests
import sys

def construct_url(symbol_list):
    url = 'https://query.yahooapis.com/v1/public/yql';
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    data = 'select * from yahoo.finance.historicaldata where symbol in (' + \
        symbol_list + ') and startDate="' + start_date + '" and endDate="' + \
        end_date + '"&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json'
    constructed_url = url + '?q=' + data
    return constructed_url

def batch_stocks():
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
    return batches

def driver():
    batches = batch_stocks()
    urls = []
    for batch in batches:
        symbol_list = ', '.join('"{0}"'.format(ticker) for ticker in batch)
        constructed_url = construct_url(symbol_list)
        urls.append(constructed_url)
    rs = [grequests.get(url) for url in urls]
    responses = grequests.map(rs)
    name = 'MarketQuery-s' + sys.argv[1] + 'e' + sys.argv[2] + '.json'
    f = open(name, 'w')
    for response in responses:
        f.write(response.text + '\n')

if __name__ == "__main__":
    driver()
