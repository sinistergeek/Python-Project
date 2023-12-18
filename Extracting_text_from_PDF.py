import pdf2image
import os,sys
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
PATH = 'Enter your path'
i=1
def delete_ppms():
    for file in os.listdir(PATH):
        if '.ppm' in file or '.DS_store' in file:
            try:
                os.remove(PATH + file)
            except FileNotFoundError:
                pass
pdf_files = []
docx_files = []

