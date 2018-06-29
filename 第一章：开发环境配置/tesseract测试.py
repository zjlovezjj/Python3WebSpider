import tesserocr
from PIL import Image
image=Image.open('image.png')
print(tesserocr.image_to_text(image)) #用Python3.6版本能正常运行!