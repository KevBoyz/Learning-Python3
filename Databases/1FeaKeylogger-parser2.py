# This is a parser for FeaKeylogger, a browser extension
# that capture the key board on the navigator.

# It was removed from Chrome Web Store on 2022-04-28.

import json as js
from itertools import groupby

with open('log.txt', 'rb') as file:
    data = js.load(file)
    
domain = lambda x: x['url']['domain']


def input_searcher(domain_name: str):
    for key, value in groupby(data, domain):
        if key == domain_name:
            for s in list(value):
                print(f'{key}: {s["inputs"]}')


input_searcher('pt.pornhub')

