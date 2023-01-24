from PIL import Image, ImageDraw
from numpy import asarray


# img = Image.open('prueba.png')
# numpydata = asarray(img)
# print(numpydata)


img2 = Image.open('prueba.png')
img2 = img2.resize((140, 140))

pixel = Image.new('RGB', (140, 140), (255, 255, 255))
pixel = img2.load()

numpydata2 = asarray(img2)
print(numpydata2)
print(pixel)
print(img2)
