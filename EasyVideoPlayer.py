import cv2
import os
from pathlib import Path
from ffpyplayer.player import MediaPlayer

video_name = input("Name of the video file that you want to play: ")
video_directory_guess = input("Directory that may contain the video: ")

def find_the_video(file_name,directory_name):
    flies_found=[]
    for path,subdirs,files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_path = os.path.join(path,name)
                file_found.append(file_path)

    print(files_found)
    return files_found[0]
