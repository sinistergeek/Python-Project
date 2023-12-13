from PIL import Image
im = Image.open("na_first.jpg").convert("RGB")
im.save("na_first.jpg","png")
