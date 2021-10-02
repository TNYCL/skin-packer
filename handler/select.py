import tkinter as tk
from util import message as msg
from util import file
from tkinter import filedialog as fd

root = tk.Tk()
root.withdraw()

def opendialog():
    global filepath
    global pname
    pname = input('Project Name: ')
    filepath = fd.askdirectory(title='Select Skin Pack')
    msg.info('Checking folders.')
    file.checkall()