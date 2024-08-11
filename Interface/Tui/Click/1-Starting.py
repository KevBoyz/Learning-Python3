import click

'''
@click.command()
@click.argument('name')
def live(name):
    click.echo(f'Hello {name}')


live()
'''


@click.group('cli')
def cli():
    ...


@cli.command('ls', help='Multiply numbers')
@click.argument('arg', envvar='nx', type=click.INT)  # Envvar is a system variable, in windows (set nx=0)
@click.option('-m', '-multiply+', envvar='m+', is_flag=True, help="Multiply by 2 after multiply by 3")
@click.option('-p', '-prompt', prompt=True, default=None, type=click.INT)
def def_(arg, m, p):
    if p:
        click.echo(p + 10)

    if m:
        click.echo(click.style((arg * 3) * 2, bg='black', fg='green'))
    else:
        click.echo(click.style(arg * 3, bg='black', fg='green'))


cli()
