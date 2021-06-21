import click, zipfile, os, os.path
from re import search


# Groups


@click.group('zip', help='Zip tools')
def Zip():
    ...


@Zip.command(help='Compress all path FILES in zip')
@click.argument('path', metavar='<path>', type=click.Path(exists=True))
@click.option('-fn', type=click.STRING, default='ZipFile', help='Zip file name')
@click.option('-v', is_flag=True, default=True, show_default=True, help='Verbose mode')
def compress(path, fn, v):
    os.chdir(path)
    arch = 0
    if fn.rfind('.zip'):
        fn += '.zip'
    zip = zipfile.ZipFile(fn, 'w')
    print(f'Compacting archives, please wait...')
    print() if v else None
    print('  - - Process list - -') if v else None
    for folder, sub_folders, files in os.walk('.'):
        for file in files:
            if file != fn and file and file not in zip.namelist():
                print(f'Compacting: {file}') if v else None
                zip.write(os.path.join(folder, file),
                          os.path.relpath(os.path.join(folder, file), '.'),
                          compress_type=zipfile.ZIP_DEFLATED)
                arch += 1
    print() if v else None
    print(f'process completed, {arch} files compacted')
    zip.close()


@Zip.command()
@click.argument('path', metavar='<path>', type=click.Path(exists=True))
@click.argument('fn', metavar='<file_name>', type=click.STRING)
@click.option('-v', '-verbose', is_flag=True, default=False, show_default=True, help='Verbose mode')
def extract(path, fn, v, ex=0):
    os.chdir(path)
    if fn.rfind('.zip'):
        fn += '.zip'
    assert zipfile.is_zipfile(fn), f'Assertion error, can\'t find <file> on <path>'
    zip = zipfile.ZipFile(fn, 'r')
    list = zip.namelist()
    click.secho(f'{len(list)} Files founded in {fn}') if v else None    # Verbose
    click.secho(f'{list}\n') if v else None                            # Verbose
    assert len(list) >= 0, f'Assertion error, <file> is empty or can\'t be readied>'
    with click.progressbar(range(len(zip.namelist()))) as p:
        for f in p:
            click.secho(f' - Extracting {list[f]}') if v else None       # Verbose
            try:
                zip.extract(list[f])
                ex += 1
            except Exception as e:
                print(e) if v else None
    zip.close()
    click.secho(f'{ex} files extracted')




