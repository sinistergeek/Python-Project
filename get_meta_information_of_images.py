from PIL import Image
from PIL.ExifTags import TAGS
from author_utils import get_file_security,get_author
from gps_utils import get_location
import os
import sys
from datetime import datetime

def get_exif(image):
    image.verify()
    return image.getexif()

def get_labeled_exif(exif):
    labeled = {}
    for (key,val) in exif.items():
        labeled[TAGS.get(key)] = val
    return labeled
im = Image.open(sys.argv[1])
name = im.filename
w,h = im.size
_,file_extension = os.path.splitext(sys.argv[1])
exif = get_exif(im)
labeled = get_labeled_exif(exif)
ctime = os.path.getctime(sys.argv[1])
print("ImageName:%s"%(name))
print("size:%sx%s"%(w,h))
print("FileExtension:%s"%(file_extension))
if('ExifImageWidth' in labeled.keys()):
    print("ImageWidth: %s"%(labeled['ExifImageWidth']))
else:
    print('No ImageWidth')

if('ExifImageHeight' in labeled.keys()):
    print("ImageHeight:%s"%(labeled['ExifImageHeight']))
else:
    print("NO Imageheight")


