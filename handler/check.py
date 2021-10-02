from os import path
import os
import ssl
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

settings_url = "https://cdn.tnycl.com/skin_packer/settings.zip"
template_url = "https://cdn.tnycl.com/skin_packer/template.zip"
settings_exist = path.exists(os.getcwd() + "/settings")
template_exist = path.exists(os.getcwd() + "/template")

def download(extract_to='./settings'):
    if settings_exist == False:
        print('Settings folder not exists, downloading.')
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(settings_url, context=context)
            print('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path=extract_to)
            print('Settings folder successfully created.')
        except Exception:
            exit('ERROR: in download() function. (Error #2)')
    if template_exist == False:
        print('Template folder not exists, downloading.')
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(template_url, context=context)
            print('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path='./template')
            print('Template folder successfully created.')
        except Exception:
            exit('ERROR: in download() function. (Error #2)')
    return True

