def info(message): return print('INFO: {}'.format(message))

def error(message, type): return exit('ERROR ({}): {}'.format(type, message))