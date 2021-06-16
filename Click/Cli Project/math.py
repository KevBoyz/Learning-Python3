import click
from random import randint


@click.group('math')
def math():
    ...


@math.command()
@click.option('-s', type=click.INT, Default=0, help='Randomization start number')
@click.option('-e', type=click.INT, Default=9, help='Randomization end number')
@click.option('-c', type=click.INT, Default=5, help='Number of characters in random output')
def random(start, end, characters):

