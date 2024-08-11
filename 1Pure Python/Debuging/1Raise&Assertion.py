n = 12
if n > 10:
    try:
        raise Exception('\'n\' is bigger than 10')
    except Exception as error:
        print('ERROR: ', error)


assert n == 11, 'What happened here??'  # Don't use try expect in asserts, when they return false the program need broke