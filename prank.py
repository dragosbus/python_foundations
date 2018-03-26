import os

def change_name():
    '''
    get file names from folder and change the name for all the files from the selected direcotry
    '''
    #get the current working directory
    path = os.getcwd()
    directory = '{}/prank'.format(path)
    #get the files
    files = os.listdir(directory)
    
    #for each file,rename filenames
    for f in files:
        os.rename("{}/{}".format(directory,f),"{}/{}".format(directory,f[2:]))

change_name()
