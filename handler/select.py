import tkinter as tk
from handler import check
from util import message as msg
from tkinter import filedialog as fd

root = tk.Tk()
root.withdraw()

def opendialog():
    global filepath
    global pname
    check.download()
    pname = input(msg.color.green+'Project Name'+msg.color.end+': ')
    filepath = fd.askdirectory(title='Select Skin Pack')
    msg.info('Checking folders.')
    from util import file
    file.checkall()