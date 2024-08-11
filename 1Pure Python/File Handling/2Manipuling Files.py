import os, shutil, send2trash   # Shell utilities

# Copy and Move

# shutil.copy(os.path.join('nice.txt'), os.path.join('..', 'nice2.txt'))  # Actual path, path to copy
# shutil.copytree(os.path.join('.'), os.path.join('..', 'Regular Expressions', 'bkp'))  # Copy the full folder
# shutil.move('Actual', 'destination')  # Move file or directory and return srt with abs path
# shutil.move('Actual', os.path.join('Destination', 'new name'))  # Moving and rename


# Removing datas permanently

# os.unlink('path')  # Remove the file permanently
# os.rmdir('path')  # Remove dir permanently, the dir need to  empty
# shutil.rmtree('path')  # Remove the folder and all files inside her


# Safe delete with send2trash

# send2trash.send2trash('file.txt')  # Send to trash, literally

'''  # Walk the directory
os.chdir('..')
for root, dirs, file in os.walk('.'):
    print(f'{root}')
    print(f'{dirs}')
    print(f'{file}')
    print('-------------------')
'''

# os.rename('file_name', 'new_name')  # Renaming files