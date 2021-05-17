import zipfile

zip = zipfile.ZipFile('zip_archive.zip', 'w')  # Creating zip file
zip.write('Directores.py', compress_type=zipfile.ZIP_DEFLATED)  # Add file to

print(zip.namelist())  # Files in zip file

# Getting information

info = zip.getinfo('Directores.py')  # creating new object GetInfo
# Obj attributes
print(info.file_size)       # Original size (in bytes)
print(info.compress_size)   # After compact size


zip.extractall('..')  # Extracting all files
# zip.extract('file', 'path')  # Extracting one file