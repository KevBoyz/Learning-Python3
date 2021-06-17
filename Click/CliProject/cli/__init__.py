from click import group
from file_handler import Zip
from app_math import *



@group('global')
def Global():
    ...


# Groups declaration
Global.add_command(calc)
Global.add_command(Zip)

# Global Commands
Global.add_command(random)




Global()
