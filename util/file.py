import os
from handler import create
from pathlib import Path
from handler import select
from util import message as msg
import shutil

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
        msg.info('Files are verified, progressing.')
        global createdfile
        global skinfolder
        global steve
        global slim
        createdfile = create.Create()
        createdfile.copyfile()
        skinfolder = createdfile.path  + 'Content/skin_pack'
        steve = Steve()
        slim = Slim()
        msg.info('{} skin included.'.format(getskincount()))
        create.createproject()

def getskincount(): return len(steve.output) + len(slim.output)

class Slim:
    def __init__(self, names=[]):
        free = directory.format('/Skins/Slim/Free')
        paid = directory.format('/Skins/Slim/Paid')
        for name in os.listdir(free):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(free + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_customSlim.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.customSlim', realname + '_customSlim.png', 'free')
            msg.info('Including (Slim -> Free): {}'.format(realname))
        for name in os.listdir(paid):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(paid + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_customSlim.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.customSlim', realname + '_customSlim.png', 'paid')
            msg.info('Including (Slim -> Paid): {}'.format(realname))
        self.output = names

class Steve:
    def __init__(self, names=[]):
        free = directory.format('/Skins/Steve/Free')
        paid = directory.format('/Skins/Steve/Paid')
        for name in os.listdir(free):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(free + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_custom.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.custom', realname + '_custom.png', 'free')
            msg.info('Including (Steve -> Free): {}'.format(realname))
        for name in os.listdir(paid):
            realname = name.replace('.png', '')
            names.append(realname)
            shutil.copy(paid + '/' + name, skinfolder)
            os.rename(skinfolder + '/' + name, skinfolder + '/' + realname + '_custom.png')
            create.text_skin(realname)
            create.jsonparse_skin(realname, 'geometry.humanoid.custom', realname + '_custom.png', 'paid')
            msg.info('Including (Steve -> Paid): {}'.format(realname))
        self.output = names
            