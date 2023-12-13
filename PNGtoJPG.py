from PIL import Image
im=Image.open("na_first.png").convert("RGB")
im.save("na_first.jpg",'jpeg')
