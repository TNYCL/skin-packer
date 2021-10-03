def info(message): return print(color.cyan+'INFO'+color.end+': {}'.format(message))

def success(message): return print(color.green+'SUCCESS'+color.end+': {}'.format(message))

def error(message, type=None): 
    if type != None:
        return exit(color.red+'ERROR ({})'+color.end+': {}'.format(type, message))
    else:
        return exit(color.red+'ERROR'+color.end+': {}'.format(message))

class color:
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'