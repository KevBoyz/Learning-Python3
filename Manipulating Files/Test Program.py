import os, shutil


def clear():
    os.chdir('..')
    if os.path.isdir('folder'):
        shutil.rmtree('folder')


if not os.path.isdir('folder'):
    os.mkdir('folder')

os.chdir('folder')

if os.path.isfile('text.txt'):
    os.remove('text.txt')

with open('text.txt', 'w') as text:
    text.write()

if len(os.listdir()) < 3:
    for c in range(0, 3):
        shutil.copy('text.txt', f'text{c+1}.txt')

print(os.listdir())

# clear()  # Uncomment to test