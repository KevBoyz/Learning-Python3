import click
from random import randint


@click.group('math')
def math():
    ...


@math.command(help='Randomize numbers')
@click.option('-s', type=click.INT, default=0, help='Randomization start number')
@click.option('-e', type=click.INT, default=9, help='Randomization end number')
@click.option('-c', type=click.INT, default=5, help='Number of characters in random output')
def random(s=0, e=9, c=5):
    if s != 0:
        e = s + 9
    randstr = ''
    for r in range(0, c):
        randstr += str((randint(s, e)))
    if len(randstr) > c:
        click.echo(randstr[0:c + 1])
    else:
        click.echo(randstr)


@math.command(help='Calculate simple probability')
@click.option('-pc', type=click.INT, prompt=True, help='Possible cases')
@click.option('-fc', type=click.INT, prompt=True, help='Favorable cases')
@click.option('-d', '-decimal', is_flag=True, default=False, help='[FLAG] Decimal output')
def prob(pc, fc, d):
    if fc > pc:
        try:
            raise Exception('[fc > pc], Operation not possible')
        except Exception as e:
            click.echo(e)
            return
    if d:
        click.echo(f'{fc / pc}')
    else:
        click.echo(f'{int((fc / pc) * 100)}%')


math()
