import sys
import os
from github import Github
path = ""
username = ""
password = ""

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username,password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created reposity {}".format(folderName))

if __name__ == "__main__":
    create()
