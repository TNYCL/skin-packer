import os
from pathlib import Path
from handler import select
from util import message as msg

def openfolder(path):
    path = os.path.realpath(path)
    os.startfile(path)

def checkall():
    global directory
    directory = select.filepath + '/{}'
    if os.path.exists(directory.format('/Skins')) == False:
        msg.error('"Skins" not found.', 'Folder')
    elif os.path.exists(directory.format('/Skins/Slim')) == False:
        msg.error('"Skins/Slim" not found.', 'Folder')
    elif os.path.exists(directory.format('/Skins/Slim/Free')) == False:
        msg.error('"Skins/Slim/Free" not found.', 'Folder')
    elif os.path.exists(directory.format('/Skins/Slim/Paid')) == False:
        msg.error('"Skins/Slim/Paid" not found.', 'Folder')
    elif os.path.exists(directory.format('/Skins/Steve')) == False:
        msg.error('"Skins/Steve" not found.', 'Folder')
    elif os.path.exists(directory.format('/Skins/Steve/Free')) == False:
        msg.error('"Skins/Steve/Free" not found.', 'Folder')
    elif os.path.exists(directory.format('/Skins/Steve/Paid')) == False:
        msg.error('"Skins/Steve/Paid" not found.', 'Folder')
    elif os.path.exists(directory.format('/Arts')) == False:
        msg.error('"Arts" not found.', 'Folder')
    elif Path(directory.format('/Arts/keyart.png')).is_file() == False:
        msg.error('"Arts/keyart.png" not found.', 'File')
    elif Path(directory.format('/Arts/partnerart.png')).is_file() == False:
        msg.error('"Arts/partnerart.png" not found.', 'File')
    elif Path(directory.format('/Arts/thumbnail.jpg')).is_file() == False:
        msg.error('"Arts/thumbnail.jpg" not found.', 'File')
    else:
        msg.info('Files are verified, progressing skin files.')
        global steve
        global slim
        steve = Steve()
        slim = Slim()

def getskincount(): return len(steve.output) + len(slim.output)

class Slim:
    def __init__(self, names=[]):
        free = directory.format('/Skins/Slim/Free')
        paid = directory.format('/Skins/Slim/Paid')
        for name in os.listdir(free):
            realname = name.strip('.png')
            names.append(realname)
            msg.info('Including (Slim -> Free): {}'.format(name))
        for name in os.listdir(paid):
            realname = name.strip('.png')
            names.append(realname)
            msg.info('Including (Slim -> Paid): {}'.format(name))
        self.output = names

class Steve:
    def __init__(self, names=[]):
        free = directory.format('/Skins/Steve/Free')
        paid = directory.format('/Skins/Steve/Paid')
        for name in os.listdir(free):
            realname = name.strip('.png')
            names.append(realname)
            msg.info('Including (Steve -> Free): {}'.format(name))
        for name in os.listdir(paid):
            realname = name.strip('.png')
            names.append(realname)
            msg.info('Including (Steve -> Paid): {}'.format(name))
        self.output = names
            