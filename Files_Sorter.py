import os
import shutil
os.chdir("~/Downloads")
files = os.listdir()

extentions = {
        "images":[".jpg",".png",".jpeg",".gif"],
        "videos":[".mp4",".mkv"],
        "musics":[".mp3",".wav"],
        "zip":[".zip",".tgz",".rar",".tar"],
        "documents":[".pdf",".docx",".csv",".xlsx",".doc",".ppt",".xls"],
        "setup":[".msi",".exe"]
        "programs":[".py",".c",".cpp",".php",".C",".CPP"],
        "design":[".xd",".psd"]

        }

def sorting(file):
    keys = list(extensions.key())
    for key in keys:
        for ext in extention[key]:
            if file.endswith(ext):
                return key

    for file in files
    dist = sorting(file)

