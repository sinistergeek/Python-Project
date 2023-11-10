import os
import requests
import wget
import subprocess
import time
import ctypes
SPI_SETDESKWALLPAPER = 20

def get_wallpaper():
    access_key = "" #add you unspash api key here
    url = 'https://api.unsplash.com/photos/random?client_id='+access_key
    params = {
    'query':'HD wallpapers',
    'orientation':'landscape'
            }
    response = requests.get(url,params=params).json()
    image_source = response['urls']['full']

    image=wget.download(image_source,'C:/Users/projects/wallpaper.jpg')
    return image
def change_wallaper():
    wallpaper = get_wallpaper()
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPO,"C:\\Users\\projects\\wallpaper.jpg",O)

def main():
    try:
        while True:
            change_wallpaper()
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nHope you like this one! Quitting.")
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
