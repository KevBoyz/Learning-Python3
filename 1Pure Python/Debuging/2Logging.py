import logging as log

_format = '%(levelname)s: %(msg)s'

log.basicConfig(filename='Logs.log', filemode='w', level=log.DEBUG, format=_format)


# Check 'Logs.log' file

log.debug('Debug Pattern')
log.info('Just taking information\'s')
log.warning('better fix this')
log.error('Another error .-.')
log.critical('the program is totally crashed')
log.log(60, 'what I\'m say?')  # deb = 10, info = 20, warn = 30, ...

# Example

try:
    1/0
except Exception as e:
    log.warning(e)
    pass