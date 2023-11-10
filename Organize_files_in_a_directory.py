import os
import shutil

filenames=[]

def getfoldername(filename):

    if filename[0].isalpha():
        return filename[0].lower()
    else:
        return 'misc'

def readdirectory():
    global filenames
    for files in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(),files):
                          filenames.append(files))
    filenames.remove('main.py')


def createfolder():
    global filenames
    for f in filenames:
        if os.path.isdir(getfoldername(f)):
            print("foldre already created")
        else:
            os.mkdir(getfoldername(f))
            print('creating folder...')
            
def movetofolder():
    global filenames
    for i in filenames:
        filename=i
        file=getfoldername(i)
        source = os.path.join(os.getcwd(),filename)
        destination = os.path.join(os.getcwd(),file)
        print(f"moving {source} to {destination} ")
        shutil.move(source,destination)

if __name__=='__main__':
    readdirectory()
    createfolder()
    movetofolder()


