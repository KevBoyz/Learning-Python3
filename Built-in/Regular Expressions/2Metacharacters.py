import re


def new():
    print('')


# The metacharacters are: (), [], {}, ?, ., ^, +, *, $, \, |


# square brackets []
for letter in re.findall('[kevin]', 'xkxexvxixn'):
    print(letter, end='')
new()

for letter in re.findall('[^kevin]', 'xkxexvxixn'):  # ^ invert the process
    print(letter, end='')
new()

for number in re.findall('[0-9][a-z]', '1xkxex2vxixn3'):  # find all values in intervale
    print(number, end='')
new()



# parentheses ()
for letter in re.findall('(ke)(vin)', 'kevin'):  # set subgroups
    print(letter, end='')
new()

# Bonus Example
print(re.search(r'k(ev)+in', 'Kevevevin', re.IGNORECASE).group())


# keys {}
# ^
for letter in re.findall('ke{1, 3}vin', 'keeevin'):  # {min, max}, {min,}, {, max}
    print(letter, end='')
new()

# Bonus Example
print('test', end=' ')
for letter in re.findall('k{2, 5}evin?', 'kkkkevin'):  # ? at end turn regex non greedy
    print(letter, end='')
new()


# Point .
for letter in re.findall('.....', 'kevin'):  # . = any character
    print(letter, end='')
new()



# dollar $
for letter in re.findall('n$', 'kevin'):  # $ verify the last character
    print(letter, end='')
new()



# ^
for letter in re.findall('^k', 'kevin'):  # verify the firs character
    print(letter, end='')
new()



# star *
for letter in re.findall('ke*vin', 'kvin'):  # * x character zero or more times
    print(letter, end='')
new()



# plus +
for letter in re.findall('ke+vin', 'keeevin'):  # + x character one or more times
    print(letter, end='')
new()



# interrogation point ?
for letter in re.findall('ke?vin', 'kevin'):  # ? x character one or zero times
    print(letter, end='')
new()


