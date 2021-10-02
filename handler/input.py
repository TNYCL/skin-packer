import create

def askquestion():
    pname = input('Project Name: ')
    try:
        global file
        file = create.Create(pname)
        print('Success.')
    except KeyError:
        exit("Wrong template file values.")