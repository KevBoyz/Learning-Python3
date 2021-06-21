import click, zipfile, os, os.path


# Groups


@click.group('zip', help='Zip tools')
def Zip():
    ...


@Zip.command(help='Compress all path FILES in zip')
@click.argument('path', type=click.Path(exists=True))
@click.option('-fn', type=click.STRING, default='ZipFile', help='Zip file name')
@click.option('-v', '--verbose', is_flag=True, default=False, show_default=True, help='Verbose mode')
def compress(path, fn, v):
    os.chdir(path)
    cwd = os.getcwd()
    files = os.listdir()
    if len(files) <= 0:
        print(f'Files founded: {files}') if v else None     # Verbose
        raise Exception('Error, no files or directories founded in this path')
    if not fn.rfind('.zip'):
        fn += '.zip'
    zip = zipfile.ZipFile(fn, 'w')
    files.remove(fn)
    with click.progressbar(range(len(files))) as p:
        for c in p:
            if not os.path.isdir(files[c]):
                zip.write(files[c], compress_type=zipfile.ZIP_DEFLATED)
                print('Compressing:', files[c]) if v else None  # Verbose
                files.remove(files[c])
            if os.path.isdir(files[c]):
                os.chdir(files[c])
                try:
                    for file in os.listdir():
                        if not os.path.isdir(file) and file not in zip.namelist():
                            zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
                        elif os.path.isdir(file):
                            os.chdir(file)
                            for file in os.listdir():
                                if not os.path.isdir(file) and file not in zip.namelist():
                                    zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
                            os.chdir('..')
                except:
                    continue
                os.chdir(cwd)
    click.secho(f'{len(zip.namelist())} files was compressed in {fn}', fg='green')
