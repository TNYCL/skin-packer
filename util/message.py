def info(message): return print('INFO: {}'.format(message))

def error(message, type=None): 
    if type != None:
        return exit('ERROR ({}): {}'.format(type, message))
    else:
        return exit('ERROR: {}'.format(message))