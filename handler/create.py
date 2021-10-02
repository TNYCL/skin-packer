import os
import json
from util import uuid
from util import file
import input
import shutil

path = input.file.path
pname = input.file.pname
src = "template"

class Create:
    def __init__(self, pname):
        self.pname = pname
        self.path = os.getcwd() + "/projects/" + pname + "/"

    def copyfile(self):
        try:
            shutil.copytree(src, self.path)
            os.rename(self.path + '')
        except FileExistsError:
            print("This project template already have.")
            exit(file.openfolder(self.path))

def manifest():
    try:
        manifest = path + "manifest.json"
        with open(manifest) as file:
            data = json.load(file)
            data["header"]["uuid"] = str(uuid.header)
            data["modules"][0]["uuid"] = str(uuid.modules)
    except Exception:
        exit("ERROR: in manifest() function. (Error #1)")
