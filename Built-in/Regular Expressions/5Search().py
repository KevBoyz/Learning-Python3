import re

reg = re.compile(r'(\d\d)-(9\d\d\d\d)-(\d\d\d\d)')

test = reg.search('88-99400-7812')  # now test is instance of Match

# Match methods

print(test.group(1))  # Group 1, 2, 3
print(test.group(2))
print(test.group(3))

print(test.group())  # No value or 0 return all groups

print(test.groups())  # Return tuple with groups
