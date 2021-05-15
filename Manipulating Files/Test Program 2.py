import os, shutil

if not os.path.isdir('ms'):
    os.mkdir('ms')
os.chdir('ms')

if len(os.listdir()) >= 1:
    for file in os.listdir():
        if os.path.isdir(file):
            shutil.rmtree(file)
        else:
            os.remove(file)

for c in range(0, 10):
    os.mkdir(f'folder{c+1}')
    for c_ in range(0, 2):
        with open(os.path.join(f'folder{c+1}', f'text{c_}.txt'), 'w') as text:
            text.write('')


