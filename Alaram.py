import datetime
import os
import re
import subprocess

def rename_files_with_whitespaces(cd,files,extra_path=""):
    for file in files:
        if "" in file:
            renamed_file = file.replace("","_")
            os.rename(os.path.join(cd,extra_path,file),os.path.join(cd,extra_path,renamed_file))

def clean_filename(file):
    return ''.join(map(str.capitalize,file[:-4].split('_')))


def set_alarm():
    stop = False
    error = True
    while error:
        user_set_time = ":".join(map(lambda x: str(x).zfill(2),input("\nSet the alram time(e.g.01:10):").split(":")))
        if re.match(r"^[0-9]{2}:[0-9]{2}$",user_set_time):
            playback_time = f"{user_set_time}:00.000000"
            error = False
        else:
            print(">>> Error: Time format invalid! Please try again!\n")

    cd = os.path.dirname(os.path.realpath(__file__))
    musics_path = os.path.join(cd,"musics")
    renames_files_with_whitespaces(cd,os.listdir(musics_path),"musics")
    musics = os.listdir(musics_path)

    if len(musics) < 1:
        print(">>> Error: No music in the musics folder! Please add music first!\n")
        exit()

    elif len(musics) == 1:
        print(">> Alarm music has been set default -->" + clean_filename(musics[0]))
        selected_music = musics[0]

    else:
        error = True
        while error:
            try:
                print("\n Select any alaram music:\n")
                for i in range(1,len(musics)+1):
                    print(f"{i}.{clean_filename(musics[i-1])}")
