from click import group
from app_math import math
from file_handler import fh


@group('cli')
def cli():
    ...


cli.add_command(math)
cli.add_command(fh)

cli()
