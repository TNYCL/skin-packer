import os

def openfolder(path):
    path = os.path.realpath(path)
    os.startfile(path)

def checkall():
    directory = os.getcwd() + '/{}'
    if os.path.exists(directory.format('slim')):
        print('+')
        global slim 
        slim = Slim().output
    elif os.path.exists(directory.format('steve')):
        print('-')
        global steve
        steve = Steve().output
    else:
        exit('ERROR: "steve" and "slim" files not found.')

class Slim:
    def __init__(self, names=[]):
        directory = os.getcwd() + '/slim'
        for name in os.listdir(directory):
            realname = name.strip('.png')
            names.append(realname)
            print('Including: {}'.format(name))
        self.output = names

class Steve:
    def __init__(self, names=[]):
        directory = os.getcwd() + '/steve'
        for name in os.listdir(directory):
            realname = name.strip('.png')
            names.append(realname)
            print('Including: {}'.format(name))
        self.output = names
            