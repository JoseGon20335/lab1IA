from PIL import Image, ImageDraw
from numpy import asarray

# Regresa un array reducido de pixeles de la imagen
# Recibe como parametro la ruta de la imagen


def imgPixel(img):
    img2 = Image.open(img)
    img2 = img2.resize((140, 140))

    pixel = Image.new('RGB', (140, 140), (255, 255, 255))
    pixel = img2.load()

    numpydata2 = asarray(img2)
    return numpydata2
