import os
from shelve import open

text = open('text.txt')
write_text = open(os.path.join('.', 'text.txt'), 'w')  # Sobrescreve o texto atual
append_text = open(os.path.join('.', 'text.txt'), 'a')

# print(read_text.readlines())

write_text.write('Hello World\n')
append_text.write('Lol')

write_text.close()
append_text.close()

print(text.read())
text.close()


# Working with Shelf to save variables in database

data = open('data')

cats = ['Zophie', 'Pooka', 'Simon']
data['cats'] = cats  # Look like dict syntax

print(data['cats'])