import click, zipfile, os, os.path


@click.group('fh', help='Files manipulation')
def fh():
    ...



@fh.command(help='Create a zipfile with all files in one path')
@click.argument('path', type=click.Path(exists=True))
@click.option('-fn', type=click.STRING, default='ZipFile', help='Zip file name')
def zip(path, fn):
    os.chdir(path)
    files = os.listdir()
    if len(files) <= 0:
        raise Exception('Error, no files or directories founded in this path')
    zip = zipfile.ZipFile(fn + '.zip', 'w')
    with click.progressbar(range(len(files))) as p:
        for c in p:
            if files[c] != fn + '.zip' and files[c] not in zip.namelist():
                zip.write(files[c], compress_type=zipfile.ZIP_DEFLATED)
    click.secho(f'{len(zip.namelist())} files was compressed in {fn}', fg='green')