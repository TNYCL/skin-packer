import os
import json
from util import uuid
from util import file
from handler import select
import shutil

path = select.filepath
pname = select.pname
src = "settings"

class Create:
    def __init__(self, pname):
        self.pname = pname
        self.path = os.getcwd() + "/projects/" + pname + "/"

    def copyfile(self):
        try:
            shutil.copytree(src, self.path)
        except FileExistsError:
            print("This project already created.")
            exit(file.openfolder(self.path))

def manifest():
    try:
        manifest = path + "manifest.json"
        with open(manifest) as file:
            data = json.load(file)
            data["header"]["uuid"] = str(uuid.header)
            data["modules"][0]["uuid"] = str(uuid.modules)
    except Exception:
        exit("ERROR: (#1)")
