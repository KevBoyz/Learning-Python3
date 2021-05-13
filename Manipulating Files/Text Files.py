import os, shelve


if os.path.isfile('text.txt'):

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

else:
    print('Error, file not found')

# Working with Shelf to save variables in database

data = shelve.open('data')

cats = ['Zophie', 'Pooka', 'Simon']
data['cats'] = cats  # Look like dict syntax

print(data['cats'])