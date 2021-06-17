import click, zipfile, os, os.path


# Groups


@click.group('zip', help='Zip tools')
def Zip():
    ...


@Zip.command(help='Compress all path FILES in zip')
@click.argument('path', type=click.Path(exists=True))
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
