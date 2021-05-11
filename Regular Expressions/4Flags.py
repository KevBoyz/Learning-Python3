import re

target = 'KELLy is a Python developer at a PYnative. kelly loves ML and AI'

print(re.findall(r'kelly', target, re.I))  # Long syntax: re.IGNORECASE

result = re.search(r".+", target, re.S)  # Log syntax: re.DOTALL
print(result.group())
