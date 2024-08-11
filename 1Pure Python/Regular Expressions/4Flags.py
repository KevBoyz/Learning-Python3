import re

target = 'KELLy is a Python developer at a PYnative. kelly loves ML and AI '

print(re.findall(r'kelly', target, re.I))  # Long syntax: re.IGNORECASE

result = re.search(r".+", target, re.S)  # Log syntax: re.DOTALL
print(result.group())


regex = re.compile(r'''
        (\(\d{2}\)) (-|\s|\.)    # DDD
        (9-\d{4}) (-|\s|\.)      # Number n1
        (\d{4})                  # Number n2 
        ''', re.VERBOSE | re.IGNORECASE)

print(regex.search('!#(99) 9-9289.2276#!').group())
