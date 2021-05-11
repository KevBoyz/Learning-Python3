import re

# \A \b \B \d \D \w \W \Z


for letter in re.findall('\Athe', 'the sun'):  # Search the value in start of string
    print(f'{letter}', end='')
print()


for letter in re.findall('sum\Z', 'the sum'):  # All backspace or null characters
    print(f'{letter}', end='')
print()


for letter in re.compile(r'\bX\b').findall('X + Y'):  # Match if defined characters are in start or end of word (\B)
    print(f'{letter}', end='')
print()


for letter in re.findall('\d', '12456'):  # all numbers
    print(f'{letter}', end='')
print()


for letter in re.findall('\D', 'H1e2l3l4o W5o6r8l7d'):  # All non numbers
    print(f'{letter}', end='')
print()


for letter in re.findall('\s', 'Hello World'):  # All backspace or null characters
    print(f'{letter}', end='')
print()


for letter in re.findall('\S', 'Hello World'):  # All non backspace or non null characters
    print(f'{letter}', end='')
print()