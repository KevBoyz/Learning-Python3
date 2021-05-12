import os

'''

# os.mkdir('New Folder')
print(f'Files in this directory: {os.listdir()}')

print(f"Absolute path {os.path.abspath('.')}")

print(f"{os.path.join('Github', 'Manipulating Files', 'New Folder')}")

os.system('title Learning Python3')
'''

# Organizing Files in <New Folder>

img_types = ['.jpg', '.jpeg', '.png']
doc_types = ['.txt', '.docx', '.xls', '.ppt', '.pdf', '.doc']

n = 0


def get_ext(file):
    index = file.rfind('.')
    return file[index:].lower()


def organize(path):
    images_dir = os.path.join(path, 'Images')
    docs_dir = os.path.join(path, 'Docs')
    others_dir = os.path.join(path, 'Others')

    if not os.path.isdir(images_dir):  # os.path.exists(s)
        os.mkdir(images_dir)
    if not os.path.isdir(docs_dir):
        os.mkdir(docs_dir)
    if not os.path.isdir(others_dir):
        os.mkdir(others_dir)

    files = os.listdir(path)
    files.remove('Docs')
    files.remove('Images')
    files.remove('Others')

    for file in files:
        global n
        n += 1
        if not os.path.isdir(file):
            if get_ext(file) in img_types:
                os.rename(os.path.join(path, file), os.path.join(images_dir, file))
            elif get_ext(file) in doc_types:
                os.rename(os.path.join(path, file), os.path.join(docs_dir, file))
            elif file not in img_types and file not in doc_types:
                os.rename(os.path.join(path, file), os.path.join(others_dir, file))


print(f'Hello {os.getlogin().capitalize()}, type the way that you want organize')
test = input('Path: ')

while True:
    try:
        organize(test)
        break
    except:
        print('Error, the input is invalid. Try look a like this C:\\Users\\Folder')
        continue


input(f'<End Process> {n} files moved')