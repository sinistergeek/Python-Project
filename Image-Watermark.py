import os
from PIL import Image
from PIL import ImageFilter

def watermark_photo(input_image_path,output_image_path,watermark_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    position = base_image.size
    watermark.size
    newsize = int(position[0]*8/100),int(position[0]*8/100)
    watermark = watermark.resize(newsize)
    new_position = position[0]-newsize[0] - 20, position[1]-newsize[1]-20
    transparent = Image.new(mode="RGBA",size=position,color=(0,0,0,0))
    transparent.paste(base_image,(0,0))
    transparent.paste(watermark,new_position,mask=watermark)
    image_mode = base_image.mode
    if image_mode == "RGB":
        transparent = transparent.convert(image_mode)
    else:

        transparent = transparent.convert("P")
    transparent.save(output_image_path,optimize=True,quality=100)
    print("Saving" + output_image_path + "...")

