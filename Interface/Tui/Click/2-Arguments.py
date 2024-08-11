import click


@click.group('cli')
def cli():
    """Simple command line toll"""


@cli.command(help='Print string')
@click.argument('name', type=click.STRING, metavar='<name>')
@click.option('-t', '-times', type=click.IntRange(min=1, max=10, clamp=True), default=1, show_default=True)  # nargs=2
def name(name, times):
    """<name> = Common string

    Usage Example:
    cli name -t 5 Kevin

    \b
    This is a very long second paragraph and as you
        can see wrapped very early in the source text
        but will be rewrapped to the terminal width in
        the final output.
    """
    for c in range(0, times):
        print(f'{c}, {name}')



cli()