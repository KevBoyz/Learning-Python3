import click, zipfile, os, os.path
from re import search


# Groups


@click.group('zip', help='Zip tools')
def Zip():
    ...


@Zip.command(help='Compress all path FILES in zip')
@click.argument('path', metavar='<path>', type=click.Path(exists=True))
@click.option('-fn', type=click.STRING, default='ZipFile', help='Zip file name')
def compress(path, fn):
    os.chdir(path)
    cwd = os.getcwd()
    files = os.listdir()
    if len(files) <= 0:
        raise Exception('Error, no files or directories founded in this path')
    zip = zipfile.ZipFile(fn + '.zip', 'w')
    with click.progressbar(range(len(files))) as p:
        for c in p:
            if files[c] != fn + '.zip' and files[c] not in zip.namelist() and not os.path.isdir(files[c]):
                zip.write(files[c], compress_type=zipfile.ZIP_DEFLATED)
            if os.path.isdir(files[c]):
                os.chdir(files[c])
                try:
                    for file in os.listdir():
                        if not os.path.isdir(file) and file not in zip.namelist():
                            zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
                except:
                    continue
                os.chdir(cwd)
    click.secho(f'{len(zip.namelist())} files was compressed in {fn}', fg='green')


@Zip.command()
@click.argument('path', metavar='<path>', type=click.Path(exists=True))
@click.argument('file', metavar='<file_name>', type=click.STRING)
@click.option('-v', '-verbose', is_flag=True, default=False, show_default=True, help='Active verbose mode')
def extract(path, file, v):
    os.chdir(path)
    assert zipfile.is_zipfile(file), f'Assertion error, can\'t find <{file}> on <{path}>'
    zip = zipfile.ZipFile(file + '.zip', 'r')
    list = zip.namelist()
    click.secho(f'{len(list)} Files founded in {file}')if v else None    # Verbose
    click.secho(f'{list}\n') if v else None                              # Verbose
    assert len(list) >= 0, f'Assertion error, <{file}> is empty or can\'t be readied>'
    fs = 0
    with click.progressbar(range(len(zip.namelist()))) as p:
        for f in p:
            fs += 1
            click.secho(f' - Extracting {list[f]}') if v else None       # Verbose
            try:
                zip.extract(list[f])
            except:
                continue
    zip.close()
    click.secho(f'{fs} files extracted')




