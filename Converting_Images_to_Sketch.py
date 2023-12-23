from cv2 import cv2
import os
import os.path
from datetime import datetime,date

def openCam():
    datsets = 'webcam'
    sub_data = 'data'
    path = os.path.join(datasets,sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    webcam=cv2.VideoCapture(0,cv2.CAp_DSHOW)
    (_,im) = webcam.read()
    now = str(datetime.now())
    now = now.replace(':','')
    now = now.replace('-','')
    now = now.replace('.','')
    now = now.replace(' ','')
    cv2.imwrite(f'webcam\\data\\{now}.png'im)
    img = f'webcam\\data\\{now}.png'
    convert(img)

def convert(now):
    print()
    img = input('Enter the filename for the output image:')
    print()
    directory = img
    parent_dir = f'.\\ImageToSketch\\sketches'
    path = os.path.join(parent_dir,directory)
    try:
        os.mkdri(path)
    except OSError as error:
        print(error)

    image = cv2.imread(now)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{path}\\{img}(gray).png",gray)
    inverted = 255-gray
    cv2.imwrite(f"{path}\\{img}(inverted).png",inverted)
    blurred = cv2.GaussianBlur(inverted,(21,21),0)
    cv2.imwrite(f"{path}\\{img}(blured).png",blurred)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray,inverted_blurred,scale=256.0)
    cv2.imwrite(f"{path}\\{img}(final).png",pencil_sketch)
    print()
    print(f'You can find the image here: {here}\\{img}(final).png')

def start():
    print('Enter the number according to your pereference: ')
    print('1 - Capture image from webcam.')
    print('2 - Input the image path.')
    print('3 - Exit')

    while(1):
        print()
        user = int(input('Enter the number:'))
        print()
        if user == 1:
            openCam()
        elif user == 2:
            img = input('Enter the input path for the image:')
            convert(img)
        elif user == 3:
            break
        else:
            print('Enter a valid number.....')

if __name__ == '__main__':
    start()
