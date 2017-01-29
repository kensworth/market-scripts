import json
import sys
from pprint import pprint

with open(sys.argv[1]) as stock_info:
    for line in stock_info:
        data = json.loads(line)
        results = data['query']['results']['quote']
        for result in results:
            pprint(result['Symbol'])

