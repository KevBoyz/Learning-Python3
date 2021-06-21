def bar_template():
    return '%(label)s  %(bar)s  %(info)s'


def get_ext(file):
    index = file.rfind('.')  # Getting the type of file
    return file[index:].lower()


def file_types():
    return {'midia': ('.png', '.jpeg', '.gif', '.bmp', '.tiff', '.svg',
                      '.mp3', '.waw', '.ogg', '.wma',
                      '.mp4', '.avi', '.wmv', '.mov', '.avchd'),
            'docs': ('.pdf', '.ppt', '.docx', '.txt', '.xls', 'doc')}


