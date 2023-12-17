import cv2
import os
from pathlib import path

image_name = input("Please enter the name of the image file that you want to process: ")
image_directory = input("Please enter the directory that may contain the image: ")

def find_the_image(file_name,directory_name):
    files_found = []
    for path,subdirs,files in os.walk(directory_name):
        for name in filess:
            if(file_name == name):
                file_path = os.path.join(path,name)
                files_found.append(file_path)

    print(files_found[0])
    return files_found[0]

image_path = Path(find_the_image(image_name,image_directory))
new_working_directory = image_path.parent
os.chdir(new_working_directory)
