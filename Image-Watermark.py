import os
from PIL import Image
from PIL import ImageFilter

def watermark_photo(input_image_path,output_image_path,watermark_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    position = base_image.size

