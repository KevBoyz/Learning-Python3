import re

if re.search('Kevin', 'Where is Kevin?') is not None:  # Simple use of RegExp
    print('Kevin has founded in string, process done')
else:
    print('Error value not found')


if re.search('\d\dKe+vin', '94Keeeevin'):  # \d == 0-9, e+ = 'e' 1 or more times
    print('Kevin has founded successfully.')
else:
    print('Why you remove me from string?')
